# cline_project_template

Production‑grade Python template enforcing elegance, modularity, Pythonic best practices, and clean architecture. This template encodes architectural and quality standards via tooling (pre‑commit), CI, docs, and governance so every new repo starts strong and remains consistent.

- Clean Architecture: domain → application → adapters → infrastructure (no reverse imports)
- Python 3.11+, strict typing (mypy), docstrings, property‑based tests (Hypothesis)
- Automated quality gates: Black, Ruff (incl. D docstring rules), isort, mypy, interrogate, Bandit, detect‑secrets, import‑linter, coverage ≥ 90%
- CI: quality gates, tests with coverage artifacts, security scans (pip‑audit, Bandit), docs build (MkDocs)
- Docs: MkDocs Material with quickstart, architecture, contributing, and security pages
- License Propagation Safeguard: prevents template LICENSE from leaking into downstream private repos

Repository layout (src/)

- src/cline_project_template/
  - domain: pure business logic (entities, value objects, services, errors)
  - application: use cases/orchestrators, depends on domain only
  - adapters: inbound (CLI/HTTP) wrappers and outbound protocol implementations
  - infrastructure: concrete gateways/clients (DB, HTTP); no inward leaks
  - config: typed settings via Pydantic Settings (env‑driven)
  - shared: layer‑agnostic utilities
  - cli: click‑based CLI group and subcommands

Quickstart

1) Create and activate a virtual environment:
   ```
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

2) Install the project in editable mode with dev extras:
   ```
   pip install -e ".[dev]"
   ```

3) Install pre‑commit hooks:
   ```
   pre-commit install
   ```

4) Run all quality checks:
   ```
   pre-commit run --all-files
   ```

5) Run tests with coverage:
   ```
   pytest --cov=src --cov-report=term-missing
   ```

6) Optional: configure environment
   - Copy .env.example to .env and adjust values. Never commit .env.

CLI usage

After installing, explore the CLI:

```
python -m cline_project_template.cli.main --help
python -m cline_project_template.cli.main example 7 "Seven"

# Console script (installed as entry point)
cline-template-cli --help
cline-template-cli example 7 "Seven"
```

Architecture and contracts

- Boundaries enforced by import‑linter contracts (importlinter.ini).
- Domain must not import application/adapters/infrastructure.
- Application must not import adapters/infrastructure.
- Adapters and infrastructure must not import domain directly.
- See docs/architecture.md for details.

Docs (MkDocs Material)

- Local build:
  ```
  mkdocs build --strict
  ```
- Local serve:
  ```
  mkdocs serve
  ```
- Navigation: Home, Architecture, Contributing, Security.

Security policy

- No secrets in code or configs; .env is ignored; .env.example documents variables.
- Pre‑commit and CI run Bandit, detect‑secrets, and pip‑audit.
- See SECURITY.md and docs/security.md.

Contributing

- Follow Conventional Commits, strict typing, and test coverage (≥90%).
- See CONTRIBUTING.md and docs/contributing.md for setup, standards, and PR checklist.

Release workflow

- Versioning managed by bumpver (PEP 440).
- On pushing a tag vX.Y.Z, .github/workflows/release.yml builds and attempts to publish to PyPI via Trusted Publishing (fallback to Twine if credentials provided).
- Maintain CHANGELOG.md in Keep a Changelog format.

License propagation policy (downstream reminder)

If you use this as a template to create a new repository:
- Remove or replace LICENSE in the new repository before the first commit.
- Update that repo’s README to reflect the chosen license (or “All rights reserved” if private).
- A pre‑commit hook (scripts/check_license.py) enforces this policy; pyproject includes a fingerprint of this template’s LICENSE for detection.

Using with Cline and the Memory Bank

- Fill memory-bank/projectbrief.md before coding (Cline reads it first).
- .clinerules/ codifies architecture, testing, security, and governance standards; CI and hooks enforce these automatically.
- This template is designed to work smoothly with Cline’s Plan/Act workflows.

References (selected)

- Packaging and structure: https://packaging.python.org/
- Hypermodern Python template: https://github.com/cjolowicz/cookiecutter-hypermodern-python
- Ruff: https://docs.astral.sh/ruff/
- mypy: https://mypy.readthedocs.io/
- import‑linter: https://import-linter.readthedocs.io/
- pre‑commit: https://pre-commit.com/
- pytest: https://docs.pytest.org/
- Hypothesis: https://hypothesis.readthedocs.io/
- Bandit: https://bandit.readthedocs.io/
- pip‑audit: https://pypi.org/project/pip-audit/
- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
- Conventional Commits: https://www.conventionalcommits.org/
- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
