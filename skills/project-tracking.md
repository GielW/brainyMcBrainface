---
name: project-tracking
description: TODO management, session tracking, planning discipline, verification checklists, and the self-improvement loop. Use whenever creating tasks, updating progress, planning work, checking off linked files, or syncing TODOs to GitHub Issues.
---

# Project Tracking

## Planning Discipline

- **Plan before building** — Enter plan mode for any non-trivial task (3+ steps or architectural decisions)
- Write a brief spec or checklist before you start coding
- If something goes sideways mid-task, **STOP and re-plan** — don't keep pushing a broken approach
- Use planning for verification steps too, not just building

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

### Session Lifecycle Discipline

> Source: Memory persistence hooks from [everything-claude-code](https://github.com/affaan-m/everything-claude-code).

Every session has three critical moments. Handle them deliberately:

#### Session Start — Load Context

Before diving into work:

1. Read the project's `tasks/lessons.md` (or equivalent) for previous learnings
2. Check the TODO/progress file for current state and "Up Next" items
3. Review any session handoff notes from the previous session (see Session End below)
4. Orient yourself: what branch are we on, what's the current phase, what was last done?

#### Before Compaction / Context Reset — Save State

When context is running low or before a manual `/compact`:

1. Summarise current progress in the session log — what's done, what's in progress, what's blocked
2. Note any partial state that would be lost: variable names, file paths being worked on, half-finished approach
3. Write "Up Next" steps clearly enough that a fresh context can pick up without re-exploration

#### Session End — Persist Learnings

Before closing a session:

1. **Capture what worked** — successful approaches, useful commands, effective patterns
2. **Capture what failed** — dead ends, wrong assumptions, wasted effort (so the next session doesn't repeat them)
3. **Capture what's left** — unfinished tasks, open questions, blockers
4. Write this to the project's session log or handoff file
5. Check if any learnings qualify as patterns for the Self-Improvement Loop (see below)

#### Handoff File Format

For complex multi-session work, use a structured handoff:

```markdown
## Session Handoff — [date]

### Completed
- [what got done]

### In Progress
- [what's partially done + current state]

### Not Attempted
- [what's left to do]

### Learnings
- [what worked, what didn't, gotchas discovered]

### Resume From
- Branch: `feat/...`
- File: `src/...` line ~N
- Next step: [specific action]
```

## After Every Change — Checklist Pattern

Every project should define its "linked files" that must be updated together. The universal pattern:

### On Every Commit

- [ ] **TODO/Progress file** — Update task status
- [ ] **CHANGELOG** — Add entry under `[Unreleased]`
- [ ] **Commit message** — Follows conventional commits
- [ ] **GitHub Issues sync** — If TODO items changed, run the TODO-to-Issues sync (see below)

### On Version Bump

- [ ] Project config file (e.g., `pyproject.toml`, `pubspec.yaml`) — update version
- [ ] CHANGELOG — Move `[Unreleased]` to new version heading
- [ ] CLAUDE.md — Update version reference

### On New Feature/Module

- [ ] Requirements/specs docs — add/update spec
- [ ] Progress tracking — add to module table
- [ ] README — update features and structure
- [ ] CLAUDE.md — update module reference

## Verification Before Done

- **Never mark a task complete without proving it works** — run tests, check logs, demonstrate correctness
- Diff behaviour between `main` and your changes when relevant
- Ask yourself: "Would a senior engineer approve this?"
- For CI-visible work, verify the pipeline is green before moving on

### Verification Loop Patterns

> Source: [everything-claude-code](https://github.com/affaan-m/everything-claude-code) eval-harness and verification-loop skills.

- **Checkpoint-based evals**: Set explicit checkpoints at milestones, verify against defined criteria, fix before proceeding
- **Continuous evals**: Full test suite + lint after major changes or at regular intervals
- Use `pass@k` (at least one of k attempts succeeds) when you just need it to work
- Use `pass^k` (ALL k must succeed) when consistency is essential

### Strategic Compaction

When to `/compact` or reset context:

- After research/exploration, **before** implementation
- After completing a milestone, **before** the next
- After debugging, **before** feature work
- After a failed approach, **before** trying a new one

When **NOT** to compact:

- Mid-implementation — you'll lose variable names, file paths, partial state

## Self-Improvement Loop

- After **any correction** from the user, capture the pattern in the project's `tasks/lessons.md` (or equivalent)
- Write rules for yourself that prevent the same mistake recurring
- Review lessons at the start of each session for the active project
- If the lesson is cross-project, route it to the brainyMcBrain Inbox (see Brain Update Rule)

### Pattern Maturity Model

> Source: Adapted from the instinct-based learning model in [everything-claude-code](https://github.com/affaan-m/everything-claude-code) continuous-learning-v2.

Not every observation deserves to become a skill immediately. Patterns should mature through stages:

#### Stages

| Stage | Maturity | Action |
| --- | --- | --- |
| **Observation** | Single occurrence | Note in project's `tasks/lessons.md` — don't promote yet |
| **Pattern** | 2–3 occurrences across sessions or projects | Add to brainyMcBrain Inbox with evidence |
| **Convention** | Repeated, proven, never contradicted | Promote to the correct skill/domain/language file |

#### Confidence Signals

A pattern is ready for promotion when:

- It has been observed in **2+ projects** or **3+ sessions** in the same project
- The user has **never corrected** the behaviour (or corrections reinforced it)
- It's **not contradicted** by existing skills

A pattern should stay local (project-only) when:

- It only applies to one framework, stack, or repo structure
- It depends on project-specific conventions (file layout, naming, tooling)

A pattern should be **demoted or removed** when:

- The user explicitly corrects it
- It hasn't been relevant for an extended period
- New evidence contradicts it

#### Scoping: Project vs Global

| Pattern Type | Scope | Where It Lives |
| --- | --- | --- |
| Language/framework conventions | **Project** | `projects/<name>.md` or project's `tasks/lessons.md` |
| File structure preferences | **Project** | `projects/<name>.md` |
| Security practices | **Global** | `skills/security.md` |
| General best practices | **Global** | Appropriate `skills/*.md` |
| Tool/workflow preferences | **Global** | `skills/wat-framework.md` or `skills/code-quality.md` |
| Git practices | **Global** | `skills/git-workflow.md` |

**Default to project-scoped.** Only promote to global when evidence from multiple projects confirms it's universal. This prevents cross-project contamination (e.g., React patterns leaking into a Flutter project).

## Roadmap Format

Track project phases in a table:

```markdown
| Phase | Status | Focus |
| ----- | ------ | ----- |
| Phase 0 | ✅ Done | Description |
| Phase 1 | 🟡 In Progress | Description |
| Phase 2 | Not started | Description |
```

## TODO → GitHub Issues Sync

All TODO items in project markdown files are synced to GitHub Issues via brainyMcBrain's `tools/todo-to-issues.py` script. This keeps GitHub Issues as the single visible backlog across all projects.

### How TODO Sync Works

- The script parses TODO tables from each project's tracking file (configured in `.sync-config.json` → `todo_file`)
- Creates GitHub Issues with labels: `synced-from-todo`, `phase:P1-core`, `priority:high`, etc.
- Updates existing issues when descriptions change
- Closes issues when TODO status is "Done"
- Title format: `[TODO #N] Description`

### Supported Table Formats

**Format A** (preferred — ilumenTool-style):

```markdown
| # | Phase | Status | Priority | Description |
| 1 | P1    | Open   | High     | Short description |
```

**Format B** (DPO-Dashboard-style):

```markdown
| Task name | ✅ Done / ⬜ Not started | Date |
```

### When to Sync

- **After adding/completing TODO items** — run the sync to keep Issues in sync
- **Locally**: `python3 tools/todo-to-issues.py <project-name>` (from brainyMcBrain)
- **Via GitHub Action**: Actions → "Sync TODOs to GitHub Issues" → Run workflow
- **Dry run first**: Add `--dry-run` flag or check the dry run box in the Action

### Convention

- The TODO markdown file is the **source of truth** — edit there, then sync to Issues
- Never edit synced Issues directly (they'll be overwritten on next sync)
- Issues created manually (without `synced-from-todo` label) are unaffected

## Root Cause Analysis (Kaizen)

> Source: Kaizen/continuous improvement patterns from [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) (617+ stars, GPL-3.0).

When something goes wrong — a bug, a failed approach, a user complaint — don't just fix the symptom. Use structured root cause analysis to find and eliminate the underlying cause.

### The 5 Whys

Ask "why?" iteratively until you reach the root cause (typically 3–5 levels deep):

```text
Problem: Tests pass locally but fail in CI
  Why? → CI uses a different Python version
  Why? → pyproject.toml doesn't pin the Python version
  Why? → We assumed all environments match dev setup
  Root cause: Missing version constraint
  Fix: Pin python-requires in pyproject.toml + add CI matrix
```

**Rules**:

- Each "why" must be supported by evidence (logs, code, config), not speculation
- Stop when you reach something you can directly fix
- If you branch into multiple causes, address the most impactful one first

### Fishbone Diagram (Ishikawa)

For complex problems with multiple potential causes, categorise by source:

| Category | Check |
|----------|-------|
| **Code** | Logic errors, wrong assumptions, missing edge cases |
| **Environment** | Version mismatches, missing dependencies, config drift |
| **Data** | Corrupt input, unexpected format, encoding issues |
| **Process** | Missing tests, skipped reviews, unclear requirements |
| **External** | API changes, service outages, third-party bugs |

### PDCA Cycle (Plan-Do-Check-Act)

For recurring issues or process improvements:

1. **Plan** — Identify the problem and hypothesise a solution
2. **Do** — Implement the fix in a small, controlled scope
3. **Check** — Measure whether the fix actually worked (tests, metrics, user feedback)
4. **Act** — If it worked, standardise it (update skills, docs, CI). If not, go back to Plan

### When to Use What

| Situation | Technique |
|-----------|-----------|
| Single, clear failure | 5 Whys — fast and direct |
| Complex problem, many possible causes | Fishbone — categorise and eliminate |
| Recurring issue, needs process change | PDCA — iterative improvement cycle |

## Spec-Driven Development

> Source: Spec-first methodology from [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) and [obra/superpowers](https://github.com/obra/superpowers).

Write the spec before writing code. A spec is a contract that defines **what** the code must do, so implementation becomes "compilation" — mechanical translation from spec to code.

### When to Write a Spec

| Change Type | Spec Needed? |
|-------------|-------------|
| Bug fix with clear reproduction | No — fix it directly |
| New function with obvious behaviour | No — TDD is sufficient |
| New feature (multi-file, non-trivial) | **Yes — write a brief spec** |
| Architecture change / new module | **Yes — write a full spec** |
| Security-sensitive code | **Yes — spec must cover threat model** |

### Spec Format (Lightweight)

For features and modules, use this structure at minimum:

```markdown
## Spec: [Feature Name]

### Goal
One sentence: what problem does this solve?

### Requirements
- [ ] Functional: what it must do (bullet list)
- [ ] Non-functional: performance, security, accessibility constraints

### Interface
- Inputs: what data comes in (types, validation rules)
- Outputs: what data goes out (types, format)
- Side effects: what changes in the system

### Edge Cases
- What happens with empty input?
- What happens with very large input?
- What happens on failure?

### Not In Scope
- What this feature explicitly does NOT do (prevents scope creep)
```

### Spec-Implementation Loop

1. Write the spec (Markdown, in the feature branch or `docs/`)
2. Review the spec — does it capture all requirements? Ask the user if unclear
3. Implement against the spec — each requirement becomes a task, each edge case becomes a test
4. Verify: every spec requirement has a passing test
5. If implementation reveals spec gaps, **update the spec first**, then code

### Spec Anti-Patterns

- Writing code and then documenting what it does (post-hoc "spec")
- Specs that describe implementation details instead of requirements
- Bloated specs for trivial changes — use judgement on when to skip

## Plan Decomposition

> Source: Task decomposition patterns from [obra/superpowers](https://github.com/obra/superpowers) (77k+ stars, MIT).

Break complex work into small, independently verifiable steps. Each step should be completable in a single focused effort with a clear "done" signal.

### Decomposition Rules

1. **Each step must be verifiable** — "implement the service" is too vague; "add `createUser()` method that passes `test_create_user`" is verifiable
2. **Steps should be ordered by dependency** — don't plan step 5 before step 3 if 5 depends on 3
3. **Include the file path** — every implementation step should name the file(s) it touches
4. **Include the verification** — every step should say how to prove it's done (test, command, visual check)

### Step Format

```markdown
| # | Step | File(s) | Verification |
|---|------|---------|-------------|
| 1 | Add User model with name, email fields | src/models/user.py | `pytest tests/test_user.py::test_user_model` passes |
| 2 | Add create endpoint | src/api/users.py | `curl -X POST /users` returns 201 |
| 3 | Add input validation | src/api/users.py | `pytest tests/test_user.py::test_invalid_email` passes |
```

### Granularity Guidelines

| Scope | Target Step Size |
|-------|-----------------|
| Bug fix | 1–3 steps |
| Small feature | 3–7 steps |
| Large feature / module | 7–15 steps (group into phases) |
| Architecture change | Phase-level decomposition → per-phase step decomposition |

### Re-Planning

If a step takes significantly longer than expected or reveals unexpected complexity:

- **Stop** — don't push through a broken plan
- **Re-assess** — what changed? What do you now know that you didn't?
- **Re-plan** — update the remaining steps with the new understanding
- This is not failure — it's the plan working as designed (plans are hypotheses, not commitments)
