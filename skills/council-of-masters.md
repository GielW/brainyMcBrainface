---
name: council-of-masters
description: Multi-expert deliberation framework for complex questions. Assembles a dynamic council of 3–5 domain masters who each analyze the problem from their unique perspective, debate, and synthesize a superior answer. Use whenever a question spans multiple domains, involves trade-offs, has no obvious right answer, or would benefit from adversarial challenge — architecture decisions, strategy, debugging mysteries, ethical dilemmas, or any "it depends" question.
---

# Council of Masters — Multi-Expert Deliberation

> When one perspective isn't enough, convene a council. Each master brings deep expertise in a different facet of the problem. They deliberate, challenge each other, and converge on a synthesis that no single expert could reach alone.

---

## When to Convene the Council

This technique shines when the problem has **multiple valid angles** that interact:

- Architecture or design decisions with competing trade-offs
- Debugging mysteries where the root cause could live in several layers
- Strategy questions that touch business, technical, and user dimensions
- "Should we...?" questions where the answer genuinely depends on perspective
- Risk assessment across domains (security vs. usability vs. cost vs. timeline)
- Ethical or regulatory dilemmas with legitimate tension between priorities

Skip it for straightforward questions with a clear factual answer. A council deliberating "what's the syntax for a for-loop" wastes everyone's time.

## How the Council Works

### Phase 1: Assess the Question

Read the user's question and identify the **distinct domains** it touches. A good council has tension — masters who will naturally disagree because they optimise for different things.

### Phase 2: Assemble the Council (3–5 Masters)

Select masters dynamically based on the question. Each master has:

- A **title** describing their expertise
- A **lens** — what they optimise for and what they watch out for
- A clear reason they're at the table (they must earn their seat)

The council should include at least one **contrarian** — someone likely to push back on the obvious answer. Groupthink is the enemy.

**Example roster for "Should we rewrite the monolith in microservices?":**

| Master | Lens |
|--------|------|
| Systems Architect | Scalability, separation of concerns, long-term maintainability |
| Pragmatic Engineer | Delivery speed, team capacity, migration risk |
| Security Lead | Attack surface, secret management, inter-service auth |
| Product Strategist | Business value, user impact, opportunity cost |

**Bad council selection** — 4 masters who all think the same way. If you're picking "Frontend Expert, CSS Expert, UI Expert, Design Expert" for a CSS question, you don't need a council.

### Phase 3: Individual Analysis

Each master gives their take **independently** before seeing the others' views. This prevents anchoring bias. Each analysis should be concise (3–5 sentences) and include:

1. Their assessment of the core problem as seen through their lens
2. What they'd recommend
3. What risk or blind spot they see that others might miss

### Phase 4: Deliberation

The masters respond to each other. This is where the value happens:

- **Challenge**: "The Architect says decouple everything, but with a 3-person team that's a maintenance nightmare" (Pragmatic Engineer)
- **Build on**: "I agree with the security concern, and I'd add that the compliance timeline makes this urgent" (Product Strategist)
- **Reframe**: "You're all debating build vs. buy, but the real question is whether this feature even belongs in our product" (contrarian)

Keep deliberation focused — one round of responses is usually enough. Two rounds if there's genuine unresolved tension.

### Phase 5: Synthesis

Produce a unified recommendation that:

1. **States the verdict** — lead with the answer, not the process
2. **Shows the reasoning** — which arguments won and why
3. **Acknowledges dissent** — if a master was outvoted, explain their concern and why it was accepted as a known risk or mitigated
4. **Defines conditions** — "This recommendation holds if X. If Y changes, revisit"

## Output Format

```markdown
## Council Verdict: [one-line answer]

### The Council
- **[Master 1 title]** — [lens in 5 words]
- **[Master 2 title]** — [lens in 5 words]
- **[Master 3 title]** — [lens in 5 words]

### Key Arguments
[2–4 bullet points capturing the strongest arguments that shaped the verdict]

### Dissent
[Which master(s) disagreed and why — this is valuable signal, not noise]

### Recommendation
[Concrete, actionable next steps]

### Conditions
[When to revisit this decision]
```

## Principles

- **Earn your seat** — every master must bring a genuinely different perspective. Overlapping experts dilute the council's value
- **Tension is the point** — if all masters agree immediately, either the question was too easy or the council was poorly assembled
- **Brevity over theatre** — the deliberation should be tight and useful, not a roleplay exercise. Skip the "As the Security Master, I must say..." preamble
- **Dissent is signal** — a minority opinion that gets recorded is more valuable than false unanimity. The dissenter might be right and you'll want that record later
- **Dynamic assembly** — never use the same council for every question. The whole point is matching expertise to the problem

## Example

**User question**: "We need to add multi-language support to the DPO-Dashboard. Should we use i18n library, database-driven translations, or hardcoded JSON files?"

**Council assembled**:

- **DPO/Compliance Lead** — regulatory accuracy in NL/FR/EN
- **Python Architect** — maintainability, developer experience
- **UX Specialist** — translator workflow, end-user experience
- **Pragmatic Engineer** — delivery speed, current team capacity

**Synthesis** (abbreviated):
> **Verdict**: JSON files with a thin i18n wrapper — start simple, migrate later if scale demands it.
>
> The Compliance Lead insisted translations must be reviewed by legal before deployment (ruling out community/crowdsource). The Architect preferred a proper i18n library (gettext/babel) for plural rules, but the Pragmatic Engineer noted the team is 1 person and the app has 3 target languages — a library adds ceremony without proportional value yet. The UX Specialist flagged that JSON files let non-developers contribute translations via PR. Dissent from the Architect: "You'll hit edge cases with plurals and gendered nouns in French — plan migration to babel once you exceed 500 translation keys."
