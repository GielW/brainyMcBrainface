#!/usr/bin/env python3
"""
Project scaffold — registers a new project in the brainyMcBrain knowledge repo.

Creates:
  1. projects/<name>.md — stub with Skills header
  2. .sync-config.json  — new project entry appended
  3. CLAUDE.md           — @projects/<name>.md import added
  4. Workflow dropdowns   — updated in sync-to-projects.yml and todo-to-issues.yml

Optionally:
  --compile   Run the brain compiler after scaffolding
  --push      Compile + push initial claude.md to the project repo

Usage:
    python tools/init-project.py MyProject --repo GielW/MyProject
    python tools/init-project.py MyProject --repo GielW/MyProject --languages python --domains belgian-legal obsidian-vault
    python tools/init-project.py MyProject --repo GielW/MyProject --compile
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

BRAIN_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BRAIN_DIR / ".sync-config.json"
CLAUDE_MD = BRAIN_DIR / "CLAUDE.md"
SYNC_WORKFLOW = BRAIN_DIR / ".github" / "workflows" / "sync-to-projects.yml"
TODO_WORKFLOW = BRAIN_DIR / ".github" / "workflows" / "todo-to-issues.yml"
PROJECTS_DIR = BRAIN_DIR / "projects"

# Available modules (auto-discovered from filesystem)
AVAILABLE_LANGUAGES = sorted(p.stem for p in (BRAIN_DIR / "languages").glob("*.md"))
AVAILABLE_DOMAINS = sorted(p.stem for p in (BRAIN_DIR / "domains").glob("*.md"))
AVAILABLE_EXTERNAL = sorted(
    p.name
    for p in (BRAIN_DIR / "skills-external" / "anthropic" / "skills").iterdir()
    if p.is_dir() and (p / "SKILL.md").exists()
)


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_config(config: dict) -> None:
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write("\n")


def existing_project_names(config: dict) -> set[str]:
    return {p["name"] for p in config["projects"]}


# ── Scaffold steps ───────────────────────────────────────────────────────────


def create_project_file(
    name: str,
    repo: str,
    languages: list[str],
    domains: list[str],
    external_skills: list[str],
    description: str,
) -> Path:
    """Create projects/<name>.md with the standard header format."""
    path = PROJECTS_DIR / f"{name}.md"
    if path.exists():
        print(f"  SKIP: {path.relative_to(BRAIN_DIR)} already exists")
        return path

    # Build Skills line
    skill_refs = ["@skills/* (all)"]
    for lang in languages:
        skill_refs.append(f"@languages/{lang}.md")
    for dom in domains:
        skill_refs.append(f"@domains/{dom}.md")
    skills_line = ", ".join(skill_refs)

    # Build External Skills line
    ext_line = ""
    if external_skills:
        ext_refs = [f"@skills-external/anthropic/skills/{s}/SKILL.md" for s in external_skills]
        ext_line = f'>\n> **External Skills**: {", ".join(ext_refs)}'

    content = f"""# {name}

> **Skills**: {skills_line}{ext_line}

## Project Overview

{description or f"<!-- TODO: Describe {name} here -->"}

- **Repository**: `{repo}`

## Active Skills

This project uses:
"""
    # Add active skill descriptions
    for lang in languages:
        content += f"- **{lang.replace('-', '/')}**\n"
    for dom in domains:
        content += f"- **{dom.replace('-', ' ')}**\n"
    for ext in external_skills:
        content += f"- **{ext}** _(external)_\n"

    content += """
## Key Files

| Purpose | File |
|---|---|
| Project overview | `README.md` |
<!-- TODO: Add key files -->

## Cross-Reference Map

| When you change... | Also update... |
|---|---|
<!-- TODO: Add cross-references -->
"""

    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  ✓ Created {path.relative_to(BRAIN_DIR)}")
    return path


def update_sync_config(
    name: str,
    repo: str,
    target_file: str,
    local_path: str | None,
    todo_file: str | None,
    config: dict,
) -> dict:
    """Add the new project to .sync-config.json."""
    if name in existing_project_names(config):
        print(f"  SKIP: {name} already in .sync-config.json")
        return config

    github_base = config.get("github_base", "")
    entry: dict = {
        "name": name,
        "repo": repo,
        "target_file": target_file,
    }
    if todo_file:
        entry["todo_file"] = todo_file
    if local_path:
        entry["source"] = local_path
    elif github_base:
        entry["source"] = f"{github_base}/{name}/{target_file}"
    entry["repo_path"] = f"projects-archive/{name}/{target_file}"

    config["projects"].append(entry)
    save_config(config)
    print(f"  ✓ Added {name} to .sync-config.json")
    return config


def update_claude_md(name: str) -> None:
    """Add @projects/<name>.md import to the Active Projects section."""
    import_line = f"@projects/{name}.md"
    content = CLAUDE_MD.read_text(encoding="utf-8")

    if import_line in content:
        print(f"  SKIP: {import_line} already in CLAUDE.md")
        return

    # Find the Active Projects section and append before the next ---
    lines = content.splitlines()
    insert_idx = None
    in_section = False

    for i, line in enumerate(lines):
        if "## Active Projects" in line:
            in_section = True
            continue
        if in_section:
            if line.strip() == "---":
                insert_idx = i
                break

    if insert_idx is None:
        print("  WARN: Could not find Active Projects section in CLAUDE.md")
        return

    # Insert before the --- separator, after the last @projects line
    # Walk back to find the last @projects line
    last_import = insert_idx
    for j in range(insert_idx - 1, 0, -1):
        if lines[j].strip().startswith("@projects/"):
            last_import = j + 1
            break
        if lines[j].strip() and not lines[j].strip().startswith("@"):
            break

    lines.insert(last_import, import_line)
    CLAUDE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  ✓ Added {import_line} to CLAUDE.md")


def update_workflow_dropdown(workflow_path: Path, name: str) -> None:
    """Add project name to a workflow's dropdown options list."""
    if not workflow_path.exists():
        return

    content = workflow_path.read_text(encoding="utf-8")
    label = workflow_path.name

    # Check if already present
    if re.search(rf"^\s+- {re.escape(name)}\s*$", content, re.MULTILINE):
        print(f"  SKIP: {name} already in {label} dropdown")
        return

    # Find the options: block and the last project entry (before any non-project entry)
    lines = content.splitlines()
    in_options = False
    last_option_idx = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "options:":
            in_options = True
            continue
        if in_options:
            if stripped.startswith("- "):
                last_option_idx = i
            else:
                break

    if last_option_idx is None:
        print(f"  WARN: Could not find options list in {label}")
        return

    # Determine indentation from the last option line
    indent = re.match(r"^(\s*)", lines[last_option_idx]).group(1)
    lines.insert(last_option_idx + 1, f"{indent}- {name}")
    workflow_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  ✓ Added {name} to {label} dropdown")


