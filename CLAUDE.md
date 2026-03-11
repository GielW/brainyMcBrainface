# CLAUDE.md — Giel's Brain

> Master instruction file. Referenced skills, languages, domains, and projects are loaded automatically via `@`-imports.

---

## ⚠️ Brain Update Rule — READ THIS FIRST

**This file is the source of truth for all projects.** When working in ANY project session (brainyMcBrain or any other repo), follow this rule:

> **Whenever you learn something new, establish a convention, fix a pattern, or make a decision that could apply beyond the current project — tell the user:**
>
> _"This looks like reusable knowledge. It should be added to the brainyMcBrain repository. I'll note it for the inbox."_

Then:
1. **If currently in brainyMcBrain**: Add it directly to the Inbox table below, or promote it straight to the correct skill/domain/language file
2. **If in another repo (compiled claude.md)**: Use the Brain Feedback Loop section at the bottom of the compiled file — ask the user, then `gh issue create` on brainyMcBrain with structured data
3. **Fallback**: If `gh` is not available, remind the user to switch to brainyMcBrain and add it manually. Provide the exact text and target file

### What Triggers a Brain Update

| Trigger | Example |
|---------|---------|
| New convention established | "We decided to use X pattern for all services" |
| Recurring mistake fixed | "This is the third time — let's document the rule" |
| Tool/workflow discovered | "This CLI flag saves time — add to skills" |
| Legal/regulatory reference | "New GBA guideline — add to belgian-legal.md" |
| Cross-project pattern | "Both projects do this — extract to shared skill" |
| Project-specific decision | "ilumenTool will use Riverpod — update projects/ilumenTool.md" |

### What Does NOT Trigger a Brain Update

- One-off debugging steps
- Temporary workarounds
- Project-specific data (serial numbers, API keys, etc.)
- Information already covered by existing skill files

---

## Identity

@skills/identity.md

## Universal Skills (apply to ALL projects)

@skills/git-workflow.md
@skills/documentation.md
@skills/project-tracking.md
@skills/code-quality.md
@skills/ci-cd.md
@skills/wat-framework.md
@skills/web-design.md
@skills/security.md
@skills/testing.md
@skills/council-of-masters.md

## Language Skills (activated per project)

@languages/python.md
@languages/dart-flutter.md
@languages/web-pwa.md

## Domain Skills (activated when relevant)

@domains/obsidian-vault.md
@domains/belgian-legal.md
@domains/iot-hardware.md
@domains/event-planning.md

## External Skills (from Anthropic)

Community skills from [anthropics/skills](https://github.com/anthropics/skills) live in `skills-external/anthropic/skills/`. Use them via `@skills-external/anthropic/skills/<name>/SKILL.md` when relevant.

Available: algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx

## Active Projects

@projects/40Jarigen.md
@projects/DPO-Dashboard.md
@projects/ilumenTool.md
@projects/peccatum-mortale.md

---

## Inbox — New Knowledge Router

When you learn something new during any project session that could be reusable, **add it here first**. Periodically, items get promoted to the correct skill/domain/language file.

### How to Route

1. **You encounter a new pattern, rule, or convention** during a project session
2. **Add it to the inbox below** with the source project tag
3. **Categorise it** using the target column
4. **Promote it** — move the content to the target file and delete from inbox

### Category Quick Reference

| If the knowledge is about... | Route to |
|------------------------------|----------|
| Who I am, location, tools, preferences | `skills/identity.md` |
| Git commits, branches, PRs | `skills/git-workflow.md` |
| Markdown, frontmatter, Obsidian links | `skills/documentation.md` |
| TODOs, session logs, checklists, phases | `skills/project-tracking.md` |
| Linting, formatting, analyzer hygiene | `skills/code-quality.md` |
| GitHub Actions, CI pipelines, SBOM | `skills/ci-cd.md` |
| Credentials, secrets, encryption | `skills/security.md` |
| WAT architecture, workflows, tools-first | `skills/wat-framework.md` |
| Frontend design, anti-generic guardrails, screenshot QA | `skills/web-design.md` |
| Test conventions, coverage, test plans | `skills/testing.md` |
| Multi-expert deliberation, complex decisions | `skills/council-of-masters.md` |
| Python-specific style / tools | `languages/python.md` |
| Dart/Flutter-specific style / tools | `languages/dart-flutter.md` |
| JS/TS/PWA-specific style / tools | `languages/web-pwa.md` |
| Obsidian vault structure, MOCs, tags | `domains/obsidian-vault.md` |
| GDPR, GBA/APD, Belgian law, NIS2 | `domains/belgian-legal.md` |
| ESP32, AVR, MQTT, serial, hardware | `domains/iot-hardware.md` |
| Event logistics, venue, budget, guests | `domains/event-planning.md` |
| Only relevant to one project | `projects/<name>.md` |
| Doesn't fit anywhere | Create new skill/domain file |

### Pending Items

<!-- Add new items here. Format: | source | description | target file | -->

| Source Project | New Knowledge | Target File | Status |
|---------------|---------------|-------------|--------|
| brainyMcBrain | ECC continuous-learning-v2 instinct model (atomic behaviors + confidence scoring + project scoping + evolution to skills) — consider adapting for brainyMcBrain's own brain update loop | `skills/project-tracking.md` | ✅ Promoted |
| brainyMcBrain | ECC parallelization patterns (git worktrees, cascade method, fork for research vs code) — useful for multi-session workflows | `skills/wat-framework.md` | ✅ Promoted |
| brainyMcBrain | ECC memory persistence hooks (PreCompact save state, Stop hook persist learnings, SessionStart load context) — session lifecycle automation | `skills/project-tracking.md` | ✅ Promoted |

---

## Meta Rules

1. **DRY principle** — If the same instruction appears in 2+ project files, extract it into a shared skill
2. **Project files stay slim** — Only truly unique, project-specific context belongs in `projects/*.md`
3. **Skills are universal** — They apply regardless of which project is active
4. **Languages activate per project** — Only the relevant language module applies
5. **Domains activate per context** — Belgian legal doesn't apply to a hardware-only session
6. **Inbox is temporary** — Items should be promoted within the same session or the next
7. **brainyMcBrain is the source of truth** — All shared knowledge lives here. Individual project repos keep their own claude.md for standalone use, but brainyMcBrain is canonical
8. **Always flag brain updates** — When reusable knowledge emerges in any session, notify the user (see Brain Update Rule above)

## Sync — Archive & Backup

The `sync.sh` script keeps a backup of the original project claude.md files in `projects-archive/`. This is a **reference/backup** role, not the source of truth.

- **`sync.sh pull`** — Snapshot the latest original claude.md files from each project repo into the archive
- **`sync.sh push`** — Push archive copies back to project repos (use sparingly — only when the original needs restoring)
- **`sync.sh status`** — Check if originals have drifted from archive
- **`sync.sh discover`** — Find new repos with claude.md files not yet tracked
- **Auto-sync (cron)** — Runs daily at midnight to keep archive fresh
