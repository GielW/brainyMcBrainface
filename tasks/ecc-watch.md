# External Watch — everything-claude-code

> Track useful patterns from [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) (71k+ stars, MIT license) and sync relevant updates to brainyMcBrainface skills.

<!-- Also tracks other repos discovered during skill research (March 2026). -->

## Repo Details

- **URL**: <https://github.com/affaan-m/everything-claude-code>
- **Current version at analysis**: v1.8.0 (Mar 2026)
- **License**: MIT
- **Last reviewed**: 2026-03-11

## What We Already Extracted (2026-03-11)

### Promoted to skills

| ECC Source | brainyMcBrainface Target | What We Took |
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

---

## Additional Watch List

> Added March 2026 from web research session. These repos contain patterns we partially extracted (Tier 1 & 2 items implemented). Watch for deeper patterns, updates, and new skills.

### obra/superpowers (77k+ stars, MIT)

- **URL**: <https://github.com/obra/superpowers>
- **Last reviewed**: 2026-03-11
- **What we extracted**: Systematic debugging (4-phase), plan decomposition (micro-tasks), spec-driven development patterns, reflexion/self-critique methodology
- **What to watch for**:
  - Full brainstorming → planning → subagent-driven-dev → code review pipeline (deeper than what we took)
  - Test-writing methodology updates (their approach to test-first is more prescriptive)
  - New subagent orchestration patterns beyond what's in our WAT framework
- **Next review**: June 2026

### trailofbits/skills (3.5k+ stars, CC-BY-SA-4.0)

- **URL**: <https://github.com/trailofbits/skills>
- **Last reviewed**: 2026-03-11
- **What we extracted**: Property-based testing patterns, supply chain risk analysis depth, fuzzing & sanitiser guidance
- **What to watch for**:
  - Code auditing / variant analysis skills (deep security review methodology — not yet in our skills)
  - Vulnerability research patterns (structured approach to finding security bugs)
  - Semgrep/CodeQL rule writing (automated security scanning — could enrich `skills/security.md`)
  - New language-specific security skills
- **Next review**: June 2026

### NeoLabHQ/context-engineering-kit (617+ stars, GPL-3.0)

- **URL**: <https://github.com/NeoLabHQ/context-engineering-kit>
- **Last reviewed**: 2026-03-11
- **What we extracted**: Reflexion pattern, Kaizen/5 Whys/PDCA, spec-driven development, context engineering (attention budget, progressive disclosure), quality gates / LLM-as-Judge
- **What to watch for**:
  - First Principles Framework (FPF) — hypothesis-driven ADI reasoning (we noted it but didn't implement)
  - MAKER pattern — more structured version of plan decomposition
  - Research-backed prompt engineering patterns (they cite academic papers)
  - Updates to their reflexion and kaizen patterns as community contributes
- **Next review**: June 2026

### K-Dense-AI/claude-scientific-skills

- **URL**: <https://github.com/K-Dense-AI/claude-scientific-skills>
- **Last reviewed**: 2026-03-11 (surface-level; not deeply analysed)
- **What we extracted**: Nothing yet — flagged for deeper review
- **What to watch for**:
  - Scientific/research methodology skills (hypothesis formation, experiment design)
  - Data analysis patterns (statistical testing, visualisation)
  - Engineering domain skills (may overlap with `domains/iot-hardware.md`)
  - Could inform a new `domains/data-science.md` or `domains/research.md` if patterns are strong enough
- **Next review**: June 2026
