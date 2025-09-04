# Contributing to cline_project_template

This template enforces clean architecture, strong typing, high‑quality tests, and security‑by‑default. To avoid documentation drift, the canonical contribution guide lives in the documentation site.

Please read the full guide here:
- docs/contributing.md (in this repository)

Quick links:
- Architecture overview: docs/architecture.md
- Security policy (developer guidance): docs/security.md
- Root security disclosure and contacts: SECURITY.md
- Project brief template: memory-bank/projectbrief.md
- Architecture and quality policies: .clinerules/

Local workflow (summary):
1) Create a virtual environment and install dev extras:
   ```
   python3.11 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   pre-commit install
   ```
2) Run quality gates and tests before pushing:
   ```
   pre-commit run --all-files
   pytest --cov=src --cov-report=term-missing
   ```

For detailed standards (branch naming, Conventional Commits, typing, testing strategy, PR checklist), see docs/contributing.md. This file intentionally remains a short pointer to prevent duplication.
