# Project Tracking

## TODO Management

- All task tracking lives in **dedicated files** (e.g., `docs/TODO.md`, `meta/session-progress.md`)
- **Never add `// TODO` comments in source code** — they get lost
- Use consistent table format:

```markdown
| # | Phase | Status | Priority | Description |
| --- | --- | --- | --- | --- |
| 1 | P1 | Open | High | Short, clear description |
```

### Status Values

`Open` → `In Progress` → `Done`

### Priority Values

`High` | `Medium` | `Low`

### Phase Convention

- `P0` — Security / critical
- `P1` — Core features / cleanup
- `P2` — Architecture / refactoring
- `P3` — Decomposition / restructuring
- `P4` — Testing / logging / CI / documentation
- `PX` — Extras (independent of core phases)

## Session Tracking

When working in sessions (e.g., with Claude Code):
- Track progress in a session log file
- Add numbered entries under the date section
- Update "Up Next" / "Current Phase" sections to reflect state
- Mark TODOs as done in their **source files** when completed (don't just log it)

## After Every Change — Checklist Pattern

Every project should define its "linked files" that must be updated together. The universal pattern:

### On Every Commit

- [ ] **TODO/Progress file** — Update task status
- [ ] **CHANGELOG** — Add entry under `[Unreleased]`
- [ ] **Commit message** — Follows conventional commits

### On Version Bump

- [ ] Project config file (e.g., `pyproject.toml`, `pubspec.yaml`) — update version
- [ ] CHANGELOG — Move `[Unreleased]` to new version heading
- [ ] CLAUDE.md — Update version reference

### On New Feature/Module

- [ ] Requirements/specs docs — add/update spec
- [ ] Progress tracking — add to module table
- [ ] README — update features and structure
- [ ] CLAUDE.md — update module reference

## Roadmap Format

Track project phases in a table:

```markdown
| Phase | Status | Focus |
| ----- | ------ | ----- |
| Phase 0 | ✅ Done | Description |
| Phase 1 | 🟡 In Progress | Description |
| Phase 2 | Not started | Description |
```
