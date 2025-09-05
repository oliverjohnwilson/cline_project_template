# Contributing

Thank you for considering a contribution. This template encodes strict quality and architecture standards so downstream repos stay elegant and maintainable.

- Clean architecture (domain → application → adapters → infrastructure)
- Python 3.11+, strict typing, docstrings, high-quality tests
- Automated quality gates via pre-commit and CI
- Security-first defaults (no secrets in code; scans enabled)

Use this file as the canonical contribution guide for the docs site. A short root-level CONTRIBUTING.md should link here.

## Development setup

1) Create and activate a virtual environment (recommended):
```
python3.11 -m venv .venv
source .venv/bin/activate
```

2) Install the project in editable mode with dev extras:
```
pip install -e ".[dev]"
```

3) Install pre-commit hooks:
```
pre-commit install
```

4) Run all quality checks locally before pushing:
```
pre-commit run --all-files
pytest --cov=src --cov-report=term-missing
```

Environment configuration (optional):
- Copy `.env.example` to `.env` and adjust values.
- Never commit `.env` (covered by .gitignore).

See .env.example at the repository root.

## Branching and commits

- Branch naming: `feat/<slug>`, `fix/<slug>`, `chore/<slug>`, `docs/<slug>`, etc.
- Conventional Commits enforced (commitizen hook available):
  - `feat: add X`
  - `fix: correct Y`
  - `docs: update Z`
  - `refactor:`, `test:`, `build:`, `ci:`, `chore:`, `perf:`
- Keep commits focused and PRs small; link issues with “Fixes #123” when applicable.

## Architecture and boundaries

- Dependencies flow inward only:
  - domain → application → adapters → infrastructure (no reverse imports)
- Domain is pure: no I/O, framework imports, or side effects.
- Application orchestrates use cases; depends on abstractions (Protocols/ABCs).
- Adapters translate protocols (inbound/outbound).
- Infrastructure holds concrete gateways/clients; must not import domain.

Architecture contracts are enforced by import-linter:
```
lint-imports -c importlinter.ini
```

## Coding standards

- Style/formatting: Black (line length 100), isort (Black profile), Ruff (lint)
- Typing: mypy strict; no implicit Any in public APIs
- Docstrings: PEP 257 (Google style), aim for ≥90% docstring coverage via `interrogate`
- Security: Bandit (SAST), detect-secrets; see Security policy

Run locally:
```
pre-commit run --all-files
mypy
pytest --cov=src --cov-report=term-missing
```

## Testing strategy

- Unit tests deterministic and fast; prioritize coverage of domain and pure logic
- Property-based tests (Hypothesis) for invariants and pure functions
- Integration tests at adapter boundaries (e.g., use case + repository)
- E2E tests for critical flows (e.g., CLI)

Coverage target: ≥ 90% overall; domain trending to 100%.

## Documentation

- Update docstrings when changing public APIs.
- Update docs under `docs/` and `mkdocs.yml` navigation as needed.
- `mkdocs build` (CI builds docs; warnings should be treated as errors in CI).

## Security expectations

- Never commit secrets; `.env.example` shows required variables without values.
- Redact sensitive data in logs. Prefer safe serializers; avoid `pickle`.
- Security scans (Bandit, pip-audit, detect-secrets) must be clean or risk-accepted with mitigation.

## Releases

- Versioning managed by `bumpver` (PEP 440). On tag `vX.Y.Z`, release workflow can publish to PyPI (requires project configuration).
- Follow Keep a Changelog format in `CHANGELOG.md`.

## Cline and the Memory Bank

- For new downstream projects, complete `memory-bank/projectbrief.md` before coding.
- Cline reads the brief first and adheres to `.clinerules/`.

## Pull request checklist

- [ ] Code respects architecture boundaries and contracts pass
- [ ] Pre-commit hooks pass locally
- [ ] Types, style, docs checks pass (mypy, Ruff D, interrogate)
- [ ] Tests added/updated; coverage ≥ 90%
- [ ] Security scans green or justified
- [ ] Docs/README updated where visible behavior changed
