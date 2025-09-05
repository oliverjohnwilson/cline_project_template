# 020 – License Handling (No Propagation)

## Purpose
Allow public use of this template while preventing its license from propagating into private or proprietary downstream projects.

## Objectives
- Keep the template permissively licensed.
- Ensure downstream users choose and apply their own license.

## Non-negotiable rules
- Template license: This repository is MIT-licensed (or chosen permissive license).
- Downstream projects created from this template:
  - Must remove or replace the LICENSE file before the first commit.
  - Must update the README to reflect the chosen license or “All rights reserved” if private.
- README notice: The template README must instruct downstream users to set their own license.

## Enforcement
- Pre-commit: `scripts/check_license.py` fails if the template copyright line remains.
- CI: a required job runs the same check across the repo.
- PR review: template changes must keep the license reminder intact.

## Cline directives
- Must remind users to remove/replace the license on project generation.
- Must not copy this template’s LICENSE into downstream code intended to be private/proprietary.

## Checklist
- [ ] LICENSE removed/replaced in downstream.
- [ ] README updated with correct license notice.
- [ ] License check passes in pre-commit and CI.
