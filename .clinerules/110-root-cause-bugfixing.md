# 110 – Root-Cause Bugfixing (No Quick Fixes)

## Purpose
Eliminate defects at their source and prevent recurrence. Quick fixes without root cause are prohibited.

## Objectives
- Systematically identify and document the root cause.
- Prove the bug via a failing test before the fix.
- Implement minimal, principled fixes plus prevention.

## Non-negotiable rules
- RCA required: every bug fix must include a Root Cause Analysis using the template below.
- Reproduction first: add a failing test that reliably reproduces the defect; only then implement the fix.
- Systematic solution: address the root cause, not just symptoms; remove dead code or incorrect assumptions.
- Prevention: add tests, assertions, invariants, or lints that would catch the defect earlier next time.
- Documentation: update PR/CHANGELOG with RCA, impact, and preventive actions.

## RCA template (embed in PR)
- Title: concise defect summary
- Symptoms: what failed, where, and under what conditions
- Impact: user/system impact (scope, severity)
- Timeline: first occurrence → detection → mitigation → fix
- 5 Whys: iterative questioning to reach the root cause
- Root cause: the single proximate cause in specific terms
- Fix details: what changed and why it addresses the root cause
- Prevention: new tests/guards/tooling; how they prevent recurrence
- Alternatives considered: trade-offs and why rejected
- Risk: potential side effects; mitigation plans

## Enforcement
- CI: PR body check requires the RCA sections for any `fix:` PR; failing test must exist and pass after fix.
- Review: maintainers reject fixes without reproduction or with hand-wavy RCA.
- Coverage: tests added to maintain overall thresholds.

## Cline directives
- Must refuse to produce a fix without a plan to reproduce and an RCA outline.
- Must guide through adding a minimal failing test before proposing code changes.
- Must propose preventive guardrails (tests, asserts, invariants, lint rules).

## Checklist
- [ ] Failing reproduction test added (red).
- [ ] Minimal principled fix implemented (green).
- [ ] Preventive guardrails added; coverage preserved or improved.
- [ ] RCA included in PR and CHANGELOG updated if user-visible.
