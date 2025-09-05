# 130 - MCP and Cline Execution Protocol

## Goals
- Use MCP servers when available to improve accuracy, planning, and integrations.
- Stay activation-conditioned: if a server is absent, proceed without it.

## Discovery
- Cline hosts MCP servers listed in cline_mcp_settings.json and via user-enabled servers.
- Before using any MCP tool, surface availability to the user and request approval.

## Context7 (API and library docs)
Use when:
- Implementing or integrating with third-party libraries or APIs.
- Upgrading dependencies or evaluating alternatives.

Protocol:
1) If Context7 MCP is available, offer to search for the exact library or API endpoints.
2) With user approval, retrieve the most relevant docs and examples.
3) Cite retrieved sources inline in the PR description or code comments where helpful.

Fallback:
- If Context7 is unavailable, proceed with locally available docs or vendor docs linked manually.

## Sequential Thinking (structured multi-step planning)
Use when:
- Complex refactors, migrations, or multi-module features.
- Ambiguous requirements needing explicit branching or revision steps.

Protocol:
1) Propose a stepwise plan and ask to run sequential_thinking with initial thoughts.
2) With approval, run the tool to structure steps, revisions, and branches.
3) Execute steps iteratively, checkpointing after each milestone and updating the plan as needed.

Privacy:
- If required, set the environment variable to disable logging of detailed thoughts per server documentation.

Fallback:
- If the server is unavailable, outline the plan inline and execute with frequent checkpoints.

## Azure MCP (illustrative)
Use when:
- Interacting with Azure resources or needing live listings/operations provided by the Azure MCP server.

Protocol:
1) If Azure MCP is available and authenticated, list relevant resources with user approval.
2) Confirm intended scope and execute minimal, reversible operations.
3) Record commands and results for traceability.

## General Cline Execution
- Always ask before invoking MCP tools; show the intended query and expected outcome.
- Surface tool responses and how they affect the next step.
- Keep rules toggleable: enable this file when external tools are desired; disable otherwise.

## Checklist
- [ ] Server availability surfaced and user approved.
- [ ] Tool invocations minimal and relevant.
- [ ] Results integrated into code or docs with citations.
- [ ] Fallback path followed if servers are unavailable.