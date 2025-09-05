# 010 – Python Style and Typing

## Purpose
Ensure consistent, idiomatic, and maintainable Python with strong type safety and clear documentation.

## Objectives
- Uniform style and imports for readability and diffs.
- Strong typing to prevent defects and enable safe refactoring.
- Self-documenting public APIs via docstrings and examples.

## Non-negotiable rules
- Formatting: Black (line length 100). No manual alignment that fights the formatter.
- Linting: Ruff with core PEP 8 and bug-finding rules; treat warnings as work items, not to be silenced without cause.
- Imports: isort (Black profile); groups: stdlib, third-party, local; no wildcard imports; no circulars.
- Naming: Classes CapWords; functions/variables lower_snake_case; constants UPPER_SNAKE_CASE; modules lower_snake_case.
- Typing:
  - Public functions/methods fully typed; no implicit Any in public API.
  - Use `typing.Protocol` or `abc.ABC` for interfaces; prefer `dataclasses` for data.
  - Avoid `cast()` where possible; refactor to satisfy the checker.
- Docstrings:
  - PEP 257 required for public APIs.
  - Use Google or NumPy style; document params, returns, raises, and side effects.
  - Include minimal runnable examples when practical.
- Idioms:
  - Prefer f-strings; comprehensions where they improve clarity.
  - Avoid mutable default args; avoid deep nesting; extract helpers for clarity.

## Enforcement
- Pre-commit: black, ruff, isort, mypy (strict), pydocstyle, interrogate (docstring coverage ≥ 90%).
- CI: fails on any style/type/doc violation; coverage gates enforced.

## Cline directives
- Must output typed, PEP 8–compliant code and docstrings by default.
- Must propose interfaces (Protocols/ABCs) where cross-layer boundaries exist.
- Must not recommend adding ignore-comments to silence genuine issues without justification.

## Checklist
- [ ] Black, Ruff, isort clean.
- [ ] mypy strict passes; no public Any.
- [ ] Public APIs have complete docstrings (≥ 90% coverage).
- [ ] No wildcard imports; import groups correct.
