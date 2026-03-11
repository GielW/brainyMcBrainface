#!/usr/bin/env python3
"""
Brain compiler — assembles modular brain files into project-specific standalone claude.md files.

Reads the modular brain (skills, languages, domains, projects) and produces a single
self-contained claude.md per project that can be pushed to the project repo.

Usage:
    python tools/compile-brain.py [project | all]       Compile to compiled/<project>/
    python tools/compile-brain.py all --output-dir out/  Custom output directory
    python tools/compile-brain.py all --dry-run           Show what would be compiled
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BRAIN_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BRAIN_DIR / ".sync-config.json"
DEFAULT_OUTPUT = BRAIN_DIR / "compiled"

# ── Feedback loop instruction (injected into every compiled file) ────────────

FEEDBACK_LOOP_SECTION = """\
## ⚠️ Brain Feedback Loop — Self-Learning System

This file is auto-compiled from **brainyMcBrain**. When you discover reusable knowledge during this session, **do not just tell the user** — actively push it back to the brain.

### When to Trigger

| Trigger | Example |
|---------|---------|
| New convention established | "We decided to use X pattern for all services" |
| Recurring mistake fixed | "This is the third time — document the rule" |
| Tool/workflow discovered | "This CLI flag saves time" |
| Legal/regulatory reference | "New GBA guideline" |
| Cross-project pattern | "Multiple projects share this pattern" |

### Do NOT Trigger For

- One-off debugging steps or temporary workarounds
- Project-specific data (serial numbers, API keys, etc.)
- Information already covered in this file

### How to Report Back

When you detect reusable knowledge, **create a GitHub Issue on brainyMcBrain**:

```bash
gh issue create --repo GielW/brainyMcBrain \\
  --title "[brain-update] <short description>" \\
  --label "brain-update,triage" \\
  --body "## Source Project
{project_name}

## Suggested Target File
<!-- one of: skills/*.md, languages/*.md, domains/*.md, projects/*.md, or 'new file needed' -->
<target>

## Category
<!-- Convention | Pattern fix | Tool/workflow | Legal/regulatory | Cross-project -->
<category>

## Knowledge Content
<the actual rule, convention, or pattern — write it as it should appear in the skill file>

## Context
<what happened that surfaced this knowledge>"
```

### Brain Update Rules

