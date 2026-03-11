#!/usr/bin/env python3
"""
todo-to-issues.py — Parse TODO.md tables and sync them to GitHub Issues.

Reads markdown TODO files with the brainyMcBrainface table format:
    | # | Phase | Status | Priority | Description |

Creates/updates GitHub Issues with matching labels, and closes issues
when the TODO status is "Done".

Requires: gh CLI (authenticated), Python 3.9+
"""

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

# ── Config ───────────────────────────────────────────────────────────────────

SYNC_CONFIG = Path(__file__).parent.parent / ".sync-config.json"

# Map TODO status values → GitHub Issue state
STATUS_MAP = {
    "done": "closed",
    "open": "open",
    "in progress": "open",
}

# Labels to create/use on each repo
PHASE_LABELS = {
    "P0": "phase:P0-security",
    "P1": "phase:P1-core",
    "P2": "phase:P2-architecture",
    "P3": "phase:P3-decomposition",
    "P4": "phase:P4-testing",
    "PX": "phase:PX-extras",
}

PRIORITY_LABELS = {
    "high": "priority:high",
    "medium": "priority:medium",
    "low": "priority:low",
}

SYNC_LABEL = "synced-from-todo"


# ── Data ─────────────────────────────────────────────────────────────────────

@dataclass
class TodoItem:
    number: str
    phase: str
    status: str
    priority: str
    description: str
    section: str  # e.g., "programmingView.dart"


@dataclass
class ProjectConfig:
    name: str
    repo: str
    todo_file: str  # relative path within the project repo


# ── Parsing ──────────────────────────────────────────────────────────────────

# Format A: ilumenTool-style — | # | Phase | Status | Priority | Description |
TABLE_ROW_A = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\w+)\s*\|\s*([\w\s]+?)\s*\|\s*(\w+)\s*\|\s*(.+?)\s*\|$"
)

# Format B: DPO-Dashboard-style — | Task | ✅ Done | Date | or | Task | ⬜ Not started | — |
TABLE_ROW_B = re.compile(
    r"^\|\s*(.+?)\s*\|\s*(✅\s*Done|⬜\s*Not started|🟡\s*In Progress|⬜\s*Pending)\s*\|\s*(.+?)\s*\|$"
)

SECTION_RE = re.compile(r"^###?\s+`?(.+?)`?\s*$")

STATUS_EMOJI_MAP = {
    "✅ done": "done",
    "⬜ not started": "open",
    "🟡 in progress": "in progress",
    "⬜ pending": "open",
}


def parse_todo_file(content: str) -> list[TodoItem]:
    """Parse a markdown TODO file into TodoItem objects."""
    items = []
    current_section = "General"
    auto_num = 1

    for line in content.splitlines():
        # Track section headers
        section_match = SECTION_RE.match(line)
        if section_match:
            current_section = section_match.group(1).strip()
            continue

        # Try Format A (ilumenTool-style)
        row_match = TABLE_ROW_A.match(line)
        if row_match:
            items.append(TodoItem(
                number=row_match.group(1).strip(),
                phase=row_match.group(2).strip(),
                status=row_match.group(3).strip().lower(),
                priority=row_match.group(4).strip().lower(),
                description=row_match.group(5).strip(),
                section=current_section,
            ))
            continue

        # Try Format B (DPO-Dashboard-style)
        row_match_b = TABLE_ROW_B.match(line)
        if row_match_b:
            task = row_match_b.group(1).strip()
            status_raw = row_match_b.group(2).strip().lower()
            # Skip header/separator rows and metadata rows
            if task.lower() in ("task", "---", "metric") or task.startswith("**"):
                continue
            status = STATUS_EMOJI_MAP.get(status_raw, "open")
            items.append(TodoItem(
                number=str(auto_num),
                phase="P1",
                status=status,
                priority="medium",
                description=task,
                section=current_section,
            ))
            auto_num += 1

    return items


# ── GitHub CLI helpers ───────────────────────────────────────────────────────

def gh(args: list[str], check: bool = True) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True, text=True, check=check,
    )
    return result.stdout.strip()


def gh_json(args: list[str]) -> list[dict]:
    """Run a gh CLI command that returns JSON."""
    raw = gh(args, check=True)
    if not raw:
        return []
    return json.loads(raw)


def ensure_labels(repo: str) -> None:
    """Create required labels if they don't exist."""
    existing_raw = gh(["label", "list", "--repo", repo, "--json", "name", "--limit", "100"])
    existing = {l["name"] for l in json.loads(existing_raw)} if existing_raw else set()

    labels_needed = {
        SYNC_LABEL: "4a86c7",
        **{v: "d4c5f9" for v in PHASE_LABELS.values()},
        **{v: "fbca04" for v in PRIORITY_LABELS.values()},
    }

    for label, color in labels_needed.items():
        if label not in existing:
            gh(["label", "create", label, "--repo", repo,
                "--color", color, "--force"], check=False)
            print(f"    Created label: {label}")


