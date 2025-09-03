# 040 – Object-Oriented Practices

## Purpose
Use OOP to model intent clearly while avoiding unnecessary complexity.

## Objectives
- High cohesion, low coupling.
- Composition over inheritance.
- Immutable value objects and minimal shared state.

## Non‑negotiable rules
- SRP: each class has one reason to change.
- Composition > inheritance: prefer delegating behavior; use interfaces (Protocols/ABCs).
- Immutability: use `@dataclass(frozen=True)` for value objects; avoid hidden state.
- Method size/complexity: target ≤ 30 lines and low cyclomatic complexity; extract helpers early.
- Invariants: encode as validation in constructors/factories; prefer pure functions in domain services.

## Enforcement
- Lint: enable complexity and anti‑pattern checks (Ruff rulesets for complexity, returns, simplification).
- Review: PR must justify inheritance and complex control flow.
- Tests: unit tests for entities and services asserting invariants.

## Cline directives
- Must default to dataclasses for state and protocols for contracts.
- Must not introduce deep inheritance hierarchies or “god objects.”
- Must recommend pure functions where state isn’t needed.

## Checklist
- [ ] Classes small and cohesive; no deep hierarchies.
- [ ] Value objects are immutable; invariants covered by tests.
- [ ] Complex methods decomposed into readable units.
