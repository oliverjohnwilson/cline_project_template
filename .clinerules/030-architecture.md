# 030 – Architecture and Boundaries

## Purpose
Maintain a clean, scalable, testable architecture with strict separation of concerns.

## Objectives
- Domain purity (no IO or framework coupling).
- Application orchestrates use cases via abstractions.
- Adapters translate protocols to real IO.
- Infrastructure implements concrete gateways/clients.
- Dependencies flow inward only.

## Layering
1. Domain: entities, value objects, domain services, domain errors. No IO. No framework imports.
2. Application: use cases, orchestrators, interfaces (Protocols/ABCs). No concrete infra imports.
3. Adapters:
   - Inbound (CLI/HTTP/GraphQL): thin entrypoints calling application use cases.
   - Outbound (DB/cache/queue): implement application interfaces.
4. Infrastructure: DB/HTTP clients, serialization, settings loaders; no leakage inward.

## Non‑negotiable rules
- No reverse dependencies: domain → application → adapters → infrastructure is allowed; reverse is forbidden.
- DIP: depend on abstractions; inject implementations at edges (composition root).
- Config injection: pass settings explicitly; avoid global state and singletons.
- Shared utils: minimal, generic, and dependency‑free; no cross‑layer shortcuts.
- Error design: domain‑specific exceptions; avoid catching broad exceptions at inner layers.

## Enforcement
- Import contracts (example using import‑linter):
  - adapters/infrastructure must not be imported by domain or application.
  - infrastructure must not import domain directly.
  - inbound adapters only call application; outbound adapters implement application interfaces.
- CI: contract checks are required; violations fail builds.
- Static checks: forbid `requests`, `sqlalchemy`, `os`, `pathlib.Path.open`, etc., in domain (pattern‑based lints).

## Cline directives
- Must propose `typing.Protocol`/`abc.ABC` interfaces where the application depends on external systems.
- Must keep entrypoints (CLI/HTTP) thin and delegating to use cases.
- Must refuse designs that import adapters/infrastructure from domain/application layers.

## Checklist
- [ ] Imports respect layering; contracts pass.
- [ ] Application depends on interfaces; concrete impls are injected at edges.
- [ ] Domain free of IO/framework imports and side effects.
- [ ] Shared utilities are minimal and layer‑agnostic.

## Examples
- Good: `application.use_cases.CreateOrder(repository: OrderRepository) -> OrderId`
- Bad: Domain entity importing `requests` or calling a SQL client.
