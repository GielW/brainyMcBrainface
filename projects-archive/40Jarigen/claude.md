# Claude Code Instructions — 40Jarigen / Peccatum Mortale

> Rules and conventions for AI assistants working on this project.

---

## Project Overview

This is an **immersive 1920s Prohibition-themed 40th birthday party** project, doubling as a proof-of-concept for an immersive experience business in Belgium. Event date: **Saturday 27 June 2026**.

The project spans hardware (chess pieces, PCBs, 3D printing), software (PWA, COGS show control, MQTT), narrative design, logistics, and creative production.

---

## Critical Rule: Update All Linked Files

When making changes to any file, **always check and update all files that reference or are referenced by the changed file**. This project is heavily cross-linked (Obsidian vault style with `[[wikilinks]]` and Markdown links).

Common cross-references to check:

| When you change... | Also update... |
|---|---|
| `concept/ideas.md` (gadgets, chess pieces) | `tech/puzzles/al-capone-gambit.md`, `logistics/budget/costs.md`, `tech/puzzles/puzzle-catalogue.md` |
| `tech/puzzles/al-capone-gambit.md` (PCB/connector spec) | `concept/ideas.md`, `logistics/budget/costs.md`, `tech/app/registration-station.md`, `tech/puzzles/puzzle-catalogue.md` |
| `logistics/budget/costs.md` (prices, BOM) | Verify against source BOMs in linked files |
| `concept/narrative/narrative-framework.md` (story, characters) | `tech/puzzles/puzzle-catalogue.md`, `concept/experience-design/night-flow.md`, `guests/invitations/concept.md` |
| `logistics/venue/home-layout.md` (rooms, layout) | `concept/experience-design/night-flow.md`, `logistics/suppliers/toiletwagen.md` |
| `tech/puzzles/puzzle-catalogue.md` (puzzle list) | `concept/experience-design/night-flow.md` (tech trigger flow diagram) |
| `meta/session-progress.md` (completed items) | Mark corresponding `- [ ]` checkboxes as `- [x]` in source files |
| Any hardware research file | `concept/ideas.md` (Props & Materials Found), `logistics/budget/costs.md` |
| `tech/guides/wax-seal-stamp.md` | `guests/invitations/concept.md` (supplies section) |

**Before finishing any edit session**, search for `[[filename]]` and `[text](path)` references to the changed file and verify they still make sense.

---

## File Conventions

- **Frontmatter:** Every `.md` file has YAML frontmatter with `tags` and `aliases`
- **Tag system:** Use `#type/`, `#status/`, and `#domain/` tags (see `meta/tag-legend.md`)
- **Status tags:** `status/todo` → `status/exploring` → `status/draft` → `status/done`
- **Language:** Mix of English (technical content) and Dutch (logistics, guest-facing text) — match the existing language of each file
- **Links:** Use Obsidian `[[wikilinks]]` for internal references where the file already uses them; use standard Markdown links `[text](path)` otherwise

---

## Session Tracking

- **Session progress** is tracked in `meta/session-progress.md`
- When completing work, add a numbered entry under the appropriate date section in "Completed"
- Update the "Up Next" master timeline (8 phases, chronologically ordered) to reflect current state
- Mark TODOs as done in their source files when completed (don't just log in session-progress)

---

## Design Evolution — Chess Pieces

The chess piece design has evolved. Be aware of the current state:

- **V1 (deprecated):** M12 screw-lock connector + dual-resistor analog ID
- **V2 (current):** DS2401 digital 1-Wire ID + 3-pin magnetic pogo-pin connector + Ø25mm circular SMD PCB
- Old M12 references in `concept/ideas.md` are kept for history but marked with a warning banner
- The active spec is `tech/puzzles/al-capone-gambit.md`

---

## Wax Seal Stamp — Resolved

The wax seal stamp design and 3D printing iteration is **no longer needed**. A professional brass stamp has been ordered from [Stamptitude](https://stamptitude.com). The FDM/SLA prototyping pipeline in `tech/guides/wax-seal-stamp.md` is historical reference only. Do NOT add new stamp-related fabrication tasks.

---

## Key Files (start here)

| Purpose | File |
|---|---|
| Project overview | `README.md` |
| Session log + master timeline | `meta/session-progress.md` |
| Master ideas list | `concept/ideas.md` |
| Evening flow (4 acts + diagrams) | `concept/experience-design/night-flow.md` |
| Narrative & characters | `concept/narrative/narrative-framework.md` |
| Puzzle catalogue (27 puzzles) | `tech/puzzles/puzzle-catalogue.md` |
| Chess piece PCB spec | `tech/puzzles/al-capone-gambit.md` |
| Registration station | `tech/app/registration-station.md` |
| Cost tracker | `logistics/budget/costs.md` |
| Venue layout | `logistics/venue/home-layout.md` |
| Invitations | `guests/invitations/concept.md` |
