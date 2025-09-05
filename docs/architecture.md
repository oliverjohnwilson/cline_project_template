# Architecture

This template enforces a clean architecture with explicit boundaries that are statically checked and continuously verified in CI.

- Domain → Application → Adapters → Infrastructure
- Dependencies flow inward only; no reverse imports
- Configuration-driven design (typed settings; .env example provided)

## Layers

- Domain
  - Pure business logic: entities, value objects, domain services, domain-specific errors
  - No I/O, frameworks, or side effects
  - Example: `ExampleEntity` (`@dataclass(frozen=True)`)

- Application
  - Use cases and orchestrators that depend only on domain abstractions
  - No concrete infrastructure imports
  - Example: `ExampleUseCase` creates domain entities

- Adapters
  - Inbound (CLI/HTTP/etc.): thin argument parsing + delegation to application
  - Outbound (DB/cache/queue): implement application interfaces; translate to concrete I/O
  - Example: CLI adapter (`click`) that invokes `ExampleUseCase`

- Infrastructure
  - Concrete gateways and clients (DB, HTTP, messaging)
  - Must not import domain directly to avoid inward leakage
  - Example: `InMemoryExampleRepository` for prototyping

## Architecture Contracts

Import contracts are defined in `importlinter.ini` and enforced locally (pre-commit) and in CI:

- Domain must not import application, adapters, or infrastructure
- Application must not import adapters or infrastructure
- Infrastructure must not import domain
- Adapters must not import domain

Run manually:

```
lint-imports -c importlinter.ini
```

## Configuration

Typed settings via Pydantic:

- `src/cline_project_template/config/settings.py`
- Environment variables prefixed with `APP_` (see `.env.example`)
- Example fields: `env`, `api_base`, `retry_limit`, `feature_x_enabled`

## CLI

`click`-based CLI entrypoint:

- Group defined in `src/cline_project_template/cli/main.py`
- Subcommand example registered from `adapters/cli_adapter.py`

Usage:

```
python -m cline_project_template.cli.main --help
python -m cline_project_template.cli.main example 7 "Seven"
```

## Testing Strategy

- Unit tests for domain and shared utilities
- Property-based tests (Hypothesis) for invariants
- Integration tests across application + repository
- E2E tests exercising CLI via subprocess
- Coverage gate ≥ 90%

## Tooling Pipeline

- Pre-commit: Black, Ruff (incl. D), isort, mypy, interrogate, Bandit, detect-secrets, import-linter, license check
- CI:
  - Quality gates (pre-commit, mypy, import-linter)
  - Tests with coverage (XML artifact)
  - Security scans (pip-audit, Bandit)
  - (Optional) Docs build

## Extending the Template

- Add new domain entities with invariants and unit tests
- Introduce use cases composing domain services
- Implement adapters and infrastructure for real I/O
- Update import-linter contracts if you create additional layers/packages
- Add configuration fields via typed settings; update `.env.example` and docs
