# 40Jarigen / Peccatum Mortale

> **Skills**: @skills/* (all), @languages/web-pwa.md, @domains/event-planning.md, @domains/obsidian-vault.md, @domains/iot-hardware.md

## Project Overview

**Immersive 1920s Prohibition-themed 40th birthday party** — proof-of-concept for an immersive experience business in Belgium.

- **Event date**: Saturday 27 June 2026
- **Repository**: `GielW/40Jarigen` (private)
- **Disciplines**: Hardware (chess pieces, PCBs, 3D printing), software (PWA, COGS show control, MQTT), narrative design, logistics, creative production

## Active Skills

This project uses:
- **Event planning** — venue, budget, suppliers, guest management
- **IoT hardware** — DS2401 1-Wire, ESP32, PCBs, pogo-pin connectors
- **Obsidian vault** — wikilinks, session tracking, MOCs
- **Web/PWA** — registration station app

## Key Files

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

## Cross-Reference Map

| When you change... | Also update... |
|---|---|
| `concept/ideas.md` (gadgets, chess pieces) | `tech/puzzles/al-capone-gambit.md`, `logistics/budget/costs.md`, `tech/puzzles/puzzle-catalogue.md` |
| `tech/puzzles/al-capone-gambit.md` (PCB/connector spec) | `concept/ideas.md`, `logistics/budget/costs.md`, `tech/app/registration-station.md`, `tech/puzzles/puzzle-catalogue.md` |
| `logistics/budget/costs.md` (prices, BOM) | Verify against source BOMs in linked files |
| `concept/narrative/narrative-framework.md` (story, characters) | `tech/puzzles/puzzle-catalogue.md`, `concept/experience-design/night-flow.md`, `guests/invitations/concept.md` |
| `logistics/venue/home-layout.md` (rooms, layout) | `concept/experience-design/night-flow.md`, `logistics/suppliers/toiletwagen.md` |
| `tech/puzzles/puzzle-catalogue.md` (puzzle list) | `concept/experience-design/night-flow.md` (tech trigger flow diagram) |
| `meta/session-progress.md` (completed items) | Mark `- [ ]` → `- [x]` in source files |
| Any hardware research file | `concept/ideas.md` (Props & Materials Found), `logistics/budget/costs.md` |

## Design Evolution — Chess Pieces

- **V1 (deprecated):** M12 screw-lock connector + dual-resistor analog ID
- **V2 (current):** DS2401 digital 1-Wire ID + 3-pin magnetic pogo-pin connector + Ø25mm circular SMD PCB
- Active spec: `tech/puzzles/al-capone-gambit.md`

## Resolved Items

- **Wax seal stamp**: Professional brass stamp ordered from Stamptitude. FDM/SLA pipeline in `tech/guides/wax-seal-stamp.md` is historical only. Do NOT add new stamp tasks.

## Language Note

Mix of English (technical content) and Dutch (logistics, guest-facing text) — match the existing language of each file.
