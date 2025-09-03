# 000 – Core Principles

## Purpose
Define the foundational values and non‑negotiable standards for all code in this repository.

## Principles

1. **Readability First**
   Code is for humans first, machines second. Favor clarity over cleverness.

2. **Pythonic by Default**
   Follow the Zen of Python (PEP 20) and PEP 8 style guidelines.

3. **Boundaries Matter**
   Maintain strict separation between domain, application, adapters, and infrastructure.

4. **Reproducibility**
   Every build, test, and deployment must be deterministic.

5. **Automation Over Convention**
   Enforce rules via tooling (pre‑commit, CI) rather than relying on memory.

6. **Security Consciousness**
   No secrets in code. Scan dependencies and code for vulnerabilities.

7. **Documentation as a Feature**
   Docs are part of the deliverable, not an afterthought.

8. **Fail Fast**
   Detect and reject violations early in the development process.

## Checklist
- [ ] Code passes all automated checks before commit.
- [ ] No unexplained deviations from PEP 8 or architecture rules.
- [ ] Documentation updated alongside code changes.
