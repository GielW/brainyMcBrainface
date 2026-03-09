#!/usr/bin/env bash
# ============================================================================
# brainyMcBrain sync — two-way sync for claude.md files
# ============================================================================
#
# Usage:
#   ./sync.sh pull          Pull from project repos → this repo
#   ./sync.sh push          Push from this repo → project repos
#   ./sync.sh status        Show diff status for each project
#   ./sync.sh discover      Scan for new claude.md files not yet tracked
#   ./sync.sh auto          Pull → commit → push to GitHub (for cron)
#
# Config: .sync-config.json (maps project names to source paths)
# ============================================================================

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$SCRIPT_DIR/.sync-config.json"
PROJECTS_DIR="$SCRIPT_DIR/projects"

# Colours
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Colour

# ── Helpers ──────────────────────────────────────────────────────────────────

check_deps() {
    for cmd in jq; do
        if ! command -v "$cmd" &>/dev/null; then
            echo -e "${RED}Error: '$cmd' is required but not installed.${NC}"
            echo "Install with: sudo apt install $cmd"
            exit 1
        fi
    done
}

get_projects() {
    jq -c '.projects[]' "$CONFIG"
}

get_project_count() {
    jq '.projects | length' "$CONFIG"
}

# ── Commands ─────────────────────────────────────────────────────────────────

cmd_pull() {
    echo -e "${BLUE}══ Pulling claude.md files from project repos ══${NC}"
    local updated=0 skipped=0 missing=0

    while IFS= read -r project; do
        local name source repo_path
        name=$(echo "$project" | jq -r '.name')
        source=$(echo "$project" | jq -r '.source')
        repo_path=$(echo "$project" | jq -r '.repo_path')
        local dest="$SCRIPT_DIR/$repo_path"

        if [[ ! -f "$source" ]]; then
            echo -e "  ${RED}✗ $name${NC} — source not found: $source"
            ((missing++))
            continue
        fi

        # Create directory if needed
        mkdir -p "$(dirname "$dest")"

        if [[ ! -f "$dest" ]] || ! diff -q "$source" "$dest" &>/dev/null; then
            cp "$source" "$dest"
            echo -e "  ${GREEN}✓ $name${NC} — updated"
            ((updated++))
        else
            echo -e "  ${YELLOW}· $name${NC} — already up to date"
            ((skipped++))
        fi
    done < <(get_projects)

    echo -e "\n${BLUE}Summary:${NC} $updated updated, $skipped unchanged, $missing missing"
}

cmd_push() {
    echo -e "${BLUE}══ Pushing claude.md files to project repos ══${NC}"
    local updated=0 skipped=0 missing=0

    while IFS= read -r project; do
        local name source repo_path
        name=$(echo "$project" | jq -r '.name')
        source=$(echo "$project" | jq -r '.source')
        repo_path=$(echo "$project" | jq -r '.repo_path')
        local src="$SCRIPT_DIR/$repo_path"

        if [[ ! -f "$src" ]]; then
            echo -e "  ${RED}✗ $name${NC} — repo copy not found: $repo_path"
            ((missing++))
            continue
        fi

        if [[ ! -d "$(dirname "$source")" ]]; then
            echo -e "  ${RED}✗ $name${NC} — target project dir not found: $(dirname "$source")"
            ((missing++))
            continue
        fi

        if ! diff -q "$src" "$source" &>/dev/null; then
            cp "$src" "$source"
            echo -e "  ${GREEN}✓ $name${NC} — pushed"
            ((updated++))
        else
            echo -e "  ${YELLOW}· $name${NC} — already in sync"
            ((skipped++))
        fi
    done < <(get_projects)

    echo -e "\n${BLUE}Summary:${NC} $updated pushed, $skipped unchanged, $missing missing"
}

cmd_status() {
    echo -e "${BLUE}══ Sync Status ══${NC}"
    echo ""

    while IFS= read -r project; do
        local name source repo_path
        name=$(echo "$project" | jq -r '.name')
        source=$(echo "$project" | jq -r '.source')
        repo_path=$(echo "$project" | jq -r '.repo_path')
        local dest="$SCRIPT_DIR/$repo_path"

        printf "  %-20s" "$name"

        if [[ ! -f "$source" ]]; then
            echo -e "${RED}source missing${NC}"
            continue
        fi

        if [[ ! -f "$dest" ]]; then
            echo -e "${RED}repo copy missing${NC}"
            continue
        fi

        if diff -q "$source" "$dest" &>/dev/null; then
            local mod_date
            mod_date=$(date -r "$source" '+%Y-%m-%d %H:%M')
            echo -e "${GREEN}✓ in sync${NC}  (last modified: $mod_date)"
        else
            local src_date dst_date
            src_date=$(stat -c %Y "$source" 2>/dev/null || stat -f %m "$source")
            dst_date=$(stat -c %Y "$dest" 2>/dev/null || stat -f %m "$dest")

            if [[ "$src_date" -gt "$dst_date" ]]; then
                echo -e "${YELLOW}⟵ source is newer${NC} — run 'pull' to update"
            else
                echo -e "${YELLOW}⟶ repo is newer${NC} — run 'push' to update"
            fi
        fi
    done < <(get_projects)

    echo ""
}

