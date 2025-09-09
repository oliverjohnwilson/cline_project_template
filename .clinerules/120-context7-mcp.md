---
description: High-signal retrieval of authoritative API/library documentation via a docs-search MCP.
author: Your Team
version: 1.1
tags: ["mcp","docs","api","research"]
---

# 120 – Context7 MCP (API and Library Docs)

Objective
- Retrieve authoritative docs/examples to reduce guesswork when integrating, upgrading, or evaluating libraries/APIs.

When to use
- Implementing or integrating third-party libraries/APIs.
- Upgrading dependencies or comparing alternatives.
- Verifying exact parameters, return types, or edge-case behaviors.

Cline directives
- MUST, before first use, list the Context7 tool and echo its parameter schema; use exact parameter names and required types.
- MUST show intended query and expected doc types (symbols, versions) and get approval before invocation.
- MUST include short summaries and links to retrieved sources; cite where they influence code/tests/PRs.
- SHOULD craft precise queries (package, symbol, version) and filter to relevant excerpts.
- MUST fall back to local/vendor docs if the server is unavailable and note the fallback.

Acceptance signals
- Approved, precise query; tool schema acknowledged and respected.
- Citations present where docs inform decisions.
- Clear fallback noted if Context7 is unavailable.