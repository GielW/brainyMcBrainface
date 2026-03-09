# brainyMcBrain

Central repository for Giel's `CLAUDE.md` brain — a modular instruction system for AI assistants across all projects, hobbies, and tasks.

## How It Works

One master `CLAUDE.md` references **skills** (universal rules), **languages** (per-language conventions), **domains** (subject-matter expertise), and **projects** (project-specific context). Claude Code loads all referenced files automatically via `@`-imports.

New knowledge gets added to the **Inbox** in `CLAUDE.md`, categorised, then promoted to the correct module.

## Structure

```
brainyMcBrain/
├── CLAUDE.md                        ← Master file (identity + router + inbox)
├── skills/                          ← Universal rules (apply to ALL projects)
│   ├── identity.md                  ← Who is Giel, Belgium, languages, tools
│   ├── git-workflow.md              ← Conventional commits, branching, PRs
│   ├── documentation.md             ← Markdown style, YAML frontmatter, links
│   ├── project-tracking.md          ← TODOs, session logs, phases, checklists
│   ├── code-quality.md              ← Lint/format/analyze rules, naming, imports
│   ├── ci-cd.md                     ← GitHub Actions, pipelines, releases, SBOM
│   ├── security.md                  ← Credentials, secrets, scanning, encryption
│   └── testing.md                   ← Test conventions, coverage, test plans
├── languages/                       ← Language-specific skills (per project)
│   ├── python.md                    ← Ruff, black, mypy, pytest, FastAPI
│   ├── dart-flutter.md              ← Flutter analyze, package imports, platforms
│   └── web-pwa.md                   ← ESLint, Prettier, PWA patterns
├── domains/                         ← Subject-matter expertise (when relevant)
│   ├── obsidian-vault.md            ← MOCs, graph colours, tags, templates
│   ├── belgian-legal.md             ← GDPR, GBA/APD, NIS2, retention periods
│   ├── iot-hardware.md              ← ESP32, AVR, MQTT, serial, production
│   └── event-planning.md            ← Logistics, venue, budget, cross-linking
├── projects/                        ← Project-specific context (slim files)
│   ├── 40Jarigen.md                 ← Immersive party — chess pieces, puzzles
│   ├── DPO-Dashboard.md             ← GDPR compliance dashboard — 15 modules
│   └── ilumenTool.md                ← IoT production tool — Flutter, Firebase
├── projects-archive/                ← Original full claude.md files (reference)
│   ├── 40Jarigen/claude.md
│   ├── DPO-Dashboard/CLAUDE.md
│   └── ilumenTool/claude.md
├── sync.sh                          ← Sync script (pull/push/status/discover)
├── .sync-config.json                ← Project → path mappings
└── README.md
```

## Tracked Projects

| Project | Languages | Domains | Source |
|---------|-----------|---------|--------|
| 40Jarigen | web-pwa | event-planning, obsidian-vault, iot-hardware | `GielW/40Jarigen` |
| DPO-Dashboard | python | obsidian-vault, belgian-legal | `GielW/DPO-Dashboard` |
| ilumenTool | dart-flutter | iot-hardware | `RdFutech/ilumenTool` |

## Sync Commands

```bash
./sync.sh status     # Show sync status for each tracked project
./sync.sh pull       # Pull claude.md files from project repos → archive
./sync.sh push       # Push claude.md files from archive → project repos
./sync.sh discover   # Scan PC for new, untracked claude.md files
./sync.sh add <name> <path>  # Add a new project to track
./sync.sh auto       # Pull + commit + push to GitHub (cron job runs hourly)
```

## Adding New Knowledge

1. During a project session, you discover a reusable pattern
2. Add it to the **Inbox** table in `CLAUDE.md` with the source project
3. Pick the target file from the **Category Quick Reference** table
4. Move the content to the target file
5. Delete from inbox

## Adding a New Project

1. `./sync.sh add ProjectName /path/to/ProjectName/CLAUDE.md` — tracks the original file
2. Create `projects/ProjectName.md` — slim project-specific context (reference the skills/languages/domains it uses)
3. Update this README