def run_compiler(name: str) -> None:
    """Run the brain compiler for the new project."""
    print(f"\n── Compiling {name} ──")
    result = subprocess.run(
        [sys.executable, str(BRAIN_DIR / "tools" / "compile-brain.py"), name],
        cwd=BRAIN_DIR,
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


# ── CLI ──────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new project in brainyMcBrain",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available languages: {', '.join(AVAILABLE_LANGUAGES)}
Available domains:   {', '.join(AVAILABLE_DOMAINS)}
Available external:  {', '.join(AVAILABLE_EXTERNAL)}
""",
    )
    parser.add_argument("name", help="Project name (PascalCase or as-is)")
    parser.add_argument("--repo", required=True, help="GitHub repo (e.g., GielW/MyProject)")
    parser.add_argument(
        "--languages",
        nargs="+",
        default=[],
        choices=AVAILABLE_LANGUAGES,
        help="Language modules to include",
    )
    parser.add_argument(
        "--domains",
        nargs="+",
        default=[],
        choices=AVAILABLE_DOMAINS,
        help="Domain modules to include",
    )
    parser.add_argument(
        "--external",
        nargs="+",
        default=[],
        choices=AVAILABLE_EXTERNAL,
        metavar="SKILL",
        help="External skills to include",
    )
    parser.add_argument(
        "--target-file",
        default="claude.md",
        help="Name of the claude.md file in the target repo (default: claude.md)",
    )
    parser.add_argument("--todo-file", default=None, help="Path to TODO/progress file in the target repo")
    parser.add_argument("--local-path", default=None, help="Local clone path for sync.sh")
    parser.add_argument("--description", default="", help="One-line project description")
    parser.add_argument("--compile", action="store_true", help="Run brain compiler after scaffolding")
    parser.add_argument("--push", action="store_true", help="Compile + push initial claude.md (implies --compile)")

    args = parser.parse_args()

    if args.push:
        args.compile = True

    config = load_config()

    # Validate name isn't taken
    if args.name in existing_project_names(config):
        # Allow re-running to fix partial scaffolds
        print(f"Note: {args.name} already exists in config. Will update missing pieces only.\n")

    print(f"══ Scaffolding project: {args.name} ══\n")

    # 1. Create project file
    create_project_file(
        name=args.name,
        repo=args.repo,
        languages=args.languages,
        domains=args.domains,
        external_skills=args.external,
        description=args.description,
    )

    # 2. Update .sync-config.json
    config = update_sync_config(
        name=args.name,
        repo=args.repo,
        target_file=args.target_file,
        local_path=args.local_path,
        todo_file=args.todo_file,
        config=config,
    )

    # 3. Update CLAUDE.md
    update_claude_md(args.name)

    # 4. Update workflow dropdowns
    update_workflow_dropdown(SYNC_WORKFLOW, args.name)
    update_workflow_dropdown(TODO_WORKFLOW, args.name)

    print(f"\n══ Scaffold complete ══")

    # 5. Optionally compile
    if args.compile:
        run_compiler(args.name)

    # 6. Optionally push
    if args.push:
        print(f"\n── Pushing to {args.repo} ──")
        print("Trigger the sync workflow manually or push to main to auto-sync.")
        print(f"Or run: gh workflow run 'Sync claude.md to projects' -f project={args.name}")

    # Summary
    print(f"\nNext steps:")
    if not args.compile:
        print(f"  1. Edit projects/{args.name}.md — fill in project details")
        print(f"  2. Run: python3 tools/compile-brain.py {args.name}")
    else:
        print(f"  1. Edit projects/{args.name}.md — fill in project details")
    print(f"  3. Commit and push to main → auto-sync will push to {args.repo}")


if __name__ == "__main__":
    main()
