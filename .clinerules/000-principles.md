# 000 – Core Principles

## Purpose
Establish non‑negotiable standards for elegance, correctness, reproducibility, and security. These principles guide all design, implementation, review, and automation decisions.

## Objectives
- Readable, Pythonic code that communicates intent clearly.
- Clean architecture with strict boundaries and low coupling.
- Deterministic builds, tests, and deployments (reproducibility).
- Guardrails by automation (pre‑commit, CI) over manual policing.
- Security as a first‑class requirement (no secrets, scanned dependencies).
- Documentation treated as a feature, not an afterthought.
- Continuous improvement through metrics, RCA, and small iterations.

## Scope
Applies to all code, configuration, documentation, scripts, and CI/CD in this repository and any downstream project created from this template.

## Principles
1. Readability first: clarity over cleverness; simple beats novel when both work.
2. Pythonic by default: follow PEP 8, PEP 257, and the Zen of Python (PEP 20).
3. Boundaries matter: keep domain pure; isolate side effects at the edges.
4. Reproducibility: pin tools, version environments, and document constraints.
5. Automation: enforce via tools; exceptions must be explicit and reviewed.
6. Security everywhere: assume scrutiny; prevent, detect, and respond early.
7. Documentation as a contract: reflect real behavior with runnable examples.
8. Fail fast: catch violations at commit time; block merges when checks fail.

## Enforcement
- Local: pre‑commit runs formatting, linting, typing, docs checks, security scans, and license safeguards.
- CI: re‑runs all local checks, enforces coverage, import contracts, docs build, and security gates; required checks block merges.
- PR workflow: templates require rationale, tests, docs, and (for fixes) an RCA.

## Cline directives
- Must propose the simplest correct design that honors architecture and configuration rules.
- Must refuse to introduce shortcuts that bypass tests, docs, or boundaries.
- Must surface assumptions, acceptance criteria, and risks for significant changes.

## Exceptions
- Rare and temporary. Document rationale, scope, time limit, and mitigation in PR; add a tracking issue. Remove or replace ASAP.

## Checklist
- [ ] All automated checks pass (local and CI).
- [ ] Architectural boundaries intact; no reverse imports.
- [ ] Docs updated with runnable examples if behavior changed.
- [ ] Security scans green; no secrets leaked.
