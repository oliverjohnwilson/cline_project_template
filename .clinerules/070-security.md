# 060 – Security Standards

## Purpose
Prevent vulnerabilities and protect sensitive data.

## Rules
- **Secrets:** Never committed; use .env and secret managers.
- **Scanning:** Run bandit and pip‑audit in CI.
- **Dependencies:** Pin versions; review changelogs before updating.
- **Input Validation:** Validate and sanitize all external input.

## Checklist
- [ ] No secrets in repo.
- [ ] Security scans pass.
