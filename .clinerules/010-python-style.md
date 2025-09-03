# 010 – Python Style Guide

## Purpose
Ensure consistent, idiomatic, and maintainable Python code.

## Rules

- **Formatting:** Use Black with a line length of 100.
- **Linting:** Use Ruff with PEP 8 compliance and selected plugins for bug prevention.
- **Imports:** Use isort with Black profile; group as stdlib, third‑party, local.
- **Naming:**
  - Classes: CapWords
  - Functions/variables: lower_snake_case
  - Constants: UPPER_SNAKE_CASE
- **Typing:** All public functions/methods must have complete type hints.
- **Docstrings:** Follow PEP 257 with Google or NumPy style.
- **F‑Strings:** Prefer f‑strings over `%` or `.format()`.
- **Comprehensions:** Use list/dict/set comprehensions where clearer.
- **Avoid:** Wildcard imports, mutable default arguments, deep nesting.

## Checklist
- [ ] Black, Ruff, isort pass locally.
- [ ] No unused imports or variables.
- [ ] Type checker passes with `--strict`.
