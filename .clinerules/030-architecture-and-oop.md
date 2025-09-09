---
description: Enforce clean architecture and pragmatic OOP to preserve separation of concerns.
author: Your Team
version: 2.1
tags: ["architecture","boundaries","oop"]
---

# 030 – Architecture and OOP

Objective
- Maintain domain purity and strict boundaries; use OOP to model intent without excess complexity.

Outcomes
- Layers: domain (pure, no IO/framework), application (use cases, interfaces), adapters (inbound/outbound), infrastructure (concrete integrations).
- Dependencies flow inward only; no reverse imports.
- Application depends on abstractions; implementations are injected at edges.
- Classes are cohesive, small, and favor composition over inheritance; value objects are immutable.

Cline directives
- MUST define interfaces with typing.Protocol or abc.ABC where external systems are involved.
- MUST keep entry points thin and delegate to application use cases.
- MUST NOT import adapters/infrastructure from domain/application layers.
- SHOULD encode invariants and prefer pure functions for stateless domain logic.

Acceptance signals
- Import contracts pass; domain has no IO or framework imports.
- Entry points orchestrate via use cases; implementations injected at edges.
- No deep inheritance hierarchies or god objects; invariants encoded and tested.
- Shared utilities are minimal and layer-agnostic.