---
description: Outcome-focused Python style, typing, and documentation standards.
author: Your Team
version: 2.1
globs: ["**/*.py","pyproject.toml","README.md","docs/**"]
tags: ["python","style","typing","docs"]
---

# 020 – Python Style, Typing, and Docs

Objective
- Keep the codebase idiomatic, strongly typed, and self-explanatory with succinct docs.

Outcomes
- Code is consistently formatted and linted; diffs are clean.
- Public APIs are fully typed; no implicit Any in public surfaces.
- Docstrings for public APIs are present, accurate, and consistent.
- Examples are runnable where practical.

Cline directives
- MUST output typed, PEP 8–compliant code and public docstrings by default.
- SHOULD use Protocol/ABC for interfaces and dataclasses for data.
- MUST NOT introduce wildcard imports or silence genuine issues without justification.

Acceptance signals
- Style and lint checks yield zero blocking issues.
- Static typing passes at a strict level for public APIs.
- Docstring coverage for public APIs is at or above target (e.g., 90%).
- No wildcard imports; import groups and order are consistent.