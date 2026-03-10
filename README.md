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
│   ├── wat-framework.md             ← Workflows-Agents-Tools architecture
│   ├── web-design.md                ← Frontend craft, anti-generic guardrails
│   ├── security.md                  ← Credentials, secrets, scanning, encryption
│   ├── testing.md                   ← Test conventions, coverage, test plans
│   └── council-of-masters.md        ← Multi-expert deliberation for complex decisions
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
├── compiled/                        ← Auto-generated standalone claude.md per project
│   ├── 40Jarigen/claude.md
│   ├── DPO-Dashboard/CLAUDE.md
│   └── ilumenTool/claude.md
├── projects-archive/                ← Original full claude.md files (reference)
│   ├── 40Jarigen/claude.md
│   ├── DPO-Dashboard/CLAUDE.md
│   └── ilumenTool/claude.md
├── tools/                           ← Automation scripts
│   ├── compile-brain.py             ← Assembles modular brain → project claude.md
│   ├── validate-brain.py            ← Lints brain for consistency (CI + local)
│   ├── init-project.py              ← Scaffold a new project (one command)
│   └── todo-to-issues.py            ← Syncs TODO tables → GitHub Issues
├── skills-external/                 ← External skill repos (git submodules)
│   └── anthropic/                   ← github.com/anthropics/skills
│       └── skills/                  ← 17 community skills (auto-updated)
├── .github/workflows/               ← GitHub Actions
│   ├── validate.yml                 ← Lint brain on push (auto)
│   ├── sync-to-projects.yml         ← Compile + push claude.md to repos (auto + manual)
│   ├── triage-brain-updates.yml     ← Auto-label incoming brain-update issues
│   └── todo-to-issues.yml           ← Sync TODOs to GitHub Issues (manual)
├── .github/ISSUE_TEMPLATE/          ← Issue templates
│   └── brain-update.yml             ← Structured brain feedback template
├── sync.sh                          ← Local sync (pull/push/status/discover)
├── .sync-config.json                ← Project → path mappings
└── README.md
```

## Tracked Projects

| Project | Languages | Domains | Source |
|---------|-----------|---------|--------|
| 40Jarigen | web-pwa | event-planning, obsidian-vault, iot-hardware | `GielW/40Jarigen` |
| DPO-Dashboard | python | obsidian-vault, belgian-legal | `GielW/DPO-Dashboard` |
| ilumenTool | dart-flutter | iot-hardware | `RdFutech/ilumenTool` |

## How Knowledge Flows

brainyMcBrain is the **source of truth**. The workflow:

1. You're working in a project (e.g., ilumenTool)
2. You establish a new convention or fix a recurring pattern
3. **Claude flags it**: _"This looks like reusable knowledge. It should be added to brainyMcBrain."_
4. Switch to brainyMcBrain → add to the **Inbox** in `CLAUDE.md`
5. Categorise it (use the Category Quick Reference table)
6. Promote it to the correct skill/language/domain file
7. Delete from inbox

This replaces the old approach of syncing monolithic claude.md files back and forth.

## Brain Compiler

The compiler assembles the modular brain into **project-specific standalone claude.md files**. Each compiled file includes only the skills, languages, and domains that project needs — all inlined into one self-contained file.

```bash
python3 tools/compile-brain.py all              # Compile all projects → compiled/
python3 tools/compile-brain.py ilumenTool       # Compile one project
python3 tools/compile-brain.py all --dry-run    # Preview without writing
```

Output goes to `compiled/<project>/<claude.md>`. These compiled files are what gets pushed to project repos via the sync workflow.

## Brain Linter

Validates internal consistency — catches broken imports, orphan files, missing frontmatter, and config drift.

```bash
python3 tools/validate-brain.py                 # Run all checks
```

Runs automatically on every push to `main` via the **Validate Brain** GitHub Action.

## Project Scaffold

Registers a new project in one command — creates the project file, updates config, adds CLAUDE.md import, and updates workflow dropdowns.

```bash
python3 tools/init-project.py MyProject --repo GielW/MyProject \
  --languages python --domains belgian-legal \
  --external pdf docx --compile
