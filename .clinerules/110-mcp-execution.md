---
description: Safe, transparent use of MCP tools with approval, context, and clear fallbacks.
author: Your Team
version: 2.1
tags: ["mcp","tools","planning","process"]
---

# 110 – MCP Execution (General)

Objective
- Improve accuracy and reliability via MCP where available, with explicit approval and transparency.

When to use
- Any task that benefits from external knowledge, structured planning, or automation via MCP.

Outcomes
- MCP server availability and intended queries are surfaced for user approval before invocation.
- Tool responses are summarized with how they change the plan or next step.
- Clear fallbacks exist if an MCP server is unavailable.

Cline directives
- MUST display tool name, parameters, and expected outcome before use_mcp_tool; get user approval.
- MUST summarize results and how they affect the next step after each invocation.
- MUST follow 010 (Continuous Improvement) before attempt_completion on non-trivial tasks.
- SHOULD minimize invocations and avoid redundant or tangential queries.
- MUST defer to tool-specific rules for Context7 (120) and SequentialThinking (130) when applicable.

Acceptance signals
- Pre-invocation: approval captured with intended query/params.
- Post-invocation: concise summary and impact on plan/next steps.
- Fallback documented when tools are unavailable.