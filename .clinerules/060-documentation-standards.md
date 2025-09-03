# 060 – Documentation Standards

## Purpose
Keep documentation accurate, actionable, and aligned with the code as it evolves.

## Objectives
- Discoverable setup and usage.
- Public APIs documented at the source.
- Runnable examples to eliminate ambiguity.

## Non‑negotiable rules
- README first: includes purpose, quickstart, architecture overview, licensing note, and contribution guidelines.
- Docstrings: required for all public APIs per PEP 257; choose Google or NumPy style consistently.
- Examples: runnable snippets where feasible; examples must reflect tested behavior.
- Docs site (optional but recommended): build from docs/ in CI; warnings are errors.

## Enforcement
- Pre‑commit: pydocstyle + interrogate (≥ 90% docstring coverage).
- CI: docs build job (if enabled) fails on warnings or broken links.
- PR: any visible behavior change must include doc updates.

## Cline directives
- Must include docstrings and brief examples when creating public APIs.
- Must update README and docs sections when introducing new capabilities.
- Must not leave TODOs or placeholders in public docs.

## Checklist
- [ ] README reflects current capabilities and constraints.
- [ ] Docstrings present and consistent (≥ 90% coverage).
- [ ] Examples runnable and aligned with tests.
