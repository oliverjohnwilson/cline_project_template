# 090 – Git and PR Standards

## Purpose
Maintain a clean, traceable history and high-quality contributions.

## Objectives
- Small, focused commits and PRs.
- Clear intent via commit messages and PR templates.
- Enforced quality gates before merge.

## Non-negotiable rules
- Conventional Commits: use types like feat, fix, docs, refactor, perf, test, build, ci, chore, with optional scope (e.g., feat(cli): add subcommand).
- Branching: feature/<slug>, fix/<slug>, chore/<slug>, etc.
- PR contents: include tests, docs, rationale, and for bug fixes a full RCA (see 210).
- Reviewability: keep diffs small; split large changes behind feature flags or sequential PRs.
- Issue linkage: link issues; use keywords (Fixes #123) when appropriate.

## Enforcement
- Pre-commit: commit-message lint (e.g., commitizen); block non-conformant messages locally.
- CI: PR body check for required sections (tests, docs, RCA when fix).
- Branch protection: required status checks must pass; linear history preferred.

## Cline directives
- Must generate Conventional Commit messages and PR descriptions with required sections.
- Must split out orthogonal changes and avoid noisy diffs.

## Checklist
- [ ] Commit messages conform; PR template fully completed.
- [ ] All required checks green; no “quick fix” merges.
- [ ] Linked issues and clear rationale present.
