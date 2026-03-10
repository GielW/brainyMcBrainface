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

## Subagent Strategy

- **Use subagents liberally** to keep the main context window clean and focused
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it — spin up subagents rather than cramming everything into one context
- **One task per subagent** for focused execution and cleaner results
- Keep the main agent for orchestration and decision-making; let subagents do the heavy lifting

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

```
.tmp/           # Temporary/intermediate files (disposable, regenerated as needed)
tools/          # Python scripts for deterministic execution
workflows/      # Markdown SOPs defining what to do and how
.env            # API keys and environment variables (NEVER elsewhere)
```

**Core file principle:** Local files are for processing. Deliverables go to cloud services (Google Sheets, Slides, etc.) where the user can access them directly. Everything in `.tmp/` is disposable.
