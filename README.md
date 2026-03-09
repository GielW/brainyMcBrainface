# brainyMcBrain

Central repository for all my `claude.md` / `CLAUDE.md` project instruction files, with two-way sync.

## Tracked Projects

| Project | Source Location |
|---------|---------------|
| 40Jarigen | `/mnt/64AA9536AA950628/GitHub/40Jarigen/claude.md` |
| DPO-Dashboard | `/mnt/64AA9536AA950628/GitHub/DPO-Dashboard/CLAUDE.md` |
| ilumenTool | `/mnt/64AA9536AA950628/GitHub/ilumenTool/claude.md` |

## Usage

```bash
# Check sync status
./sync.sh status

# Pull latest from all project repos into this repo
./sync.sh pull

# Push changes from this repo back to project repos
./sync.sh push

# Scan PC for new, untracked claude.md files
./sync.sh discover

# Add a new project manually
./sync.sh add myProject /path/to/myProject/CLAUDE.md

# Auto-sync: pull + commit + push to GitHub (for cron)
./sync.sh auto
```

## Automated Sync (optional)

Add a cron job to auto-sync every hour:

```bash
crontab -e
# Add this line:
0 * * * * /mnt/64AA9536AA950628/GitHub/brainyMcBrain/sync.sh auto >> /tmp/brainyMcBrain-sync.log 2>&1
```

## Structure

```
brainyMcBrain/
├── README.md
├── sync.sh                  # Sync script
├── .sync-config.json        # Project → path mappings
└── projects/
    ├── 40Jarigen/claude.md
    ├── DPO-Dashboard/CLAUDE.md
    └── ilumenTool/claude.md
```
