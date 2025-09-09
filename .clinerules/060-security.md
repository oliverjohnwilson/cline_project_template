---
description: Prevent vulnerabilities, protect secrets, and maintain supply-chain hygiene.
author: Your Team
version: 2.1
tags: ["security"]
globs: ["requirements*.txt","pyproject.toml",".env.example"]
---

# 060 – Security

Objective
- Bake in secure defaults and early detection.

Outcomes
- No secrets in code or configs; only references to secret managers.
- Static analysis and dependency audits pass within agreed severity thresholds.
- Inputs are validated and serialization is safe by default; sensitive data is redacted.

Cline directives
- MUST NOT commit secrets; use references/tokens only.
- MUST highlight risky libraries/patterns and recommend safer alternatives.
- SHOULD propose redaction for logs that may include sensitive fields.

Acceptance signals
- Secret scans are clean; .env.example is updated.
- SAST and dependency audit pass or explicitly risk-accepted with mitigation.
- Logging avoids sensitive data; redaction present where needed.