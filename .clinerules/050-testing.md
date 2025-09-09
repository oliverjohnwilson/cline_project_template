---
description: Fast, deterministic tests with meaningful coverage and clear scopes.
author: Your Team
version: 2.1
tags: ["testing"]
---

# 050 – Testing

Objective
- Guarantee correctness, enable safe refactoring, and prevent regressions.

Outcomes
- Prioritize unit tests; integration covers adapter boundaries; E2E is limited to critical flows.
- High, meaningful coverage; domain logic tends to near-complete coverage.
- Tests are deterministic; time, randomness, and IO are controlled.

Cline directives
- MUST keep tests independent and deterministic; control time/randomness/IO.
- SHOULD use property-based testing for key invariants and pure functions.
- MUST write meaningful assertions; avoid trivial assertions.

Acceptance signals
- Coverage meets target (e.g., ≥ 90% overall; higher in domain modules).
- Tests contain specific assertions and avoid interdependence.
- Property-based testing is present on critical logic.