def get_existing_issues(repo: str) -> dict[str, dict]:
    """Get all open+closed issues with the sync label. Returns {title: issue}."""
    issues = gh_json([
        "issue", "list", "--repo", repo,
        "--label", SYNC_LABEL,
        "--state", "all",
        "--json", "number,title,state,labels",
        "--limit", "500",
    ])
    return {i["title"]: i for i in issues}


def build_issue_title(project_name: str, item: TodoItem) -> str:
    """Consistent title format for synced issues."""
    return f"[TODO #{item.number}] {item.description}"


def build_issue_body(item: TodoItem, project_name: str) -> str:
    """Build the issue body with metadata."""
    return (
        f"**Source:** `{project_name}` TODO #{item.number}\n"
        f"**Section:** {item.section}\n"
        f"**Phase:** {item.phase}\n"
        f"**Priority:** {item.priority}\n"
        f"**Status in TODO.md:** {item.status}\n\n"
        f"---\n\n"
        f"{item.description}\n\n"
        f"---\n"
        f"*Auto-synced from TODO.md by brainyMcBrainface*"
    )


def sync_item(repo: str, project_name: str, item: TodoItem, existing: dict[str, dict]) -> str:
    """Sync a single TODO item to GitHub Issues. Returns action taken."""
    title = build_issue_title(project_name, item)
    body = build_issue_body(item, project_name)
    target_state = STATUS_MAP.get(item.status, "open")

    labels = [SYNC_LABEL]
    if item.phase in PHASE_LABELS:
        labels.append(PHASE_LABELS[item.phase])
    if item.priority in PRIORITY_LABELS:
        labels.append(PRIORITY_LABELS[item.priority])

    label_args = []
    for l in labels:
        label_args.extend(["--label", l])

    if title in existing:
        issue = existing[title]
        issue_num = issue["number"]
        current_state = issue["state"].lower()

        # Update body and labels
        gh(["issue", "edit", str(issue_num), "--repo", repo,
            "--body", body] + label_args, check=False)

        # Update state if needed
        if target_state == "closed" and current_state == "open":
            gh(["issue", "close", str(issue_num), "--repo", repo])
            return f"closed #{issue_num}"
        elif target_state == "open" and current_state == "closed":
            gh(["issue", "reopen", str(issue_num), "--repo", repo])
            return f"reopened #{issue_num}"
        return f"updated #{issue_num}"
    else:
        # Create new issue
        state_args = ["--label", "closed"] if target_state == "closed" else []
        result = gh(["issue", "create", "--repo", repo,
                      "--title", title, "--body", body] + label_args)
        if target_state == "closed":
            # gh issue create can't create closed issues, so close it after
            issue_url = result.strip()
            issue_num = issue_url.rstrip("/").split("/")[-1]
            gh(["issue", "close", issue_num, "--repo", repo], check=False)
        return f"created {result.strip()}"


# ── Main ─────────────────────────────────────────────────────────────────────

def load_config() -> list[ProjectConfig]:
    """Load project configs from .sync-config.json."""
    with open(SYNC_CONFIG) as f:
        config = json.load(f)

    projects = []
    for p in config["projects"]:
        if "todo_file" not in p:
            continue
        projects.append(ProjectConfig(
            name=p["name"],
            repo=p["repo"],
            todo_file=p["todo_file"],
        ))
    return projects


def sync_project(project: ProjectConfig, dry_run: bool = False) -> None:
    """Sync TODOs from one project to GitHub Issues."""
    github_base = json.loads(SYNC_CONFIG.read_text())["github_base"]
    todo_path = Path(github_base) / project.name / project.todo_file

    if not todo_path.exists():
        print(f"  ⚠ TODO file not found: {todo_path}")
        return

    content = todo_path.read_text()
    items = parse_todo_file(content)

    if not items:
        print(f"  ⚠ No TODO items found in {todo_path}")
        return

    print(f"  Found {len(items)} TODO items")

    if dry_run:
        for item in items:
            state = STATUS_MAP.get(item.status, "open")
            print(f"    #{item.number} [{state}] ({item.phase}/{item.priority}) {item.description[:60]}")
        return

    ensure_labels(project.repo)
    existing = get_existing_issues(project.repo)

    created = updated = closed = 0
    for item in items:
        action = sync_item(project.repo, project.name, item, existing)
        if "created" in action:
            created += 1
        elif "closed" in action:
            closed += 1
        else:
            updated += 1
        print(f"    #{item.number}: {action}")

    print(f"  Summary: {created} created, {updated} updated, {closed} closed")


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    target = sys.argv[-1] if len(sys.argv) > 1 and not sys.argv[-1].startswith("-") else "all"

    if dry_run:
        print("══ DRY RUN — no changes will be made ══\n")
    else:
        print("══ Syncing TODOs → GitHub Issues ══\n")

    projects = load_config()

    if not projects:
        print("No projects with todo_file configured in .sync-config.json")
        print("Add 'todo_file' to each project entry, e.g.:")
        print('  "todo_file": "docs/TODO.md"')
        sys.exit(1)

    for project in projects:
        if target != "all" and project.name != target:
            continue
        print(f"── {project.name} ({project.repo}) ──")
        sync_project(project, dry_run=dry_run)
        print()

    print("══ Done ══")


if __name__ == "__main__":
    main()
