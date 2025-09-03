# dev.sh — Local development bootstrap and quality gate runner
#
# Purpose:
#   - Set up a reproducible local dev environment
#   - Run all pre‑commit hooks and tests before pushing
#   - Load configuration from pyproject.toml or .env
#
# Behavior:
#   - Installs/updates dev dependencies
#   - Installs pre‑commit hooks
#   - Runs linting, typing, docs checks, security scans, and tests
#
# Configuration:
#   - Reads .env if present (for PYTHON, VENV_DIR, etc.)
#   - Falls back to defaults if not set
#
# Exit codes:
#   0 — success
#   1 — failure in one or more checks
#   2 — configuration error

set -euo pipefail

# --- Load environment variables from .env if present ---
if [[ -f ".env" ]]; then
    # shellcheck disable=SC2046
    export $(grep -v '^#' .env | xargs)
fi

# --- Configurable defaults ---
PYTHON_BIN="${PYTHON_BIN:-python3.11}"
VENV_DIR="${VENV_DIR:-.venv}"
DEV_EXTRAS="${DEV_EXTRAS:-.[dev]}"
PRECOMMIT_BIN="${PRECOMMIT_BIN:-pre-commit}"

# --- Functions ---
log() { printf "\033[1;34m[dev]\033[0m %s\n" "$*"; }
err() { printf "\033[1;31m[dev:ERROR]\033[0m %s\n" "$*" >&2; }

# --- Ensure Python and venv ---
log "Using Python: $PYTHON_BIN"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    err "Python binary not found: $PYTHON_BIN"
    exit 2
fi

if [[ ! -d "$VENV_DIR" ]]; then
    log "Creating virtual environment in $VENV_DIR"
    "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

# --- Install/upgrade pip and dev dependencies ---
log "Upgrading pip..."
pip install --upgrade pip

log "Installing dev dependencies: $DEV_EXTRAS"
pip install -e "$DEV_EXTRAS"

# --- Install pre-commit hooks ---
log "Installing pre-commit hooks..."
$PRECOMMIT_BIN install

# --- Run all pre-commit hooks on all files ---
log "Running pre-commit hooks..."
$PRECOMMIT_BIN run --all-files

# --- Run tests with coverage ---
log "Running tests with coverage..."
pytest --cov=src --cov-report=term-missing --cov-fail-under=90

# --- Summary ---
log "Development environment ready and all checks passed."
