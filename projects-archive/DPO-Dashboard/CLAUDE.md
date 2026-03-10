# CLAUDE.md — Project Context for Claude Code

This file provides context for AI-assisted development sessions on the **DPO Dashboard** project.
It is read automatically by Claude Code at the start of each session.

---

## Project Overview

**DPO/DPA Cybersecurity & Compliance Dashboard** — a comprehensive, local-first, open-source dashboard for Data Protection Officers operating under Belgian and EU data protection law.

- **Owner**: Giel W. (DPO/DPA & Cybersecurity Enthusiast, Belgium)
- **Repository**: `GielW/DPO-Dashboard` (private)
- **License**: MIT
- **Language**: Python 3.11+
- **Status**: Phase 0 — Project Definition (architecture & specs complete)
- **Version**: 0.5.0

---

## Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | **FastAPI** 0.100+ | REST API, async |
| Frontend (Phase 1) | **Streamlit** 1.30+ | Rapid prototyping |
| Frontend (Phase 2) | **React + TypeScript** | Production SPA |
| Database (dev) | **SQLite** | Local file-based |
| Database (prod) | **PostgreSQL** 15+ | Multi-user |
| ORM | **SQLAlchemy** 2.0+ | Async support |
| Migrations | **Alembic** 1.12+ | Schema versioning |
| Validation | **Pydantic** 2.0+ | Data models |
| PDF reports | **WeasyPrint** 60+ | HTML/CSS → PDF |
| DOCX reports | **python-docx** 1.0+ | Word generation |
| PPTX reports | **python-pptx** 0.6+ | PowerPoint generation |
| Templates | **Jinja2** 3.1+ | Report templates |
| Charts | **Plotly** / **matplotlib** | Visualisations |
| Auth | **bcrypt** | Local password hashing |
| Logging | **loguru** | Structured logging |
| Linting | **ruff** | Fast Python linter |
| Formatting | **black** | Code formatting |
| Type checking | **mypy** (strict) | Static type analysis |
| Testing | **pytest** + pytest-cov | Test suite |

---

## Project Structure

