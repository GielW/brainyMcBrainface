#!/usr/bin/env python3
"""
Brain linter — validates internal consistency of the brainyMcBrainface knowledge repo.

Checks:
  1. All @-imports in CLAUDE.md resolve to existing files
  2. All files in skills/, languages/, domains/ are referenced by at least one @-import
  3. All .md files in skills/, languages/, domains/ have valid YAML frontmatter
  4. Routing table entries match actual files
  5. .sync-config.json projects match projects/*.md files
  6. Project file skill references (@languages/*, @domains/*) resolve to existing files

Usage:
    python tools/validate-brain.py          Run all checks
    python tools/validate-brain.py --fix    Auto-fix trivial issues (future)

Exit code: 0 = pass, 1 = warnings only, 2 = errors found
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BRAIN_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BRAIN_DIR / ".sync-config.json"

errors: list[str] = []
warnings: list[str] = []


def error(msg: str) -> None:
    errors.append(msg)
    print(f"  ERROR  {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  WARN   {msg}")


def ok(msg: str) -> None:
    print(f"  OK     {msg}")


# ── Check 1: @-imports in CLAUDE.md resolve to files ─────────────────────────


def check_imports():
    print("\n── @-imports in CLAUDE.md ──")
    claude_md = (BRAIN_DIR / "CLAUDE.md").read_text(encoding="utf-8")
    imports = re.findall(r"^@(.+\.md)\s*$", claude_md, re.MULTILINE)

    if not imports:
        error("No @-imports found in CLAUDE.md")
        return

    for ref in imports:
        path = BRAIN_DIR / ref
        if path.exists():
            ok(f"@{ref}")
        else:
            error(f"@{ref} → file not found: {path}")


# ── Check 2: Orphan files (in dirs but not referenced) ──────────────────────


def check_orphans():
    print("\n── Orphan check (unreferenced files) ──")
    claude_md = (BRAIN_DIR / "CLAUDE.md").read_text(encoding="utf-8")
    all_imports = set(re.findall(r"@([\w\-/]+\.md)", claude_md))

    # Also gather references from project files
    for pf in (BRAIN_DIR / "projects").glob("*.md"):
        content = pf.read_text(encoding="utf-8")
        all_imports.update(re.findall(r"@([\w\-/]+\.md)", content))

    for folder in ["skills", "languages", "domains", "projects"]:
        for md_file in (BRAIN_DIR / folder).glob("*.md"):
            rel = md_file.relative_to(BRAIN_DIR).as_posix()
            if rel in all_imports:
                ok(f"{rel} — referenced")
            else:
                warn(f"{rel} — not referenced by any @-import")


# ── Check 3: YAML frontmatter ───────────────────────────────────────────────


def check_frontmatter():
    print("\n── YAML frontmatter ──")
    for folder in ["skills", "languages", "domains"]:
        for md_file in sorted((BRAIN_DIR / folder).glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            rel = md_file.relative_to(BRAIN_DIR).as_posix()

            if not content.startswith("---"):
                error(f"{rel} — missing YAML frontmatter")
                continue

            end = content.find("---", 3)
            if end == -1:
                error(f"{rel} — unclosed YAML frontmatter")
                continue

            fm = content[3:end].strip()
            has_name = any(line.startswith("name:") for line in fm.splitlines())
            has_desc = any(line.startswith("description:") for line in fm.splitlines())

            if not has_name:
                error(f"{rel} — frontmatter missing 'name'")
            if not has_desc:
                error(f"{rel} — frontmatter missing 'description'")
            if has_name and has_desc:
                ok(f"{rel}")


# ── Check 4: Routing table matches files ─────────────────────────────────────


def check_routing_table():
    print("\n── Routing table ──")
    claude_md = (BRAIN_DIR / "CLAUDE.md").read_text(encoding="utf-8")

    # Find routing table entries: | ... | `path/file.md` |
    routes = re.findall(r"\|\s*`([\w\-/]+\.md)`\s*\|", claude_md)

    if not routes:
        warn("No routing table entries found")
        return

    for route in routes:
        if route.startswith("projects/<"):
            continue  # template entry
        path = BRAIN_DIR / route
        if path.exists():
            ok(f"Route → {route}")
        else:
            error(f"Route → {route} — file not found")


# ── Check 5: .sync-config.json ↔ projects/*.md ──────────────────────────────


def check_sync_config():
    print("\n── Sync config vs project files ──")

    if not CONFIG_PATH.exists():
        error(".sync-config.json not found")
        return

    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    config_names = {p["name"] for p in config["projects"]}
    project_files = {p.stem for p in (BRAIN_DIR / "projects").glob("*.md")}

    for name in config_names:
        if name in project_files:
            ok(f"Config '{name}' has matching projects/{name}.md")
        else:
            error(f"Config '{name}' has no matching projects/{name}.md")

    for name in project_files:
        if name not in config_names:
            warn(f"projects/{name}.md has no matching entry in .sync-config.json")


# ── Check 6: Project file skill references resolve ──────────────────────────


def check_project_refs():
    print("\n── Project file references ──")
    for pf in sorted((BRAIN_DIR / "projects").glob("*.md")):
        content = pf.read_text(encoding="utf-8")
        rel = pf.relative_to(BRAIN_DIR).as_posix()
        refs = re.findall(r"@((?:languages|domains|skills)/[\w\-]+\.md)", content)
        ext_refs = re.findall(r"@(skills-external/[\w\-/]+\.md)", content)

        all_ok = True
        for ref in refs:
            if not (BRAIN_DIR / ref).exists():
                error(f"{rel} references @{ref} — file not found")
                all_ok = False

        for ref in ext_refs:
            if not (BRAIN_DIR / ref).exists():
                warn(f"{rel} references @{ref} — external skill not found (submodule may need init)")
                all_ok = False

        if all_ok:
            ok(f"{rel} — {len(refs) + len(ext_refs)} references valid")


# ── Main ─────────────────────────────────────────────────────────────────────


def main():
    print("══ Brain Linter ══")

    check_imports()
    check_orphans()
    check_frontmatter()
    check_routing_table()
    check_sync_config()
    check_project_refs()

    print(f"\n══ Summary: {len(errors)} error(s), {len(warnings)} warning(s) ══")

    if errors:
        sys.exit(2)
    elif warnings:
        sys.exit(1)
    else:
        print("All checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
