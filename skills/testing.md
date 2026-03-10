---
name: testing
description: Test conventions, test types, test plan format, fixture patterns, and runner commands for Python, Dart, and JS/TS. Use whenever writing tests, setting up test infrastructure, or creating test plans.
---

# Testing

## Conventions

- **Test file naming**: `test_<module>.py` (Python), `<module>_test.dart` (Dart), `<module>.test.ts` (JS/TS)
- **Test location**: `tests/` (Python), `test/` (Dart), `__tests__/` or alongside source (JS/TS)
- **Coverage target**: 80%+ on business logic; 100% on security-critical paths

## Test Types

| Type | Purpose | When |
|------|---------|------|
| Unit tests | Isolated function/class testing | Every module |
| Integration tests | Cross-module, database, API | Key workflows |
| E2E tests | Full user flows | Critical paths |
| Manual test plans | Hardware, UI, edge cases | When automation isn't feasible |

## Test Plan Format

For projects with manual test plans, use this table format:

```markdown
| ID | Category | Test Case | Steps | Expected | Status |
| --- | --- | --- | --- | --- | --- |
| T01 | Auth | Login with valid creds | 1. Open app 2. Enter creds 3. Submit | Dashboard loads | PASS |
```

### Status Values

`PASS` | `FAIL` | `SKIP` | `BLOCKED` | `NOT RUN`

## Fixtures & Setup

- Use framework fixtures (`pytest` fixtures, `setUp`/`tearDown`) for test setup
- Prefer factories over shared mutable state
- Use `httpx.AsyncClient` (Python) or equivalent for API tests
- Mock external services; never call real APIs in unit tests

## Running Tests

```bash
# Python
pytest                                # All tests
pytest -x                             # Stop on first failure
pytest --cov=src --cov-report=html    # With coverage
pytest -k "test_specific"             # Run specific

# Dart/Flutter
flutter test                          # All tests
flutter test --coverage               # With coverage

# JavaScript/TypeScript
npm test                              # All tests
npm run test:coverage                 # With coverage
```
