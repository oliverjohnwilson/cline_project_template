# Security

This template treats security as a first-class concern. It encodes policies and tooling to prevent secret leaks, surface risky patterns early, and maintain supply-chain hygiene.

## Policy highlights

- No secrets in code or configs. Use environment variables and a secret manager.
- Provide `.env.example` with variable names and safe defaults. Never commit `.env`.
- Prefer safe serialization formats; avoid `pickle`.
- Redact sensitive data from logs by default.
- Dependency upgrades should be reviewed with changelogs; remove unused dependencies.

See also:
- Root-level `SECURITY.md` for vulnerability disclosure.
- `.clinerules/070-security-standards.md` for detailed standards.

## Tooling and checks

- Secret scanning: `detect-secrets` pre-commit hook (scans all files).
- Static analysis (SAST): `bandit -q -r src` in pre-commit and CI.
- Dependency audit: `pip-audit` in CI (fails on known vulnerabilities).
- Linting and typing reduce entire classes of defects (Ruff, mypy strict).

## Environment configuration

- Copy `.env.example` to `.env` and adjust values:
  - `APP_ENV`: dev | test | prod
  - `APP_API_BASE`: base URL for external API (example)
  - `APP_RETRY_LIMIT`: int 0–10
  - `APP_FEATURE_X_ENABLED`: boolean
- `.env` is ignored by git (see `.gitignore`).

See .env.example at the repository root.

## Logging guidance

- Use `shared.utils.get_logger` as a starting point.
- Do not log secrets, tokens, or PII.
- Consider adding a redaction filter if the project handles sensitive data.

## CI enforcement

- `pip-audit` step fails the pipeline on vulnerabilities.
- `bandit` step runs static analysis on `src/`.
- Pre-commit is executed in CI to ensure hooks run server-side as well.

## Reporting vulnerabilities

For security issues in downstream projects, use that project’s disclosure channel. For this template repository, see the root-level `SECURITY.md` for disclosure instructions.
