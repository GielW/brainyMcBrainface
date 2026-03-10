---
name: python
description: Python-specific style, tooling, architecture patterns, and project setup. Activate for any project using Python — covers ruff, black, mypy, pytest, virtual environments, and import conventions.
---

# Python — Language Skill

> Activate for projects using Python (e.g., DPO-Dashboard).

## Style

- **Line length**: 120 characters
- **Target**: Python 3.11+
- **Type hints**: Required on all functions (`mypy` strict mode)
- **Docstrings**: Google-style on all public functions/classes

```python
def calculate_risk(score: float, weight: float = 1.0) -> RiskLevel:
    """Calculate weighted risk level.

    Args:
        score: Raw risk score (0.0–10.0).
        weight: Multiplier for score adjustment.

    Returns:
        The computed RiskLevel enum value.

    Raises:
        ValueError: If score is outside valid range.
    """
```

## Tools

| Tool | Purpose | Command |
|------|---------|---------|
| `ruff` | Linting (replaces flake8, isort, pyflakes) | `ruff check src/ tests/` |
| `ruff --fix` | Auto-fix lint issues | `ruff check src/ tests/ --fix` |
| `black` | Code formatting | `black src/ tests/` |
| `mypy` | Static type checking | `mypy src/` |
| `pytest` | Test runner | `pytest` |
| `pytest-cov` | Coverage | `pytest --cov=src --cov-report=html` |
| `pip-audit` | Security scanning | `pip-audit` |

## Architecture Patterns

- **Repository pattern** for data access (`src/data/repositories/`)
- **Service layer** for business logic
- **Pydantic models** for API request/response schemas
- **SQLAlchemy models** for database entities
- **Jinja2 templates** for reports
- **Dependency injection** via FastAPI's `Depends()`

## Project Setup Pattern

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
```

## Imports

```python
# 1. Standard library
import os
from pathlib import Path

# 2. Third-party
from fastapi import FastAPI, Depends
from pydantic import BaseModel

# 3. Local
from src.data.models import User
from src.services.auth import AuthService
```
