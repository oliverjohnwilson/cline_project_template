---
description: Mandatory reflection and knowledge capture to improve reliability and efficiency across tasks.
author: Your Team
version: 1.1
tags: ["meta","behavior","memory"]
globs: ["memory-bank/**"]
---

# 010 – Cline Continuous Improvement Protocol

Objective
- Ensure Cline captures learnings, distills core principles, and reuses them to avoid repeated effort and mistakes.

Scope and trigger
- Applies to any non-trivial, multi-step, problem-solving, or feedback-informed task.
- MUST run before attempt_completion for such tasks. Trivial mechanical tasks MAY be exempt.

Required knowledge files
- memory-bank/raw_reflection_log.md: timestamped raw entries per task (observations, difficulties and resolutions, successes, key commands/envs).
- memory-bank/consolidated_learnings.md: pruned, generalized, actionable insights organized for reuse.

Outcomes
- Every non-trivial task adds a timestamped raw entry covering learnings, difficulties, and successes before completion.
- Periodically, durable insights are synthesized into concise patterns in consolidated_learnings.md.
- Raw entries that have been consolidated are pruned to keep the raw log current and lean.

Cline directives
- MUST create the memory-bank/ files if missing (empty stubs are acceptable).
- MUST NOT include secrets or sensitive data in knowledge files; reference placeholders if needed.
- SHOULD reference sources or PRs when insights are project-specific.

Raw entry template (example)
- Date: YYYY-MM-DD
- TaskRef: short description or branch/PR
- Learnings: list of new info, underlying patterns, API behaviors, project-specific commands/envs
- Difficulties: what slowed us down; how it was resolved; preventive note
- Successes: what worked especially well; contributing factors
- Candidates for consolidation: generalizable patterns or critical specifics to move up

Consolidation guidance
- Focus on reusable patterns, critical configurations, resolved errors, and strategies that save time.
- Keep entries concise, structured, and non-redundant; organize by topic/tech/project.
- Only propose changes to other .clinerules when an insight is broadly applicable and confirmed; ask for user confirmation first.

Acceptance signals
- New non-trivial work results in a raw entry before completion.
- Consolidated learnings remain short, high-signal, and easy to retrieve.
- The raw log is periodically pruned after consolidation.