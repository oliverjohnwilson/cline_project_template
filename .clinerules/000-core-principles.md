---
description: Non-negotiable outcomes for elegance, correctness, reproducibility, and security across the repo.
author: Your Team
version: 2.1
tags: ["core","behavior","quality"]
---

# 000 – Core Principles

Objective
- Set mandatory outcomes that govern design, implementation, review, and automation.

Outcomes
- Code is readable and intent-revealing; simplicity over cleverness when both suffice.
- Architecture has strict boundaries and low coupling; domain remains pure.
- Builds, tests, and releases are deterministic and reproducible.
- Automation enforces standards; exceptions are explicit and time-bounded.
- Security-first: no secrets in code; dependencies scanned.
- Documentation is part of the feature.
- Continuous improvement is sustained via reflection and small iterations (see 010).

Cline directives
- MUST propose the simplest correct design that honors boundaries and configuration.
- MUST refuse shortcuts that bypass tests, docs, or architectural rules.
- SHOULD surface assumptions, acceptance criteria, and risks for significant changes.

Acceptance signals
- All required checks pass consistently on local and CI.
- Layering and import contracts hold; no reverse imports.
- Docs reflect real behavior; runnable examples where feasible.
- Security scans pass; no secrets leaked.

Exceptions
- Rare and temporary; document rationale, scope, expiry, mitigation; track and remove quickly.