```
DPO-Dashboard/
├── .github/
│   ├── workflows/
│   │   └── security-scan.yml      # CI: pip-audit, safety, trivy, SBOM, security report
│   ├── dependabot.yml             # Auto-dependency updates
│   └── ISSUE_TEMPLATE/            # GitHub issue templates
│
├── .obsidian/                     # Obsidian vault configuration
│   ├── app.json                   # Vault settings (wikilinks, attachments folder)
│   ├── appearance.json            # Theme & font settings
│   ├── core-plugins.json          # Enabled core plugins
│   ├── community-plugins.json     # Community plugin list
│   ├── graph.json                 # Graph view colour groups by tag
│   ├── hotkeys.json               # Custom keybindings
│   ├── templates.json             # Template folder config
│   └── templates/                 # Note templates
│       ├── Module Note.md         # Template for new FR module notes
│       └── General Note.md        # Template for general notes
│
├── docs/
│   ├── obsidian/                  # Obsidian knowledge graph layer
│   │   ├── 000 - Vault Index.md   # Main entry point (start here)
│   │   ├── MOC - Project.md       # Map of Content: project management
│   │   ├── MOC - Architecture.md  # Map of Content: tech stack & design
│   │   ├── MOC - Legal & GDPR.md  # Map of Content: legal references
│   │   ├── MOC - Modules.md       # Map of Content: all 15 FR modules
│   │   ├── MOC - Security.md      # Map of Content: CVE, scanning, security
│   │   └── modules/               # Individual module notes (FR-001..FR-015)
│   │       ├── FR-001 Dashboard.md
│   │       ├── FR-002 DPIA Engine.md
│   │       ├── FR-003 Breach Register.md
│   │       ├── FR-004 Vendor Assessment.md
│   │       ├── FR-005 Report Generator.md
│   │       ├── FR-006 GDPR Mapper.md
│   │       ├── FR-007 Cybersecurity.md
│   │       ├── FR-008 Art 30 Register.md
│   │       ├── FR-009 Belgian Regulatory.md
│   │       ├── FR-010 Data Management.md
│   │       ├── FR-011 Agreements.md
│   │       ├── FR-012 Data Retention.md
│   │       ├── FR-013 Advice Reports.md
│   │       ├── FR-014 CVE Tracker.md
│   │       └── FR-015 Dependency Scan.md
│   ├── project-definition/        # Project specs
│   │   ├── 01-PROJECT-CHARTER.md
│   │   ├── 02-FUNCTIONAL-REQUIREMENTS.md
│   │   ├── 03-TECHNICAL-ARCHITECTURE.md
│   │   ├── 04-MCKINSEY-REPORT-FRAMEWORK.md
│   │   └── 05-BELGIAN-REGULATORY-CONTEXT.md
│   ├── research/                  # Competitive & market analysis
│   │   └── 06-COMPETITIVE-LANDSCAPE.md
│   ├── progress/                  # Project tracking
│   │   └── PROGRESS.md
│   ├── architecture/              # ADRs, diagrams
│   ├── templates/                 # Document templates
│   ├── legal-references/          # GDPR text, GBA guidelines
│   └── attachments/               # Obsidian file attachments
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Application entry point
│   ├── dashboard/                 # Streamlit/React frontend
│   ├── analysis/                  # Analysis modules
│   │   ├── gdpr/                  #   GDPR compliance
│   │   ├── risk/                  #   Risk assessment
│   │   ├── breach/                #   Breach analysis
│   │   ├── dpia/                  #   DPIA engine
│   │   ├── vendor/                #   Vendor assessment
│   │   └── cybersecurity/         #   Cyber posture (NIST/ISO/NIS2)
│   ├── agreements/                # Agreement generator & management
│   │   ├── templates/             #   Agreement templates (DPA, JCA, SCC)
│   │   ├── clauses/               #   Reusable clause library
│   │   ├── generators/            #   Document generators
│   │   └── validators/            #   Art. 28 compliance validators
│   ├── retention/                 # Data retention management
│   │   ├── policies/              #   Retention policy engine
│   │   ├── schedules/             #   Retention schedule & calendar
│   │   ├── references/            #   Statutory retention periods DB
│   │   └── workflows/             #   Deletion & anonymisation workflows
│   ├── advice/                    # DPO advice reports (Art. 39)
│   │   ├── intake/                #   Advice request intake
│   │   ├── builder/               #   Advice document builder
│   │   ├── templates/             #   Category-specific templates
│   │   ├── clauses/               #   Reusable paragraph library
│   │   └── tracking/              #   Recommendation follow-up
│   ├── cve/                       # CVE tracker & vulnerability management
│   │   ├── register/              #   CVE register & asset inventory
│   │   ├── feeds/                 #   NVD, MITRE, EPSS data fetchers
│   │   ├── scanner/               #   Dependency & project scanning
│   │   ├── assessment/            #   Risk & data protection impact
│   │   └── remediation/           #   Remediation workflows
│   ├── reports/                   # Report generation engine
│   │   ├── generators/            #   Report type generators
│   │   ├── templates/             #   Jinja2/HTML templates
│   │   └── output/                #   Generated reports (gitignored)
│   ├── data/                      # Data layer
│   │   ├── models/                #   SQLAlchemy ORM models
│   │   ├── repositories/          #   Repository pattern (CRUD)
│   │   └── migrations/            #   Alembic migration scripts
│   ├── utils/                     # Shared utilities
│   └── integrations/              # External integrations
│
├── tests/                         # Test suite (pytest)
├── config/                        # Configuration
│   ├── __init__.py
│   └── settings.py                # App settings & env loading
├── scripts/
│   └── download-security-report.sh  # Download CI security report
│
├── pyproject.toml                 # Python project config & dependencies
├── CHANGELOG.md                   # Version history
├── CLAUDE.md                      # This file — AI assistant context
├── CONTRIBUTING.md                # Dev setup, coding standards, commit conventions
├── README.md                      # Project overview & getting started
├── LICENSE                        # MIT License
├── .env.example                   # Environment variable template
└── .gitignore                     # Git ignore rules
```

---

## Obsidian Knowledge Vault

The project doubles as an **Obsidian vault**. Open the repo root (`DPO-Dashboard/`) as a vault in Obsidian to browse the full knowledge graph.

### Vault Entry Point
Open `docs/obsidian/000 - Vault Index.md` — this links to all 5 Maps of Content (MOCs).

### Maps of Content (MOCs)
| MOC | Purpose |
|-----|--------|
| `MOC - Project` | Roadmap, charter, progress, changelog |
| `MOC - Architecture` | Tech stack, design patterns, ADRs |
| `MOC - Legal & GDPR` | Belgian law, GDPR articles, regulatory bodies |
| `MOC - Modules` | All 15 FR modules with implementation status |
| `MOC - Security` | CVE tracking, CI/CD pipeline, security by design |

