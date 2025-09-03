# 050 – Testing Standards

## Purpose
Guarantee correctness, enable safe refactoring, and prevent regressions.

## Objectives
- Fast, deterministic tests.
- High coverage with meaningful assertions.
- Clear separation of unit, integration, and E2E scopes.

## Non‑negotiable rules
- Pyramid: prioritize unit tests; integration tests cover adapter boundaries; E2E reserved for critical flows.
- Coverage: ≥ 90% overall; aim for 100% in domain modules where feasible.
- Property‑based testing: use Hypothesis for key invariants and pure functions.
- Determinism: stub time, randomness, and IO; avoid sleeps and flakes; seed randomness.
- Contracts: adapters must pass shared protocol test suites.
- Bug fixes: add a failing reproduction test before implementing the fix (see 210).

## Enforcement
- CI: coverage threshold gate; test failures are blocking; flaky tests must be deflaked before merge.
- Local: optional “fast tests” subset in pre‑commit; full suite in CI.
- Style: assert specific outcomes; avoid “assert True”/empty tests.

## Cline directives
- Must write reproduction tests first for bugs (red → green → refactor).
- Must provide meaningful assertions and property tests on critical logic.
- Must avoid test interdependence; each test self‑contained.

## Checklist
- [ ] New/changed code has tests.
- [ ] Coverage threshold met; no untested branches in domain.
- [ ] Tests deterministic; seeds or fakes used where applicable.
