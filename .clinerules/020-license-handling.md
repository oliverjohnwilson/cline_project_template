# 020 – License Handling

## Purpose
Prevent the template's license from propagating into private or proprietary projects.

## Rules

- **Template License:** MIT License applies to this repository only.
- **Downstream Projects:** Remove or replace LICENSE before first commit in a new repo.
- **Automation:** Pre‑commit hook (`scripts/check_license.py`) fails if template license is detected in a non‑template repo.
- **README Notice:** Include a reminder to set an appropriate license.

## Checklist
- [ ] LICENSE removed/replaced in downstream projects.
- [ ] CI passes license check.
