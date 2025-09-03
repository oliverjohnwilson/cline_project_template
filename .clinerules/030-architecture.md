# 030 – Architecture Rules

## Purpose
Maintain a clean, scalable, and testable architecture.

## Layered Structure
1. **Domain:** Pure business logic, no external dependencies.
2. **Application:** Orchestrates domain logic, defines use cases.
3. **Adapters:** Translate between application and external systems.
4. **Infrastructure:** Concrete implementations (DB, APIs, etc.).

## Rules
- Dependencies flow inward only.
- No reverse imports (enforced via import‑linter).
- Configuration injected, not hardcoded.
- Shared utilities minimal and generic.

## Checklist
- [ ] No domain code imports from adapters/infrastructure.
- [ ] All external calls isolated in adapters/infrastructure.