### Module Notes
`docs/obsidian/modules/FR-001 Dashboard.md` through `FR-015 Dependency Scan.md` — one note per functional requirement with:
- YAML frontmatter (`tags`, `aliases`, `fr`, `status`, `phase`, `source`)
- Cross-module `[[wikilinks]]`
- Legal basis references
- Navigation back to MOC and Vault Index

### Graph View Colour Groups
| Tag | Colour | Content |
|-----|--------|--------|
| `#project-definition` | Green | Charter, requirements, specs |
| `#module` | Purple | FR-001 to FR-015 module notes |
| `#architecture` | Orange | Tech stack, design, patterns |
| `#belgian-law` | Red | GBA/APD, Belgian DPA Act, NIS2 |
| `#security` | Red | CVE, scanning, encryption |
| `#moc` | Cyan | Maps of Content (index pages) |

### Obsidian Conventions
- All markdown files have **YAML frontmatter** with `tags`, `aliases`, `created`
- Cross-references use **Obsidian wikilinks**: `[[path/to/note|Display Text]]`
- Attachments go in `docs/attachments/`
- New module notes: use template **Insert Template → Module Note**
- New general notes: use template **Insert Template → General Note**
- `.obsidian/workspace.json` is gitignored (user-specific layout)
- `.obsidian/plugins/` and `.obsidian/themes/` are gitignored (user-specific)

### Tags
Use these tags consistently across all notes:
`#project-definition` `#module` `#architecture` `#belgian-law` `#gdpr` `#security` `#report` `#moc` `#dashboard` `#dpia` `#breach` `#vendor` `#research`

---

## Key Design Principles

1. **Local-first**: No cloud dependency. All data stored locally. No telemetry.
2. **Belgian regulatory focus**: GBA/APD guidelines, Belgian DPA Act, CyberFundamentals, NIS2.
3. **Multi-language**: Dutch (NL), French (FR), English (EN) — all user-facing text.
4. **Modular architecture**: Each module is independent and testable in isolation.
5. **Report quality**: McKinsey Pyramid Principle — lead with the answer, structured arguments.
6. **Security by design**: Encryption at rest (optional SQLCipher), audit trail, no external data.

---

## Coding Conventions

### Python Style
- **Line length**: 120 characters (configured in ruff & black)
- **Target**: Python 3.11+
- **Type hints**: Required on all functions (mypy strict mode)
- **Docstrings**: Google-style docstrings on all public functions/classes
- **Imports**: Sorted by ruff (isort compatible)

### Naming
- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: Prefix with `_` (single underscore)

### Architecture Patterns
- **Repository pattern** for data access (`src/data/repositories/`)
- **Service layer** for business logic
- **Pydantic models** for API request/response schemas
- **SQLAlchemy models** for database entities
- **Jinja2 templates** for reports
- **Dependency injection** via FastAPI's `Depends()`

### Testing
- Test files: `tests/test_<module>.py`
- Use `pytest` fixtures for setup
- Aim for 80%+ coverage on business logic
- Use `httpx.AsyncClient` for API tests

---

## Project Setup

### Prerequisites
- Python 3.11+
- Git
- pip or uv package manager
- GitHub CLI (`gh`) — for security report downloads
- Obsidian (optional) — for knowledge vault browsing

### First-Time Setup

```bash
# 1. Clone the repository
git clone https://github.com/GielW/DPO-Dashboard.git
cd DPO-Dashboard

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate          # Windows

# 3. Install all dependencies (including dev tools)
pip install -e ".[dev]"

# 4. Copy environment configuration
cp .env.example .env
# Edit .env with your settings

# 5. Verify installation
python -m src.main              # Should start without errors
ruff check src/                 # Should pass linting
pytest                          # Should discover test suite
```

