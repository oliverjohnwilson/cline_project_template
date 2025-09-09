---
description: Root-cause-first approach to bug fixing; quick fixes without reproduction are prohibited.
author: Your Team
version: 2.1
tags: ["quality","process","bugs"]
---

# 040 – Root-Cause Bugfixing

Objective
- Eliminate defects at the source and prevent recurrence.

Outcomes
- Every fix starts with a reliable failing test that reproduces the defect.
- PR includes a compact RCA covering symptoms, 5 Whys, root cause, fix, and prevention.
- Preventive guardrails (tests/assertions/lints) are added to catch similar issues earlier.

Cline directives
- MUST guide adding a minimal failing test (red) before proposing code fixes.
- MUST provide an RCA outline and propose preventive guardrails.
- MUST NOT merge fixes that lack reproduction or RCA.

Acceptance signals
- Red → green → refactor is followed.
- RCA present for fix PRs; coverage maintained or improved.
- New safeguards exist for the class of issue fixed.