1. **Always ask the user first**: _"I found reusable knowledge: [summary]. Shall I push this to brainyMcBrain?"_
2. Only create the issue after user confirms
3. One issue per piece of knowledge (don't bundle)
4. Write the knowledge content as you'd want it to appear in the target skill file
"""

# ── Helpers ──────────────────────────────────────────────────────────────────


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def read_md(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter (--- ... ---) from the start of a file."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3 :].lstrip("\n")
    return content


def demote_headings(content: str, levels: int = 2) -> str:
    """Demote all markdown headings by N levels (# → ###)."""
    def _demote(match: re.Match) -> str:
        hashes = match.group(1)
        rest = match.group(2)
        new_level = min(len(hashes) + levels, 6)  # cap at h6
        return "#" * new_level + rest

    return re.sub(r"^(#{1,6})([ \t]+.*)$", _demote, content, flags=re.MULTILINE)


def parse_project_skills(project_file: Path) -> dict:
    """Parse Skills and External Skills from a project file's blockquote header."""
    content = read_md(project_file)
    result = {"languages": [], "domains": [], "external_skills": []}

    for line in content.splitlines():
        if line.startswith("> **Skills**:"):
            refs = re.findall(r"@((?:languages|domains)/[\w\-]+\.md)", line)
            for ref in refs:
                if ref.startswith("languages/"):
                    result["languages"].append(ref)
                elif ref.startswith("domains/"):
                    result["domains"].append(ref)
        elif line.startswith("> **External Skills**:"):
            refs = re.findall(r"@(skills-external/[\w\-/]+\.md)", line)
            result["external_skills"] = refs

    return result


def get_universal_skills() -> list[str]:
    """Get the list of universal skill file paths from CLAUDE.md's @-imports."""
    claude_md = read_md(BRAIN_DIR / "CLAUDE.md")
    skills = []
    in_section = False

    for line in claude_md.splitlines():
        if "## Universal Skills" in line:
            in_section = True
            continue
        if in_section:
            if line.startswith("##"):
                break
            match = re.match(r"^@(.+\.md)\s*$", line.strip())
            if match:
                skills.append(match.group(1))

    return skills


def section(title: str, content: str) -> str:
    """Wrap content in a markdown section with a separator."""
    return f"### {title}\n\n{content.strip()}\n\n---\n"


# ── Compiler ─────────────────────────────────────────────────────────────────


def compile_project(project_name: str, config: dict, output_dir: Path) -> Path:
    """Compile a single project's standalone claude.md."""
    # Find project config
    project_config = None
    for p in config["projects"]:
        if p["name"] == project_name:
            project_config = p
            break
    if not project_config:
        print(f"  ERROR: '{project_name}' not found in .sync-config.json", file=sys.stderr)
        sys.exit(1)

    project_file = BRAIN_DIR / "projects" / f"{project_name}.md"
    if not project_file.exists():
        print(f"  ERROR: Project file not found: {project_file}", file=sys.stderr)
        sys.exit(1)

    # Parse project dependencies
    project_skills = parse_project_skills(project_file)
    universal_skills = get_universal_skills()

    parts: list[str] = []
    included_files: list[str] = []

    # ── Header ──
    target = project_config["target_file"]
    parts.append(f"# {target} — {project_name}\n")
    parts.append(
        "> **Auto-compiled from [brainyMcBrain](https://github.com/GielW/brainyMcBrain).**\n"
        "> Do not edit directly — changes will be overwritten on next sync.\n"
    )
    parts.append("---\n")

    # ── Identity ──
    identity_path = BRAIN_DIR / "skills" / "identity.md"
    if identity_path.exists():
        parts.append("## Identity\n")
        parts.append(demote_headings(strip_frontmatter(read_md(identity_path))).strip())
        parts.append("\n\n---\n")
        included_files.append("skills/identity.md")

    # ── Universal Skills ──
    parts.append("## Universal Skills\n")
    for skill_rel in universal_skills:
        if skill_rel == "skills/identity.md":
            continue  # already included above
        skill_path = BRAIN_DIR / skill_rel
        if skill_path.exists():
            content = demote_headings(strip_frontmatter(read_md(skill_path)))
            parts.append(content.strip())
            parts.append("\n\n---\n")
            included_files.append(skill_rel)
        else:
            parts.append(f"<!-- MISSING: {skill_rel} -->\n")

    # ── Language Skills ──
    if project_skills["languages"]:
        parts.append("## Language Skills\n")
        for lang_rel in project_skills["languages"]:
            lang_path = BRAIN_DIR / lang_rel
            if lang_path.exists():
                content = demote_headings(strip_frontmatter(read_md(lang_path)))
                parts.append(content.strip())
                parts.append("\n\n---\n")
                included_files.append(lang_rel)
            else:
                parts.append(f"<!-- MISSING: {lang_rel} -->\n")

    # ── Domain Skills ──
    if project_skills["domains"]:
        parts.append("## Domain Skills\n")
        for domain_rel in project_skills["domains"]:
            domain_path = BRAIN_DIR / domain_rel
            if domain_path.exists():
                content = demote_headings(strip_frontmatter(read_md(domain_path)))
                parts.append(content.strip())
                parts.append("\n\n---\n")
                included_files.append(domain_rel)
            else:
                parts.append(f"<!-- MISSING: {domain_rel} -->\n")

    # ── External Skills reference ──
    if project_skills["external_skills"]:
        parts.append("## External Skills\n")
        parts.append(
            "The following external skills from [anthropics/skills](https://github.com/anthropics/skills) "
            "are available for this project. Reference them with `@<path>` when needed:\n"
        )
        for ext in project_skills["external_skills"]:
            parts.append(f"- `@{ext}`")
        parts.append("\n\n---\n")

    # ── Project Context ──
    parts.append("## Project Context\n")
    project_content = demote_headings(strip_frontmatter(read_md(project_file)))
    parts.append(project_content.strip())
    parts.append("\n\n---\n")

    # ── Feedback Loop ──
    parts.append(FEEDBACK_LOOP_SECTION.format(project_name=project_name))
    parts.append("\n")

    # ── Compose ──
    compiled = "\n".join(parts).strip() + "\n"
    # Collapse consecutive blank lines (MD012)
    compiled = re.sub(r"\n{3,}", "\n\n", compiled)

    # ── Write ──
    out_path = output_dir / project_name / project_config["target_file"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(compiled, encoding="utf-8")

    return out_path, included_files


# ── CLI ──────────────────────────────────────────────────────────────────────


def _lint_compiled(output_dir: Path, targets: list[str]) -> None:
    """Run markdownlint on compiled files if markdownlint-cli2 is available."""
    import shutil
    import subprocess

    if not shutil.which("markdownlint-cli2"):
        print("\n  ℹ markdownlint-cli2 not found — skipping lint (install via: npm i -g markdownlint-cli2)")
        return

    files = [str(output_dir / name / "*.md") for name in targets]
    result = subprocess.run(
        ["markdownlint-cli2"] + files,
        capture_output=True,
        text=True,
        cwd=BRAIN_DIR,
    )

    if result.returncode == 0:
        print(f"\n  ✓ Markdown lint: all compiled files clean")
    else:
        print(f"\n  ⚠ Markdown lint warnings in compiled output:")
        for line in result.stdout.strip().splitlines():
            print(f"    {line}")
        for line in result.stderr.strip().splitlines():
            print(f"    {line}")


def main():
    parser = argparse.ArgumentParser(description="Compile modular brain into project-specific claude.md files")
    parser.add_argument("project", nargs="?", default="all", help="Project name or 'all'")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be compiled without writing")
    args = parser.parse_args()

    config = load_config()
    project_names = [p["name"] for p in config["projects"]]

    if args.project == "all":
        targets = project_names
    elif args.project in project_names:
        targets = [args.project]
    else:
        print(f"Unknown project '{args.project}'. Available: {', '.join(project_names)}")
        sys.exit(1)

    print(f"══ Brain Compiler ══")
    print(f"Output: {args.output_dir}/\n")

    for name in targets:
        project_file = BRAIN_DIR / "projects" / f"{name}.md"
        skills = parse_project_skills(project_file)

        if args.dry_run:
            print(f"  {name}:")
            print(f"    Languages: {skills['languages'] or '(none)'}")
            print(f"    Domains:   {skills['domains'] or '(none)'}")
            print(f"    External:  {len(skills['external_skills'])} skill(s)")
            print()
            continue

        out_path, included = compile_project(name, config, args.output_dir)
        line_count = out_path.read_text(encoding="utf-8").count("\n")
        print(f"  ✓ {name} — {len(included)} files inlined, {line_count} lines → {out_path.relative_to(BRAIN_DIR)}")

    if not args.dry_run:
        _lint_compiled(args.output_dir, targets)
        print(f"\n══ Done ══")


if __name__ == "__main__":
    main()
