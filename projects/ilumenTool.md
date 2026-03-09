# ilumenTool

> **Skills**: @skills/* (all), @languages/dart-flutter.md, @domains/iot-hardware.md

## Project Overview

**Cross-platform Flutter desktop application** (Linux + Windows) for iLumen BV. Covers the full lifecycle of iLumen IoT hardware products: firmware flashing, EEPROM cloning, automated testing, production batch management, and field installation/commissioning.

- **Repository**: `RdFutech/ilumenTool` — branch `iLumenTool_V2.0`
- **Flutter project root**: `ilumentool/` (one level below repo root)
- **Current version**: 2.0.0-alpha.8

## Active Skills

This project uses:
- **Dart/Flutter** — desktop app, Firebase, Firestore
- **IoT hardware** — ESP32 (esptool), AVR (avrdude), MQTT, 1-Wire
- **Security** — Firestore-backed secrets, credential rotation
- **CI/CD** — GitHub Actions (build on tag push)

## Supported Products

| Code | Product | MCU | Wireless | ThingsBoard Type |
| ---- | ------- | --- | -------- | ---------------- |
| `ILB` | Ilubat | ATmega328P | ESP32 | `ILUBAT` |
| `ILB2` | Ilubat v2 | ATmega64 | ESP32 | `ILUBAT2` |
| `ILC` | Ilucharge | ATmega | ESP32 | `ILUCHARGE` |
| `ILC2` | Ilucharge v2 | ATmega | ESP32 | `ILUCHARGE` |
| `ILH` | Iluheat | ATmega48 | ESP32 | `ILUHEAT` |
| `ILH-SGR` | Iluheat SGR | — | ESP32 | `ILUHEAT_SGR` |
| `ILS` | Ilusmart | ATmega | ESP32 | `ILUSMART` |

**When adding a new product**, update ALL of:
1. `programming_view.dart` — `_config` array entry
2. `product_button_widget.dart` — button label + navigation case
3. `programming_tab.dart` — product button grid
4. `thingsboard_connector.dart` — device type mapping + attributes
5. `product_manager.dart` — serial number/category mapping
6. `espressif.dart` — SPIFFS config JSON + firmware path mappings
7. `production_view.dart` — dropdown menu item

## External Services

| Service | Purpose | Status |
|---------|---------|--------|
| Firebase/Firestore | Auth, secrets, device records, build orders | Active (via `firedart`) |
| ThingsBoard | IoT device provisioning | Active |
| MQTT | Device communication (ILS:1884, ILC:1883) | Active |
| InvenTree | Warehouse/BOM management | Planned |

## Firebase Platform Abstraction

Official Firebase SDKs don't support Linux. Solution: abstraction layer in `lib/services/firebase/`:
- `firebase_interface.dart` — abstract `FirebaseBackend`
- `firedart_backend.dart` — firedart (works Linux + Windows)
- `official_sdk_backend.dart` — official SDK (Windows only, stub)
- `firebase_factory.dart` — selects backend by platform

## Build Orders (Firestore)

Collection `build_orders/{orderId}` — status workflow: `draft` → `approved` → `in_progress` → `completed` (or `cancelled`).

Tab access: Users need `BuildOrders: true` in Firestore `Users/{email}/tabs/tabs`.

## Linked Files Checklist

| File | What to update |
| ---- | -------------- |
| `docs/TODO.md` | Add/close items, Phase tags, Summary counts |
| `claude.md` | Roadmap, known issues, relevant sections |
| `test/test_plan.md` | Test cases, summary counts |
| `README.md` | Features, structure, version history |
| `firestore.rules` | Rules for new collections |

**After every change**: `flutter analyze` — 0 warnings, 0 errors confirmed.

## Known Issues

- **Monolithic files**: `programming_view.dart` (2,385 lines), `ilusmart1_setup.dart` (1,550 lines) — planned decomposition
- **Product if-chains**: Product type mapping via chained `if` in 8+ files — refactor to registry/enum
- **Credential rotation**: Deferred until all deployed instances run Firestore-backed version

## Roadmap

| Phase | Status | Focus |
| ----- | ------ | ----- |
| Phase 0 | ✅ Done | Security — secrets externalized |
| Phase 1 | 🟡 In Progress | Core cleanup: auto-updater, lint, Firebase, GSheets→Firestore, ESP bugs |
| Phase 2 | Not started | Architecture: product registry, state management, wire `ilumentool_db` |
| Phase 3 | Not started | View decomposition: break monoliths |
| Phase 4 | Not started | Testing, logging, CI/CD, documentation |
| Extras (PX) | 🟡 Ongoing | Build orders, InvenTree integration, label printing |

## Completed Migrations

- ✅ GSheets → Firestore (March 5, 2026) — `gsheetConnector.dart` removed, all paths Firestore-only
- ✅ File naming standardisation (March 9, 2026) — 37 files + 4 folders → `snake_case`
- ✅ Lint cleanup — 46 → 4 info-level issues
- ✅ ESP progress bar bugs fixed
- ✅ Firebase platform abstraction implemented
