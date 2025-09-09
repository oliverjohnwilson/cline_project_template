---
description: Behavior is shaped by configuration and policy; code stays generic and typed.
author: Your Team
version: 2.1
tags: ["configuration","design"]
globs: ["configs/**","**/*.yaml","**/*.yml","**/*.json"]
---

# 080 – Configuration-Driven Design

Objective
- Externalize behavior via validated, versioned configuration and policies.

Outcomes
- No hardcoded configuration values; settings are injected and typed.
- Declarative workflows/policies are interpreted at runtime.
- Schemas/typed loaders validate configs in CI and on startup.
- Deterministic resolution order is documented and honored.

Cline directives
- MUST NOT introduce hardcoded thresholds, URLs, or API keys; reference typed settings.
- MUST validate config and fail fast with actionable errors.
- SHOULD factor branching logic into declarative representations where practical.

Acceptance signals
- Config/workflow files validate against schemas; app refuses invalid configs with actionable errors.
- Secrets appear only as references/tokens; not raw values.
- Tests and examples demonstrate configuration-driven behavior.