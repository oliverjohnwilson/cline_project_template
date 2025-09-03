# 180 – Performance Standards

## Purpose
Ensure efficiency on critical paths without premature optimization.

## Objectives
- Identify hot paths and set budgets.
- Guard against performance regressions.
- Optimize only with evidence.

## Non‑negotiable rules
- Profiling: identify hot paths with profiles/metrics before optimizing.
- Budgets: define latency/throughput targets for critical flows and track in CI.
- Allocations: minimize unnecessary allocations in tight loops; consider generators/iterators.
- Concurrency: use asyncio or multiprocessing only when profiles show benefits; avoid needless complexity.
- Data structures: choose appropriate structures (e.g., dict/set for lookups) based on usage.

## Enforcement
- Benchmarks: pytest‑benchmark (or similar) for targeted hot paths; CI tracks baseline and fails on significant regressions.
- Review: evidence required (profile/bench results) for performance‑motivated changes.

## Cline directives
- Must propose optimizations only after establishing the bottleneck.
- Must include micro‑benchmarks or profile excerpts for changes justified by performance.

## Checklist
- [ ] Hot paths identified and covered by benchmarks.
- [ ] Budgets documented; CI within thresholds.
- [ ] Optimizations backed by evidence; complexity justified.