```

The script is idempotent — re-running it skips anything already in place.

## Archive Sync (backup role)

The `sync.sh` script serves a **backup/reference** role — it snapshots the original project claude.md files into `projects-archive/`.

```bash
./sync.sh status           # Check if project originals have drifted from archive
./sync.sh pull             # Snapshot latest originals into archive
./sync.sh push             # Restore archive copies back to project repos (rare)
./sync.sh discover         # Scan PC for new repos with claude.md files
./sync.sh add <name> <path>  # Track a new project's original file
./sync.sh update-external  # Update external skill repos (submodules)
./sync.sh auto             # Pull + update externals + commit + push (cron daily)
```

### GitHub Action — Sync claude.md to Projects

Compiles the brain and pushes the result to project repos. Runs in two modes:

- **Automatic:** Triggers after the **Validate Brain** workflow succeeds on `main`. When you push changes to skills, languages, domains, projects, or CLAUDE.md, the brain is validated first — if validation passes, all project repos receive updated compiled files automatically.
- **Manual:** Go to **Actions → Sync claude.md to projects**, click **Run workflow**, and pick a specific project or `all`.

**Setup:** Add a Personal Access Token as `BRAIN_SYNC_PAT` in this repo's secrets. The token needs `repo` scope (or fine-grained: Contents read/write) for the target repos.

### GitHub Action — Validate Brain

Runs automatically on every push to `main` that touches skill, language, domain, project files, or CLAUDE.md. Also runs on pull requests.

### GitHub Action — Triage Brain Updates

Auto-labels incoming `brain-update` issues when they're created via the feedback loop. Parses the issue body to extract target file, category, and source project, then applies corresponding labels (`scope:skills`, `type:convention`, `from:ilumenTool`, etc.).

### GitHub Action — Sync TODOs to GitHub Issues

A manual Action that parses TODO/progress markdown files from each project and creates/updates/closes GitHub Issues to match.

1. Go to **Actions → Sync TODOs to GitHub Issues**
2. Click **Run workflow**
3. Pick a project or `all`, and optionally enable **Dry run** to preview
4. The action creates issues with labels (`phase:P1-core`, `priority:high`, `synced-from-todo`) and closes issues whose TODO status is "Done"

**Supported formats:**
- ilumenTool-style: `| # | Phase | Status | Priority | Description |`
- DPO-Dashboard-style: `| Task | ✅ Done / ⬜ Not started | Date |`

The parser script lives at `tools/todo-to-issues.py` and can also be run locally:
```bash
python3 tools/todo-to-issues.py --dry-run          # Preview all projects
python3 tools/todo-to-issues.py ilumenTool          # Sync one project
python3 tools/todo-to-issues.py all                 # Sync all projects
```

**Setup:** Same `BRAIN_SYNC_PAT` secret — needs `repo` scope + Issues write permission.

## External Skills

The [anthropics/skills](https://github.com/anthropics/skills) repo is tracked as a git submodule in `skills-external/anthropic/`. It's updated automatically during the daily cron sync.

To update manually:
```bash
./sync.sh update-external
```

To use an external skill in a project, reference it via:
```
@skills-external/anthropic/skills/<skill-name>/SKILL.md
```

Available skills: algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx

## Adding a New Project

Use the scaffold script:

```bash
python3 tools/init-project.py ProjectName --repo GielW/ProjectName \
  --languages python --domains belgian-legal \
  --external pdf docx --compile
```

This handles everything: project file, config, CLAUDE.md import, and workflow dropdowns. See [Project Scaffold](#project-scaffold) for details.

For archive tracking, also run:
```bash
./sync.sh add ProjectName /path/to/ProjectName/claude.md
```
