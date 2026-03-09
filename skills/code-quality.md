# Code Quality

## Universal Rules

- **Zero warnings, zero errors** is the baseline — maintain it
- Run the project's linter/analyzer **before every commit**
- Fix warnings immediately; don't accumulate tech debt

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
- Never swallow errors silently
- Log errors with context (but never log credentials — see `security.md`)

## Analyzer Hygiene

- When removing a field/variable, grep for **all references** (assignments, reads, comments) and clean up in the same change
- Never suppress warnings on truly dead code — delete it instead
- Only use `// ignore:` for intentionally kept unused code, with a comment explaining why