cmd_discover() {
    echo -e "${BLUE}══ Scanning for new claude.md files ══${NC}"

    local github_base
    github_base=$(jq -r '.github_base' "$CONFIG")

    # Get already-tracked source paths
    local tracked_sources
    tracked_sources=$(jq -r '.projects[].source' "$CONFIG")

    local found=0 new=0

    while IFS= read -r file; do
        ((found++))

        # Skip third-party locations and this repo's own copies
        if [[ "$file" == *"linuxbrew"* ]] || [[ "$file" == *".vscode/extensions"* ]] || [[ "$file" == *"brainyMcBrain/projects/"* ]]; then
            continue
        fi

        # Skip if already tracked
        if echo "$tracked_sources" | grep -qF "$file"; then
            continue
        fi

        ((new++))

        # Try to extract project name from path
        local project_name
        project_name=$(echo "$file" | sed -E "s|.*/GitHub/([^/]+)/.*|\1|")
        local filename
        filename=$(basename "$file")

        echo -e "  ${GREEN}NEW${NC} $file"
        echo -e "       → Add to config: name=$project_name, repo_path=projects/$project_name/$filename"
    done < <(find /mnt /home -iname "claude.md" -o -iname ".claude.md" 2>/dev/null)

    if [[ $new -eq 0 ]]; then
        echo -e "  ${YELLOW}No new claude.md files found.${NC} ($found total scanned, all tracked or third-party)"
    else
        echo -e "\n  Found $new new file(s). Add them to .sync-config.json and run 'pull'."
    fi
}

cmd_auto() {
    echo -e "${BLUE}══ Auto-sync: pull → commit → push to GitHub ══${NC}"

    # Pull latest from project repos
    cmd_pull

    cd "$SCRIPT_DIR"

    # Check if there are changes to commit
    if git diff --quiet && git diff --cached --quiet; then
        echo -e "\n${YELLOW}No changes to commit.${NC}"
        return 0
    fi

    # Stage, commit, push
    git add -A
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M')
    git commit -m "sync: auto-sync claude.md files ($timestamp)"
    git push origin main

    echo -e "\n${GREEN}✓ Changes committed and pushed to GitHub.${NC}"
}

cmd_add() {
    if [[ $# -lt 2 ]]; then
        echo "Usage: ./sync.sh add <project-name> <path-to-claude.md>"
        echo "Example: ./sync.sh add myProject /mnt/64AA9536AA950628/GitHub/myProject/CLAUDE.md"
        exit 1
    fi

    local name="$1"
    local source="$2"
    local filename
    filename=$(basename "$source")
    local repo_path="projects/$name/$filename"

    if [[ ! -f "$source" ]]; then
        echo -e "${RED}Error: File not found: $source${NC}"
        exit 1
    fi

    # Check if already tracked
    if jq -r '.projects[].name' "$CONFIG" | grep -qx "$name"; then
        echo -e "${YELLOW}Project '$name' is already tracked.${NC}"
        exit 1
    fi

    # Add to config
    local tmp
    tmp=$(mktemp)
    jq --arg name "$name" --arg source "$source" --arg repo_path "$repo_path" \
        '.projects += [{"name": $name, "source": $source, "repo_path": $repo_path}]' \
        "$CONFIG" > "$tmp" && mv "$tmp" "$CONFIG"

    # Copy file
    mkdir -p "$SCRIPT_DIR/projects/$name"
    cp "$source" "$SCRIPT_DIR/$repo_path"

    echo -e "${GREEN}✓ Added '$name' → $repo_path${NC}"
    echo "  Source: $source"
}

# ── Main ─────────────────────────────────────────────────────────────────────

check_deps

case "${1:-help}" in
    pull)     cmd_pull ;;
    push)     cmd_push ;;
    status)   cmd_status ;;
    discover) cmd_discover ;;
    auto)     cmd_auto ;;
    add)      shift; cmd_add "$@" ;;
    help|*)
        echo "brainyMcBrain — claude.md sync manager"
        echo ""
        echo "Usage: ./sync.sh <command>"
        echo ""
        echo "Commands:"
        echo "  pull       Pull claude.md files from project repos into this repo"
        echo "  push       Push claude.md files from this repo back to project repos"
        echo "  status     Show sync status for each tracked project"
        echo "  discover   Scan PC for new, untracked claude.md files"
        echo "  add <name> <path>  Add a new project to track"
        echo "  auto       Pull + commit + push to GitHub (for cron jobs)"
        echo "  help       Show this help"
        ;;
esac
