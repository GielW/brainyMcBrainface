---
name: code-quality
description: Universal code hygiene — linting, naming, dead code, imports, error handling, execution discipline, and analyzer cleanup. Use whenever writing, reviewing, or refactoring code in any language.
---

# Code Quality

## Universal Rules

- **Zero warnings, zero errors** is the baseline — maintain it
- Run the project's linter/analyzer **before every commit**
- Fix warnings immediately; don't accumulate tech debt

## Immutability

> Source: [everything-claude-code](https://github.com/affaan-m/everything-claude-code) coding-style rule.

Prefer creating new objects over mutating existing ones. Immutable data prevents hidden side effects, makes debugging easier, and enables safe concurrency. Exceptions exist (performance-critical loops, builder patterns), but the default should be **copy, don't mutate**.

## File & Function Size

- **Files**: 200–400 lines typical, 800 max. Extract when a file grows beyond this
- **Functions**: < 50 lines. If it's longer, it's doing too much
- **Nesting**: Max 4 levels deep. Flatten with early returns or extraction

## Linting & Formatting

Every project must have a configured linter and formatter:

| Language | Linter | Formatter | Type Checker |
|----------|--------|-----------|-------------|
| Python | `ruff` | `black` | `mypy` (strict) |
| Dart | `flutter analyze` | `dart format` | Built-in |
| JavaScript/TypeScript | `eslint` | `prettier` | `tsc` |

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Files (Python) | `snake_case.py` | `data_service.py` |
| Files (Dart) | `snake_case.dart` | `build_order.dart` |
| Files (JS/TS) | `camelCase.ts` or `kebab-case.ts` | per project config |
| Classes | `PascalCase` | `BuildOrder`, `DpiaEngine` |
| Functions/methods | `snake_case` (Python) / `camelCase` (Dart/JS) | |
| Variables | `snake_case` (Python) / `camelCase` (Dart/JS) | |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Private members | `_` prefix | `_internalState` |

## Dead Code

- **Delete dead code** — don't comment it out
- If keeping for reference, move to an `old_files/` or `archive/` directory (gitignored)
- For intentionally unused code, use language-specific `// ignore:` annotations

## Imports

- Always use sorted, grouped imports
- Prefer absolute/package imports over relative paths
- Group: stdlib → third-party → local

## Error Handling

- **Always add error handling** in new code (try-catch, Result types, etc.)
- Never swallow errors silently — silent failures make debugging in production nearly impossible because the symptom appears far from the cause
- Log errors with context (but never log credentials — see `security.md`)

## Execution Discipline

### Core Principles

- **Simplicity first** — Make every change as simple as possible. Impact minimal code
- **No laziness** — Find root causes. No temporary fixes. Senior developer standards
- **Minimal impact** — Changes should only touch what's necessary. Avoid introducing bugs

### Demand Elegance (Balanced)

- For non-trivial changes, pause and ask: "Is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### Autonomous Problem Solving

- When given a bug report: just fix it — don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Fix failing CI tests without being told how

## Analyzer Hygiene

- When removing a field/variable, grep for **all references** (assignments, reads, comments) and clean up in the same change
- Never suppress warnings on truly dead code — delete it instead
- Only use `// ignore:` for intentionally kept unused code, with a comment explaining why

## Quality Gates

> Source: LLM-as-Judge and structured evaluation patterns from [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) (617+ stars, GPL-3.0).

Quality gates are checkpoints where work must meet defined criteria before proceeding. Use them to prevent low-quality output from flowing downstream.

### Gate Placement

| Gate | When | What It Checks |
|------|------|---------------|
| **Pre-commit** | Before every commit | Linter clean, tests pass, no secrets, no dead code |
| **Pre-PR** | Before opening a PR | Spec requirements met, coverage ≥ 80%, CHANGELOG updated |
| **Pre-merge** | Before merging to main | CI green, review approved, no regressions |
| **Pre-release** | Before deploying | E2E tests pass, SBOM generated, security scan clean |

### Structured Rubrics

For subjective quality (code reviews, design reviews, documentation), use explicit rubrics instead of gut feeling:

```markdown
| Criterion | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Correctness | _ | Tests pass? Edge cases covered? |
| Readability | _ | Clear naming? Appropriate comments? |
| Simplicity | _ | Minimal code for the task? No over-engineering? |
| Security | _ | Input validated? Secrets safe? |
| Completeness | _ | All requirements met? Docs updated? |
```

**Rules**:
- Every score must cite **specific evidence** — no vibes-based scoring
- A score of 1–2 on any criterion is a **blocker** — fix before proceeding
- Average below 3 means "go back and redo", not "ship with caveats"

### Self-Review Checklist

Before submitting any non-trivial change, run through this yourself:

- [ ] Does it do what was asked? (re-read the requirement)
- [ ] Are there untested edge cases?
- [ ] Did I leave any temporary code, debug prints, or TODOs?
- [ ] Would a colleague understand this without explanation?
- [ ] Does it pass all quality gates above?
