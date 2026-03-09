# DPO-Dashboard

> **Skills**: @skills/* (all), @languages/python.md, @domains/obsidian-vault.md, @domains/belgian-legal.md

## Project Overview

**DPO/DPA Cybersecurity & Compliance Dashboard** — local-first, open-source dashboard for Data Protection Officers under Belgian and EU data protection law.

- **Repository**: `GielW/DPO-Dashboard` (private)
- **License**: MIT
- **Language**: Python 3.11+
- **Status**: Phase 0 — Project Definition (architecture & specs complete)
- **Version**: 0.4.0

## Active Skills

This project uses:
- **Python** — FastAPI, SQLAlchemy, Pydantic, Jinja2, pytest
- **Obsidian vault** — MOCs for project, architecture, legal, modules, security
- **Belgian legal** — GDPR, GBA/APD, NIS2, CyberFundamentals
- **CI/CD** — GitHub Actions security pipeline (pip-audit, trivy, SBOM)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI 0.100+ |
| Frontend (Phase 1) | Streamlit 1.30+ |
| Frontend (Phase 2) | React + TypeScript |
| Database (dev) | SQLite |
| Database (prod) | PostgreSQL 15+ |
| ORM | SQLAlchemy 2.0+ (async) |
| Migrations | Alembic 1.12+ |
| Validation | Pydantic 2.0+ |
| Reports | WeasyPrint (PDF), python-docx, python-pptx |
| Templates | Jinja2 3.1+ |
| Charts | Plotly / matplotlib |

## Module Reference

| ID | Module | Description |
|----|--------|-------------|
| FR-001 | Dashboard | Compliance overview, KPIs, quick actions |
| FR-002 | DPIA Engine | Impact assessment lifecycle |
| FR-003 | Breach Register | Incident logging, 72h tracker, GBA notification |
| FR-004 | Vendor Assessment | Third-party risk scoring |
| FR-005 | Report Generator | McKinsey-style, PDF/DOCX/PPTX |
| FR-006 | GDPR Mapper | Article compliance checker |
| FR-007 | Cybersecurity | NIST/ISO 27001/CIS/NIS2 posture |
| FR-008 | Art. 30 Register | Processing activities management |
| FR-009 | Belgian Regulatory | GBA/APD references, Belgian law |
| FR-010 | Data Management | Storage, backup, encryption, auth |
| FR-011 | Agreements | DPA/JCA/SCC/NDA generator with clause library |
| FR-012 | Data Retention | Retention policies, schedules, deletion workflows |
| FR-013 | Advice Reports | DPO advice documents, recommendations, follow-up tracking |
| FR-014 | CVE Tracker | Vulnerability register, NVD/MITRE feeds, remediation |
| FR-015 | Dependency Scan | Project security scanning (pip-audit, trivy), SBOM, CI/CD |

## Key Design Principles

1. **Local-first**: No cloud dependency. All data stored locally. No telemetry.
2. **Belgian regulatory focus**: GBA/APD guidelines, Belgian DPA Act, CyberFundamentals, NIS2.
3. **Multi-language**: Dutch (NL), French (FR), English (EN) — all user-facing text.
4. **Modular architecture**: Each module is independent and testable in isolation.
5. **Report quality**: McKinsey Pyramid Principle — lead with the answer, structured arguments.
6. **Security by design**: Encryption at rest (optional SQLCipher), audit trail, no external data.

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/security-scan.yml`): push to `main`, PRs, weekly Monday 06:00 UTC.

| Job | Tools | Output |
|-----|-------|--------|
| Dependency Scan | pip-audit, safety | JSON + readable text |
| Trivy Scan | trivy filesystem | SARIF + JSON + table |
| Security Report | Python aggregator | security-report.txt + security-summary.json |
| SBOM Generation | cyclonedx-bom | CycloneDX JSON (main push only) |

## Linked Files Checklist

| File | What to update |
|------|---------------|
| `docs/progress/PROGRESS.md` | Task status, commit count, CI status |
| `CHANGELOG.md` | Entry under `[Unreleased]` |
| `docs/project-definition/02-FUNCTIONAL-REQUIREMENTS.md` | FR spec changes |
| `docs/obsidian/modules/FR-0XX *.md` | Module note updates |
| `docs/obsidian/MOC - Modules.md` | Module table |
| `README.md` | Features, structure, version |

## Current Phase

**Phase 0** — Project Definition ✅  
**Next**: Phase 1 — Core Dashboard (database models, Streamlit skeleton, data layer, DPIA screening, PDF reports)

## Important Notes

- **Private repository** — do not expose sensitive regulatory interpretations
- Tool must **comply with GDPR itself** (data minimisation, purpose limitation)
- Reports follow **McKinsey Pyramid Principle** (situation → complication → resolution)
- Agreements always include **mandatory Art. 28 GDPR clauses**
