# 200 – Continuous Integration Standards

## Purpose
Automate enforcement of quality, security, and architectural constraints; publish useful artifacts.

## Objectives
- Mirror local checks in CI.
- Block merges on violations.
- Provide actionable feedback quickly.

## Non-negotiable rules
- Required jobs:
  - Pre-commit (black, ruff, isort, mypy strict, pydocstyle, interrogate, detect-secrets, bandit).
  - Tests with coverage ≥ 90% (domain trending to 100%).
  - Import contracts (architecture lints) pass.
  - Security audit (pip-audit) passes per severity policy.
  - Docs build (if enabled) succeeds with no warnings.
  - License propagation check passes.
- Matrix: run against all supported Python versions; Linux mandatory (macOS optional).
- Artifacts: coverage XML/HTML, docs preview, built wheels on tags.
- Caching: cache venv/pip appropriately to speed feedback, without compromising determinism.

## Enforcement
- Branch protection: all required jobs must pass before merge; no allow-failures for core gates.
- Fail fast: CI stops on first critical failure to shorten feedback cycles.

## Cline directives
- Must keep CI configuration minimal and explicit; avoid hidden steps.
- Must not propose disabling checks to pass CI; instead fix underlying issues.

## Checklist
- [ ] All required jobs pass; artifacts uploaded.
- [ ] Coverage meets threshold; no skipped tests.
- [ ] Security and architecture gates green.
