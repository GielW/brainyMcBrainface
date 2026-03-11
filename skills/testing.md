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

## TDD Workflow (RED → GREEN → IMPROVE)

> Source: reinforced from [everything-claude-code](https://github.com/affaan-m/everything-claude-code) TDD rule.

1. **RED** — Write a failing test first
2. **GREEN** — Write the minimal implementation to make it pass
3. **IMPROVE** — Refactor while keeping tests green
4. Verify coverage (80%+)

**Key rule**: Fix the implementation, not the tests (unless the test itself is wrong).

## Test Plan Format

For projects with manual test plans, use this table format:

```markdown
| ID | Category | Test Case | Steps | Expected | Status |
| --- | --- | --- | --- | --- | --- |
| T01 | Auth | Login with valid creds | 1. Open app 2. Enter creds 3. Submit | Dashboard loads | PASS |
```

### Status Values

`PASS` | `FAIL` | `SKIP` | `BLOCKED` | `NOT RUN`

## Systematic Debugging

> Source: 4-phase debugging methodology from [obra/superpowers](https://github.com/obra/superpowers) (77k+ stars, MIT).

When a bug surfaces, follow the four phases in order. Do not skip ahead — most debugging waste comes from jumping to "fix" before understanding the root cause.

### Phase 1: Reproduce

- Create the minimal reproduction case — strip away everything unrelated
- Confirm the bug occurs **consistently** (or document the intermittent conditions)
- If you can't reproduce it, you can't verify your fix — get reproduction first

### Phase 2: Isolate

- Narrow down to the smallest unit of code that exhibits the bug
- Use bisection: disable half the system, check if bug persists, narrow further
- Add **targeted** logging or assertions — not scatter-shot `print()` everywhere

### Phase 3: Diagnose

- Read the code at the isolated location — understand what it's **supposed** to do vs what it **actually** does
- Form a hypothesis, then **test it** (don't just assume)
- Check for common causes: off-by-one, null/undefined, stale state, race conditions, wrong scope

### Phase 4: Verify

- Write a test that **fails before** your fix and **passes after** — this proves the fix and prevents regression
- Run the full test suite to ensure no collateral damage
- If the fix required understanding a subtle behaviour, add a comment explaining **why**

### Anti-Patterns

- Changing code without understanding the root cause ("shotgun debugging")
- Adding defensive code around the symptom instead of fixing the cause
- Using `time.sleep()` / arbitrary delays to "fix" race conditions — use proper synchronisation (condition-based waiting, locks, barriers)

## Property-Based Testing

> Source: Property-based and fuzz testing patterns from [trailofbits/skills](https://github.com/trailofbits/skills) (3.5k+ stars, CC-BY-SA-4.0).

Example-based tests verify specific inputs → expected outputs. Property-based tests verify **invariants** across randomly generated inputs, catching edge cases you'd never think to write by hand.

### When to Use

| Technique | Use When |
|-----------|----------|
| Example-based (unit tests) | Fixed input/output, business logic, regression tests |
| Property-based | Parsers, serialisers, data transformations, any function with clear invariants |
| Fuzzing | Security-sensitive code, parsers, protocol handlers, anything with untrusted input |

### Writing Property Tests

1. **Identify the invariant** — what must always be true regardless of input? (e.g., `decode(encode(x)) == x`, `len(sorted(L)) == len(L)`, `output >= 0`)
2. **Define the input space** — use strategies/generators to produce random valid inputs
3. **Assert the invariant** — let the framework find counterexamples

### Tools

| Language | Library | Notes |
|----------|---------|-------|
| Python | `hypothesis` | Best-in-class; integrates with pytest |
| Dart | `glados` | Property-based for Dart |
| JS/TS | `fast-check` | Integrates with Jest/Vitest |

### Fuzzing & Sanitizers

For security-critical code, go beyond property tests:

- **Fuzz testing**: Feed random/malformed inputs to find crashes and undefined behaviour
- **Sanitizers**: Enable AddressSanitizer (ASan), UndefinedBehaviourSanitizer (UBSan) in C/C++/Rust builds
- **Coverage-guided fuzzing**: Use tools like AFL++, libFuzzer to maximise code coverage during fuzzing

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
