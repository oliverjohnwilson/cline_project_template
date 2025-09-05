# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog (https://keepachangelog.com/en/1.1.0/), 
and this project adheres to PEP 440 for versioning.

## [Unreleased]

### Added
- Pre-commit configuration with Black, Ruff, isort, mypy, pydocstyle, interrogate, Bandit, detect-secrets, import-linter, commitizen, and license-propagation check.
- Architecture import contracts via import-linter (importlinter.ini) and hook integration.
- CI workflow (GitHub Actions) with quality gates, tests+coverage, docs build (MkDocs strict), and security scans (pip-audit, Bandit).
- Release workflow publishing to PyPI via Trusted Publishing (with Twine fallback).
- Dependabot configuration for pip and GitHub Actions.
- MkDocs Material documentation site: mkdocs.yml and docs/ (index, architecture, contributing, security).
- Community health files: CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md.
- .env.example at repository root (in addition to docs/env.example).
- README expanded with quickstart, architecture overview, security and Cline/Memory Bank usage notes.
- Runtime dependencies declared: click, pydantic, pydantic-settings.

### Changed
- settings.py updated to use pydantic-settings BaseSettings import for Pydantic v2.

### Security
- Enforced secret scanning (detect-secrets), SAST (Bandit), and dependency audit (pip-audit) in CI.
- License propagation policy wired to pre-commit and pyproject with LICENSE SHA-256 fingerprint.

## [0.1.0] - 2025-09-03
### Added
- Initial project structure with `src/` layout (domain, application, adapters, infrastructure, config, shared, cli).
- Example entity, use case, CLI adapter, in-memory repository.
- Test suite: unit, property-based (Hypothesis), integration, and E2E CLI tests.
- Scripts: dev.sh and release.sh.
- pyproject.toml with baseline tooling configuration.
