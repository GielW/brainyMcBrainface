# CLAUDE.md — Giel's Brain

> Master instruction file. Referenced skills, languages, domains, and projects are loaded automatically via `@`-imports.

---

## Identity

@skills/identity.md

## Universal Skills (apply to ALL projects)

@skills/git-workflow.md
@skills/documentation.md
@skills/project-tracking.md
@skills/code-quality.md
@skills/ci-cd.md
@skills/security.md
@skills/testing.md

## Language Skills (activated per project)

@languages/python.md
@languages/dart-flutter.md
@languages/web-pwa.md

## Domain Skills (activated when relevant)

@domains/obsidian-vault.md
@domains/belgian-legal.md
@domains/iot-hardware.md
@domains/event-planning.md

## Active Projects

@projects/40Jarigen.md
@projects/DPO-Dashboard.md
@projects/ilumenTool.md

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
| Test conventions, coverage, test plans | `skills/testing.md` |
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
| _(empty — add new entries here)_ | | | |

---

## Meta Rules

1. **DRY principle** — If the same instruction appears in 2+ project files, extract it into a shared skill
2. **Project files stay slim** — Only truly unique, project-specific context belongs in `projects/*.md`
3. **Skills are universal** — They apply regardless of which project is active
4. **Languages activate per project** — Only the relevant language module applies
5. **Domains activate per context** — Belgian legal doesn't apply to a hardware-only session
6. **Inbox is temporary** — Items should be promoted within the same session or the next
7. **Sync back** — When a shared skill is updated, the `sync.sh push` propagates changes. Project-specific changes go back via `sync.sh push` to the original repos
