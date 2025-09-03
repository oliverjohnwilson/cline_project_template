# 050 – Testing Standards

## Purpose
Guarantee correctness, prevent regressions, and enable safe refactoring.

## Rules
- **Test Pyramid:** Unit > Integration > E2E.
- **Coverage:** ≥ 90% global, 100% for domain.
- **Property-Based Tests:** Use Hypothesis for invariants.
- **Determinism:** No flaky tests; control time and randomness.
- **Contract Tests:** Adapters must satisfy protocol tests.

## Checklist
- [ ] All new code has tests.
- [ ] Coverage thresholds met.
- [ ] Tests pass consistently.
