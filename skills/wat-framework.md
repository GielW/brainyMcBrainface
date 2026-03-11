---
name: wat-framework
description: The Workflows-Agents-Tools architecture for AI-assisted execution. Separates deterministic tools from probabilistic reasoning. Use whenever designing automation, deciding between agent vs script execution, structuring workflows, or managing subagents.
---

# WAT Framework — Workflows, Agents, Tools

> Architecture for AI-assisted execution. Separates probabilistic reasoning (agent) from deterministic execution (tools), orchestrated by human-written instructions (workflows).

---

## Core Principle

When AI handles every step directly, accuracy compounds negatively (90% per step → 59% after five). Offload execution to deterministic scripts; focus the agent on orchestration and decision-making.

## The Three Layers

### Layer 1: Workflows (The Instructions)

- Markdown SOPs stored in `workflows/`
- Each workflow defines: objective, required inputs, which tools to use, expected outputs, edge case handling
- Written in plain language — the same way you'd brief a team member

### Layer 2: Agent (The Decision-Maker)

- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, ask clarifying questions when needed
- Connect intent to execution without trying to do everything directly
- Example: need to scrape a website? Read `workflows/scrape_website.md`, determine inputs, then execute `tools/scrape_single_site.py`

### Layer 3: Tools (The Execution)

