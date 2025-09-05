# Security Policy

Security is a first‑class concern in this template and in any downstream projects created from it.

- No secrets in code or configs. Use environment variables and a secret manager.
- `.env` must never be committed. An `.env.example` is provided to document variables.
- Static analysis and dependency audits run locally (pre‑commit) and in CI.
- Safe defaults for logging and serialization (avoid pickle; redact sensitive data).

See also:
- `.clinerules/070-security-standards.md` for detailed standards.
- `docs/security.md` for developer‑facing guidance.

## Supported versions

This template targets Python 3.11+ by default. CI typically runs on 3.11 and 3.12.

## Reporting a vulnerability

If you discover a security issue related to this template:

- Please open a confidential channel by creating a security advisory in the repository, or
- Email the maintainer listed below with details and reproduction steps.

We will acknowledge receipt, investigate promptly, and provide remediation guidance or a patch.

Maintainer:
- Name: Oliver J Wilson
- Contact: please use GitHub Security Advisories for this repository or open a “Security” discussion with minimal details and a maintainer will respond with a private channel.

## Security tooling

- Bandit (SAST) scans `src/` in pre‑commit and CI.
- detect‑secrets scans all files in pre‑commit.
- pip‑audit runs in CI to fail on known vulnerabilities.
- Pre‑commit hooks are executed in CI to ensure local gates run on the server side.

## Secrets handling

- Use `.env` for local development only (never commit). Start from `.env.example`.
- Never log secrets, tokens, or PII. Consider adding redaction filters to loggers if handling sensitive data.
- Rotate secrets immediately if a leak is suspected and invalidate exposed credentials.

## Coordinated disclosure

We support coordinated disclosure. If you plan to report a vulnerability that could impact downstream users, please indicate so in your initial report so we can coordinate fixes and communicate responsibly.
