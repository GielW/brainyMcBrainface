# External Watch — everything-claude-code

> Track useful patterns from [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) (71k+ stars, MIT license) and sync relevant updates to brainyMcBrain skills.

## Repo Details

- **URL**: https://github.com/affaan-m/everything-claude-code
- **Current version at analysis**: v1.8.0 (Mar 2026)
- **License**: MIT
- **Last reviewed**: 2026-03-11

## What We Already Extracted (2026-03-11)

### Promoted to skills

| ECC Source | brainyMcBrain Target | What We Took |
| --- | --- | --- |
| `the-security-guide.md` | `skills/security.md` | Agent security (prompt injection, OWASP Agentic Top 10, sandboxing, sanitization, supply chain) |
| `rules/common/coding-style.md` | `skills/code-quality.md` | Immutability principle, file/function size limits |
| `skills/search-first/SKILL.md` | `skills/wat-framework.md` | Search-first workflow with decision matrix |
| `the-longform-guide.md` | `skills/wat-framework.md` | Sub-agent context problem, iterative retrieval, sequential phases, context/token optimization |
| `rules/common/testing.md` | `skills/testing.md` | TDD RED→GREEN→IMPROVE naming, "fix implementation not tests" |
| `skills/strategic-compact/SKILL.md` + longform guide | `skills/project-tracking.md` | Strategic compaction timing, verification loop patterns (checkpoint vs continuous, pass@k) |
| `skills/continuous-learning-v2/SKILL.md` | `skills/project-tracking.md` | Pattern Maturity Model — observation→pattern→convention stages, confidence signals, project vs global scoping |
| Longform guide parallelization section | `skills/wat-framework.md` | Git worktrees, fork for research vs code, cascade method, two-instance kickoff |
| `hooks/memory-persistence/` + longform guide | `skills/project-tracking.md` | Session Lifecycle Discipline — start/compact/end practices, handoff file format |

### Still in Inbox (review pending)

None — all items promoted.

## What to Watch for on Updates

- New skills in `skills/` that map to our language/domain areas (especially Python, web/PWA, security)
- Updates to `the-security-guide.md` — agent security is evolving fast
- New rules in `rules/common/` — universal coding patterns
- Changes to `skills/continuous-learning-v2/` — instinct model evolution
- New `rules/python/` patterns that could enrich `languages/python.md`
- Hooks patterns in `hooks/` that could inform automation

## Review Cadence

Check quarterly (or when a major release is tagged) for new patterns worth extracting.
Next review: **June 2026**
