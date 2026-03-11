---
name: event-planning
description: Event design, logistics, and production — budget tracking, timeline management, venue planning, supplier management, and cross-linking. Use whenever planning events, tracking budgets, managing guest lists, or coordinating suppliers.
---

# Event Planning — Domain Skill

> Activate for projects involving event design, logistics, and production.
> (Initially based on 40Jarigen / Peccatum Mortale patterns — expand as more events are planned)

## Project Structure

Event projects typically span multiple disciplines:

| Area | Examples |
|------|---------|
| **Concept** | Theme, narrative, experience design, ideas |
| **Tech** | Puzzles, hardware, app, show control |
| **Logistics** | Budget, venue, suppliers, timeline |
| **Guests** | Invitations, characters, seating |
| **Meta** | Session progress, tag legend, project status |

## Budget Tracking

- Master cost tracker in `logistics/budget/costs.md`
- Always include: item, quantity, unit price, total, supplier link, status
- Cross-reference with BOMs in technical files

## Timeline Management

- Master timeline with chronological phases
- Each phase has clear deliverables and deadlines
- Session progress: numbered entries under date headers

## Cross-Linking Rule

Event projects are **heavily cross-linked**. When changing any file:

1. Search for `[[filename]]` and `[text](path)` references to the changed file
2. Verify all cross-references still make sense
3. Update budget if costs changed
4. Update timeline if dates shifted

## Design Decision Tracking

Track design evolution in the relevant files:

- Mark deprecated designs with a warning banner
- Keep old designs for historical reference
- Point to the current active spec clearly

## Venue Planning

- **Floor plan** with room assignments per act/phase
- **Capacity** per room
- **Power/network** requirements per room
- **Flow diagram** showing guest movement through spaces

## Supplier Management

- One file per major supplier category
- Include: contact info, quote reference, lead time, status
- Link from budget file to supplier files