### Obsidian Setup
1. Install [Obsidian](https://obsidian.md)
2. **Open folder as vault** → select the `DPO-Dashboard/` repo root
3. Navigate to `docs/obsidian/000 - Vault Index.md`
4. Press **Ctrl+G** (or Cmd+G) for the graph view
5. Vault config is pre-committed — graph colours, plugins, and templates are ready

---

## Common Commands

```bash
# Run application
python -m src.main                    # Entry point
uvicorn src.api:app --reload          # FastAPI dev server (when API exists)
streamlit run src/dashboard/app.py    # Streamlit dashboard (when exists)

# Code quality
ruff check src/ tests/                # Lint
ruff check src/ tests/ --fix          # Lint + auto-fix
black src/ tests/                     # Format
mypy src/                             # Type check

# Security scanning
pip-audit                             # Scan Python deps for CVEs
trivy fs .                            # Scan project files for vulnerabilities
./scripts/download-security-report.sh # Download latest CI security report

# Testing
pytest                                # Run all tests
pytest -x                             # Stop on first failure
pytest --cov=src --cov-report=html    # With coverage report
pytest -k "test_dpia"                 # Run specific tests

# Database (when Alembic is configured)
alembic upgrade head                  # Apply migrations
alembic revision --autogenerate -m "description"  # Create migration

# Git
git add -A && git status              # Stage & review
git commit -m "feat: description"     # Commit (conventional commits)
git push origin main                  # Push
```

---

## Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

<optional body>
```

| Type | Use for |
|------|---------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Code change that neither fixes nor adds |
| `test` | Adding/updating tests |
| `chore` | Maintenance (deps, CI, config) |
| `style` | Formatting, no logic change |

**Scopes**: `dashboard`, `dpia`, `breach`, `vendor`, `reports`, `agreements`, `retention`, `advice`, `cve`, `scan`, `data`, `auth`, `config`, `docs`

---

## Module Reference (Functional Requirements)

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
| FR-014 | CVE Tracker | Vulnerability register, NVD/MITRE feeds, remediation, data protection impact |
| FR-015 | Dependency Scan | Project security scanning (pip-audit, trivy), SBOM, CI/CD |

---

## Belgian Regulatory Context

Key Belgian laws and bodies to reference:
- **GBA/APD**: Gegevensbeschermingsautoriteit / Autorité de protection des données
- **Belgian DPA Act**: Wet van 30 juli 2018
- **Camera Act**: Camerawet (surveillance footage max 1 month)
- **Social law**: Employment records 5 years post-contract
- **Tax code**: 7-year retention for tax/accounting documents
- **CCB CyberFundamentals**: Belgian cybersecurity framework (Basic/Important/Essential)
- **NIS2 Belgian transposition**: Critical infrastructure requirements

---

## Current Phase & Next Steps

**Current**: Phase 0 — Project Definition ✅
**Next**: Phase 1 — Core Dashboard

Phase 1 priorities:
1. Set up database models (SQLAlchemy) and Alembic migrations
2. Build Streamlit dashboard skeleton with navigation
3. Implement data layer (repositories, CRUD operations)
4. Create first analysis module (DPIA screening)
5. Build basic report generation (PDF output)

---

## Documentation Style

### Markdown Conventions
- All docs use **YAML frontmatter**: `tags`, `aliases`, `created` (for Obsidian metadata)
- Use **Obsidian wikilinks** in `docs/obsidian/` notes: `[[path/to/note|Display Text]]`
- Use **standard markdown links** in root-level files (README, CONTRIBUTING, CHANGELOG) for GitHub compatibility
- Headers: `# Title` → `## Section` → `### Subsection` (max 3 levels in most docs)
- Tables for structured data; code blocks with language hints (```python, ```bash)
- Emoji in headers for visual navigation (📋 📦 🔒 ⚖️ etc.)

### Documentation Structure
| File / Folder | Purpose | Audience |
|---|---|---|
| `README.md` | Project overview, getting started | New visitors, GitHub |
| `CLAUDE.md` | AI assistant context (this file) | Claude Code / AI sessions |
| `CONTRIBUTING.md` | Dev setup, commit conventions | Contributors |
| `CHANGELOG.md` | Version history (Keep a Changelog) | All stakeholders |
| `docs/project-definition/` | Formal specs (charter, FRs, architecture) | Project planning |
| `docs/research/` | Market research, competitive analysis | Strategic decisions |
| `docs/progress/PROGRESS.md` | Phase tracking, milestones | Project management |
| `docs/obsidian/` | Knowledge graph (MOCs, module notes) | Obsidian browsing |
| `docs/obsidian/modules/` | One note per FR with cross-links | Knowledge exploration |

### Version Numbering
- Follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`
- Current: `0.4.0` (Phase 0 — definition complete)
- Bump version in: `pyproject.toml`, `CHANGELOG.md`, `CLAUDE.md`, project charter, PROGRESS.md

### Changelog Format
- Follow [Keep a Changelog](https://keepachangelog.com/) format
- Sections: Added, Changed, Deprecated, Removed, Fixed, Security
- Reference FR-IDs and commit scopes in entries

---

## CI/CD & Security Pipeline

GitHub Actions workflow (`.github/workflows/security-scan.yml`) runs on:
- Every push to `main`
- Every PR targeting `main`
- Weekly schedule (Monday 06:00 UTC)

| Job | Tools | Output |
|-----|-------|--------|
| Dependency Scan | pip-audit, safety | JSON + readable text |
| Trivy Scan | trivy filesystem | SARIF + JSON + table |
| Security Report | Python aggregator | `security-report.txt` + `security-summary.json` |
| SBOM Generation | cyclonedx-bom | CycloneDX JSON (main push only) |

All outputs are uploaded as **GitHub Actions artifacts** (90-day retention).
The Security Report job posts a summary with a **🟢 ALL CLEAR / 🔴 ACTION REQUIRED** verdict to the GitHub Actions step summary.

**Download locally**: `./scripts/download-security-report.sh [run-id]`

---

## After Every Change — Project File Update Checklist

**Always update the following project files when making changes.** This is mandatory — do not commit without checking each item.

### On Every Commit
- [ ] **`docs/progress/PROGRESS.md`** — Update task status, mark items done, update commit count, file counts, CI status
- [ ] **`CHANGELOG.md`** — Add entry under `[Unreleased]` with the correct section (Added/Changed/Fixed/Security)
- [ ] **Commit message** — Follow Conventional Commits: `<type>(<scope>): <description>`

### On Version Bump
- [ ] **`pyproject.toml`** — Update `version`
- [ ] **`CHANGELOG.md`** — Move `[Unreleased]` entries to new version heading with date
- [ ] **`CLAUDE.md`** — Update version in Project Overview
- [ ] **`docs/project-definition/01-PROJECT-CHARTER.md`** — Update version
- [ ] **`docs/progress/PROGRESS.md`** — Update version, add to Version History table

### On New Module or Feature
- [ ] **`docs/project-definition/02-FUNCTIONAL-REQUIREMENTS.md`** — Add/update FR spec
- [ ] **`docs/progress/PROGRESS.md`** — Add to Module Implementation Status table, update Phase tasks
- [ ] **`docs/obsidian/modules/FR-0XX *.md`** — Create module note (use Obsidian template)
- [ ] **`docs/obsidian/MOC - Modules.md`** — Add entry to module table
- [ ] **`CLAUDE.md`** — Add to Module Reference table
- [ ] **`README.md`** — Add to Key Features table and Project Structure tree

### On Architecture or Design Change
- [ ] **`docs/project-definition/03-TECHNICAL-ARCHITECTURE.md`** — Update affected sections
- [ ] **`docs/progress/PROGRESS.md`** — Add to Decision Log
- [ ] **`docs/obsidian/MOC - Architecture.md`** — Update if stack/patterns changed
- [ ] **`CLAUDE.md`** — Update Tech Stack table or Design Principles if affected

### On CI/CD or Security Change
- [ ] **`docs/progress/PROGRESS.md`** — Update CI/CD Pipeline Status table
- [ ] **`docs/obsidian/MOC - Security.md`** — Update pipeline table
- [ ] **`CLAUDE.md`** — Update CI/CD & Security Pipeline section

### On New Obsidian Note
- [ ] Add **YAML frontmatter** (`tags`, `aliases`, `created`)
- [ ] Add **`[[wikilink]]` navigation** (back to MOC and Vault Index)
- [ ] Use **consistent tags** from the approved tag list
- [ ] Update the **relevant MOC** with a link to the new note

---

## Important Notes

- This is a **private repository** — do not expose sensitive regulatory interpretations
- All data in the tool is **locally stored** — never suggest cloud storage
- The tool must **comply with GDPR itself** (data minimisation, purpose limitation)
- Belgian legal references should always cite the **source law/article**
- Reports should follow **McKinsey Pyramid Principle** (situation → complication → resolution)
- When generating agreements, always include **mandatory Art. 28 GDPR clauses**
- When adding new Obsidian notes, always include **YAML frontmatter** and **wikilink navigation**
- Keep both Obsidian wikilinks (in vault notes) and standard markdown links (in root docs) working
