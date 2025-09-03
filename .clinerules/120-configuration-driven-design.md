# 220 – Configuration-Driven Design and Declarative Workflows

## Purpose
Eliminate hardcoded configurations and embed flexibility via externalized, declarative control. Code remains generic; behavior is shaped by configuration and policy.

## Objectives
- Zero hardcoded configuration in source.
- Declarative workflows and policies interpreted at runtime.
- Validated, versioned configuration with deterministic resolution.
- Runtime flexibility without code changes.

## Non‑negotiable rules
- Configuration‑Driven Design:
  - Behavior is defined by configuration artifacts (YAML/JSON/DSL) and metadata, not embedded constants.
  - All configurable values (thresholds, URLs, feature flags, routing rules) live in config with defaults documented.
- Declarative Workflows:
  - Represent workflows as declarative specs (YAML/JSON/DSL) describing states, transitions, tasks, timeouts, and retry policy.
  - The runtime interprets these specs; procedural branching in code is minimized to a generic engine.
- Externalized Control Logic:
  - Decision criteria, thresholds, and branching rules reside outside compiled code and can change at runtime/deploy‑time.
  - Use policy bundles or rule files; do not encode these choices in if/else trees within business logic.
- Policy‑as‑Configuration:
  - Business rules and operational policies are expressed as config artifacts, peer‑reviewed and version‑controlled like code.
  - Changes to policies follow the same review/test/validation workflow as code.
- Schemas and Validation:
  - Every configuration and workflow file has a versioned schema (JSON Schema) or a strongly typed loader (Pydantic models).
  - Validate at startup and in CI; reject invalid configs with actionable errors.
- Resolution Order (documented and deterministic):
  1) Built‑in defaults → 2) Base config (configs/default.yaml) → 3) Environment overlay (configs/env/<env>.yaml) → 4) Environment variables → 5) CLI flags/runtime overrides.
- Secrets:
  - No secrets in config files; only references/tokens to secret managers (e.g., ${SECRET_REF}).
- Change Safety:
  - Config changes trigger schema validation, dry‑run (where feasible), and targeted tests/benchmarks for affected paths.

## Enforcement
- Static checks:
  - Forbid known config keys or endpoints from appearing as string literals in code (pattern‑based lint).
  - Forbid domain layer from using `os.environ` directly; require typed settings injection.
- CI jobs:
  - Validate configs/workflows against schemas.
  - Load and validate settings with Pydantic (or equivalent) in a “config‑check” job.
- Runtime guards:
  - Application refuses to start with invalid configuration; error messages enumerate offending keys/paths.
- Review:
  - Policy changes must include updated schema (if needed), examples, and tests demonstrating intended behavior.

## Cline directives
- Must propose schemas (JSON Schema) and typed settings (Pydantic BaseSettings) with defaults and overrides.
- Must factor branching logic into a declarative representation where practical (e.g., state machines, rule tables).
- Must avoid introducing hardcoded thresholds, URLs, or API keys; reference config and settings instead.

## Checklist
- [ ] No hardcoded configuration values in code; all knobs surfaced in config.
- [ ] Config/workflow files validated against schemas; startup validation passes.
- [ ] Resolution order documented and honored; secrets are references only.
- [ ] Tests and examples updated to show new configuration/policy behavior.

## Examples

### Settings skeleton (Pydantic)
```python
from pydantic import BaseSettings, AnyUrl, Field

class AppSettings(BaseSettings):
    env: str = Field(default="dev")
    api_base: AnyUrl
    retry_limit: int = Field(default=3, ge=0, le=10)
    feature_x_enabled: bool = False

    class Config:
        env_prefix = "APP_"
        case_sensitive = False
