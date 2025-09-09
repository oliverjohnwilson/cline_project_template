---
description: Evidence-driven performance improvements and regression prevention.
author: Your Team
version: 2.1
tags: ["performance"]
---

# 070 – Performance

Objective
- Optimize only with evidence; defend budgets on critical paths.

Outcomes
- Hot paths are identified and benchmarked; budgets are defined and tracked.
- Optimizations are justified with profiles or micro-benchmarks.
- Regressions are detected early in CI.

Cline directives
- MUST profile or benchmark before proposing optimizations.
- SHOULD document budgets and expected improvements.
- MUST justify added complexity with measured gains.

Acceptance signals
- Benchmarks exist for critical flows; CI monitors trends.
- Changes that affect hot paths include profiling/benchmark evidence.
- Added complexity is justified by measured improvements.