# release.sh — Automated release workflow
#
# Purpose:
#   - Validate the repository is in a releasable state
#   - Bump version, tag, and push
#   - Build and publish distribution artifacts
#
# Behavior:
#   - Runs full CI-equivalent checks locally
#   - Reads version bump type from argument (major/minor/patch) or env
#   - Uses configuration from pyproject.toml for project metadata
#
# Exit codes:
#   0 — success
#   1 — failure in checks or release steps
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
PRECOMMIT_BIN="${PRECOMMIT_BIN:-pre-commit}"
BUMP_TYPE="${1:-${BUMP_TYPE:-patch}}"
BUILD_DIR="${BUILD_DIR:-dist}"

# --- Functions ---
log() { printf "\033[1;34m[release]\033[0m %s\n" "$*"; }
err() { printf "\033[1;31m[release:ERROR]\033[0m %s\n" "$*" >&2; }

# --- Ensure clean working tree ---
if [[ -n "$(git status --porcelain)" ]]; then
    err "Working tree is dirty. Commit or stash changes before releasing."
    exit 1
fi

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

# --- Upgrade pip and install dev deps ---
log "Upgrading pip..."
pip install --upgrade pip

log "Installing dev dependencies..."
pip install -e .[dev] build twine bumpver

# --- Run full quality gates ---
log "Running pre-commit hooks..."
$PRECOMMIT_BIN run --all-files

log "Running tests with coverage..."
pytest --cov=src --cov-report=term-missing --cov-fail-under=90

# --- Bump version ---
log "Bumping version: $BUMP_TYPE"
bumpver update --${BUMP_TYPE}

# --- Build artifacts ---
log "Building distribution..."
rm -rf "$BUILD_DIR"
python -m build

# --- Publish to PyPI (requires credentials in env or keyring) ---
log "Publishing to PyPI..."
twine upload "$BUILD_DIR"/*

# --- Push changes and tags ---
log "Pushing commits and tags..."
git push --follow-tags

log "Release complete."