- Python scripts in `tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys live in `.env` — never stored anywhere else
- Scripts are consistent, testable, and fast

## Search-First Principle

> Source: `search-first` skill from [everything-claude-code](https://github.com/affaan-m/everything-claude-code).

Before writing custom code for any non-trivial functionality:

1. **Check the repo** — does this already exist? (`rg` / grep through modules and tests)
2. **Check package registries** — npm, PyPI, pub.dev for existing solutions
3. **Check MCP servers / plugins** — is there a tool that already does this?
4. **Check GitHub** — maintained OSS implementations?

### Decision Matrix

| Signal | Action |
| --- | --- |
| Exact match, well-maintained, permissive license | **Adopt** — install and use directly |
| Partial match, good foundation | **Extend** — install + thin wrapper |
| Multiple weak matches | **Compose** — combine 2–3 small packages |
| Nothing suitable | **Build** — write custom, but informed by research |

### Search-First Anti-Patterns

- Jumping to code without checking if a solution exists
- Over-wrapping a library so heavily it loses its benefits
- Installing a massive dependency for one small feature

## Subagent Strategy

- **Use subagents liberally** to keep the main context window clean and focused
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it — spin up subagents rather than cramming everything into one context
- **One task per subagent** for focused execution and cleaner results
- Keep the main agent for orchestration and decision-making; let subagents do the heavy lifting

### The Sub-Agent Context Problem

> Source: Longform Guide from [everything-claude-code](https://github.com/affaan-m/everything-claude-code).

Sub-agents only know the literal query, not the PURPOSE behind the request. Use the **Iterative Retrieval Pattern**:

1. Orchestrator sends query with objective context (not just the question)
2. Evaluate every sub-agent return — ask follow-up questions before accepting
3. Sub-agent goes back to source, refines, returns
4. Loop until sufficient (max 3 cycles)

### Sequential Phases for Complex Work

```text
Phase 1: RESEARCH  → research-summary.md
Phase 2: PLAN      → plan.md
Phase 3: IMPLEMENT → code changes
Phase 4: REVIEW    → review-comments.md
Phase 5: VERIFY    → done or loop back
```

- Each agent gets ONE clear input and produces ONE clear output
- Outputs become inputs for the next phase
- Store intermediate outputs in files
- Use `/clear` between agents when context is exhausted

## Operating Rules

### 1. Tool-First

Before building anything new, check `tools/` based on what the workflow requires. Only create new scripts when nothing exists for that task.

### 2. Learn and Adapt on Failure

When you hit an error:

1. Read the full error message and trace
2. Fix the script and retest (if it uses paid API calls or credits, **check with the user before re-running**)
3. Document what you learned in the workflow (rate limits, timing quirks, unexpected behavior)
4. Example: rate-limited on an API → discover batch endpoint → refactor tool → verify → update workflow

### 3. Keep Workflows Current

- Workflows evolve as you learn — update them when you find better methods, discover constraints, or encounter recurring issues
- **Never create or overwrite workflows without asking** unless explicitly told to
- Workflows are instructions to be preserved and refined, not discarded after one use

## The Self-Improvement Loop

Every failure makes the system stronger — fix the tool, update the workflow, move on with a more robust system:

1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow with the new approach

For the broader learning capture pattern (lessons files, cross-project routing), see the Self-Improvement Loop in `project-tracking.md`.

## Standard Directory Layout

```text
.tmp/           # Temporary/intermediate files (disposable, regenerated as needed)
tools/          # Python scripts for deterministic execution
workflows/      # Markdown SOPs defining what to do and how
.env            # API keys and environment variables (NEVER elsewhere)
```

**Core file principle:** Local files are for processing. Deliverables go to cloud services (Google Sheets, Slides, etc.) where the user can access them directly. Everything in `.tmp/` is disposable.

## Context & Token Awareness

> Source: Token optimization and context management from [everything-claude-code](https://github.com/affaan-m/everything-claude-code).

### Model Selection

| Task Type | Model Tier | Why |
| --- | --- | --- |
| Exploration, search, simple edits | Fastest/cheapest | Good enough for finding files, single-file changes |
| Multi-file implementation, PR reviews | Mid-tier (Sonnet) | Best balance for coding, catches nuance |
| Architecture, security, complex debugging | Premium (Opus) | Deep reasoning, can't afford to miss things |

Default to mid-tier for 90% of coding. Upgrade when first attempt failed, task spans 5+ files, or is security-critical.

### Context Window Hygiene

- Keep unused MCP servers disabled — each tool description eats context tokens
- Aim for < 10 MCP servers active, < 80 tools loaded
- Use CLI wrappers / skills instead of MCP servers where feasible (e.g., `gh pr create` instead of GitHub MCP)
- Modular codebases (small files, small functions) reduce token cost per task and increase first-try accuracy

### Session Lifecycle

- Compact at logical breakpoints (after research, after milestone, after debugging) — never mid-implementation
- Use `/clear` between unrelated tasks
- Persist session state to files for cross-session continuity
- Monitor context usage — avoid the last 20% of the context window for complex multi-file work

## Parallelization

> Source: Parallelization patterns from [everything-claude-code](https://github.com/affaan-m/everything-claude-code) longform guide.

### Core Rule

The goal is: **how much can you get done with the minimum viable amount of parallelization.** Don't set arbitrary terminal counts — add a parallel instance only out of true necessity.

### Git Worktrees (Parallel Code Changes)

When multiple agent instances work on code that overlaps, use git worktrees to avoid conflicts. Each worktree is an independent checkout:

```bash
git worktree add ../project-feature-a feature-a
git worktree add ../project-feature-b feature-b
# Each worktree gets its own agent instance
cd ../project-feature-a && claude
```

- Each instance must have a **well-defined, non-overlapping scope**
- Name all chats (`/rename <name>`) so you can tell them apart
- Use worktrees when tasks touch the same files; use simple forks when they don't

### Fork for Research vs Code

The simplest parallelization pattern:

- **Main chat** → code changes (implementation, refactoring)
- **Forked chats** → questions about the codebase, research on external services, exploration

This keeps the main context clean for implementation while offloading read-only analysis to forks.

### The Cascade Method

When running multiple instances:

1. Open new tasks in new tabs **to the right**
2. Sweep left to right, oldest to newest
3. Focus on **at most 3–4 tasks** at a time
4. Close completed tabs to keep the workspace manageable

### Two-Instance Kickoff Pattern

For new projects or major features, start with 2 instances:

| Instance | Role | Focus |
| --- | --- | --- |
| **Instance 1** | Scaffolding Agent | Lays down project structure, configs, CLAUDE.md, rules |
| **Instance 2** | Deep Research Agent | Connects to services, creates PRD, architecture diagrams, gathers documentation |

They work in parallel without stepping on each other, then merge their outputs before implementation begins.

## Reflexion & Self-Critique

> Source: Reflexion pattern from [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) (617+ stars, GPL-3.0) and multi-perspective critique from [obra/superpowers](https://github.com/obra/superpowers).

Don't accept your first output — iterate on it. The reflexion pattern improves quality by forcing structured self-evaluation before delivering results.

### The Reflexion Loop

1. **Generate** — Produce an initial solution (code, plan, analysis)
2. **Critique** — Evaluate your own output against explicit criteria:
   - Does it meet all stated requirements?
   - Are there edge cases not handled?
   - Is there a simpler approach?
   - Would a senior engineer accept this?
3. **Refine** — Fix the issues found in critique
4. **Loop** — Repeat until no meaningful improvements remain (max 3 cycles to avoid over-polishing)

### When to Invoke Reflexion

| Situation | Reflexion Level |
|-----------|----------------|
| Simple, isolated change | Skip — direct execution |
| Multi-file implementation | Light — one critique pass after initial code |
| Architecture / security decisions | Full — 2–3 reflexion cycles with explicit criteria |
| User-facing output (reports, specs) | Full — critique for clarity, accuracy, completeness |

### Multi-Perspective Critique

For high-stakes decisions, evaluate from multiple viewpoints:

- **Correctness**: Does this actually work for all inputs and edge cases?
- **Security**: What can go wrong if this is attacked or misused?
- **Maintainability**: Will a future developer understand this in 6 months?
- **Performance**: Are there obvious inefficiencies or scalability traps?
- **User impact**: Does this actually solve the user's problem?

When the decision is complex enough, use the Council of Masters (`skills/council-of-masters.md`) for full multi-expert deliberation.

### Memorise Insights

When reflexion reveals a pattern or mistake:

- Capture it in the project's `tasks/lessons.md`
- If it's cross-project, route to the brainyMcBrain Inbox (see Self-Improvement Loop in `project-tracking.md`)
- Never let the same mistake pass through reflexion twice

## Context Engineering

> Source: Research-backed patterns from [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) — attention budget, progressive disclosure, lost-in-middle effect.

Context engineering is the discipline of controlling **what goes into the context window, in what order, and how much** — because LLMs are not equally attentive to all positions in their context.

### The Attention Budget

Every project, agent, or skill file consumes context tokens. Treat context space like a limited budget:

- **Front-load the important stuff** — instructions at the start of context get the most attention
- **Back-load secondary detail** — supporting data, examples, reference tables go later
- **Avoid the middle** — the "lost-in-middle" effect means content in the middle of long contexts gets the least attention. Place critical instructions at the start or end, never buried in the middle

### Progressive Disclosure

Don't dump everything into context at once. Load information in stages:

1. **Always loaded**: Core identity, universal skills, active project summary
2. **On-demand**: Domain skills, language modules — only when the task needs them
3. **Just-in-time**: Specific file contents, research results — load when acting on them

This is already how brainyMcBrain's `@`-import system works. The same principle applies within sessions:

- Don't read 10 files "just in case" — read when you need them
- Use search tools to find the right file first, then read targeted sections
- Discard intermediate results (summarise, then clear raw data)

### Token Efficiency Patterns

| Pattern | Saves Tokens | How |
|---------|-------------|-----|
| Modular files (small, focused) | High | Only load the modules you need |
| Summary → detail drill-down | Medium | Start with overview, drill down on demand |
| CLI tools over MCP servers | Medium | No tool descriptions eating context |
| Compacting at milestones | High | Reset context without losing progress |
| Structured output formats | Low | Concise tables > verbose prose |

### Context Anti-Patterns

- Loading all project files at session start ("just in case")
- Keeping raw search results in context after extracting what you need
- Running 10+ MCP servers simultaneously (each adds tool descriptions to context)
- Ignoring context window usage until you hit truncation
