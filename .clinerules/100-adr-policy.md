---
description: Capture significant architectural decisions and their context for future maintainers.
author: Your Team
version: 2.1
globs: ["docs/adr/**"]
tags: ["adr","architecture"]
---

# 100 – Architecture Decision Records

Objective
- Preserve rationale behind significant choices and enable informed future changes.

Outcomes
- Major dependency/framework changes, new integration patterns, schema shifts, and non-trivial architectural changes have ADRs.
- ADRs follow a consistent template covering context, decision, alternatives, and consequences.
- PRs that implement those changes link the relevant ADR.

Cline directives
- MUST create ADRs for significant decisions BEFORE or alongside implementation.
- SHOULD reference ADRs in PRs and code comments where relevant.

Acceptance signals
- ADRs exist and are discoverable under docs/adr; PRs link to them.
- Decisions are understandable months later from ADRs alone.