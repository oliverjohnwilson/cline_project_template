# 070 – Security Standards

## Purpose
Prevent vulnerabilities, protect secrets, and maintain supply-chain hygiene.

## Objectives
- No secrets in code or configs.
- Early detection of risky patterns and vulnerable dependencies.
- Safe defaults for inputs, serialization, and external interactions.

## Non-negotiable rules
- Secrets: never commit secrets; provide `.env.example` and use a secret manager; configs contain references (e.g., ${SECRET_REF}) not raw values.
- Scanning:
  - SAST: bandit on `src/` with high/med findings reviewed; criticals must be fixed.
  - Dependency audit: pip-audit (or equivalent) with blocking severity policy.
  - Secret scanning: detect-secrets in pre-commit; rotate if a secret leaks.
- Dependencies: pin direct deps; review changelogs before upgrades; remove unused deps.
- Input handling: validate/sanitize untrusted inputs; safest serialization first (avoid `pickle`).
- Logging: no sensitive data in logs; redact by default.

## Enforcement
- Pre-commit: bandit, detect-secrets.
- CI: pip-audit job; bandit job; failure thresholds enforced.
- Review: security checklist in PR; threat considerations for new integrations.

## Cline directives
- Must default to safe libraries and patterns; call out risky suggestions.
- Must avoid encouraging suppression of security findings without mitigation.
- Must propose redaction for any potentially sensitive logs.

## Checklist
- [ ] No secrets present; `.env.example` updated.
- [ ] Audit and SAST scans clean or risk-accepted with mitigation.
- [ ] Dependency changes reviewed and justified.
