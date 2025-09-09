---
description: Clean history, reviewable PRs, and reliable quality gates.
author: Your Team
version: 2.1
globs: [".github/workflows/**", ".github/PULL_REQUEST_TEMPLATE*.md"]
tags: ["git","pr","ci","quality"]
---

# 090 – Git, PRs, and CI Quality Gates

Objective
- Maintain a traceable history and enforce quality without manual policing.

Outcomes
- Commits and PRs are small, focused, and follow Conventional Commits.
- PR descriptions communicate rationale, tests, docs changes, and for fixes, an RCA.
- All required CI gates block merges until green.

Cline directives
- MUST use Conventional Commits and propose clear PR descriptions with required sections.
- SHOULD split orthogonal changes to keep diffs reviewable.
- MUST NOT suggest disabling CI gates to pass builds; fix underlying issues instead.

Acceptance signals
- Conventional Commit messages; linked issues where appropriate.
- PRs include tests/docs/rationale; large changes split behind flags or into sequenced PRs.
- CI gates pass consistently: style/typing/docs tests, coverage, contracts, security, docs build (if applicable), and license checks.