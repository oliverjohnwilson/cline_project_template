"""
check_license.py

Purpose:
    Enforce the "no license propagation" rule in a configuration-driven way.
    If a downstream repository still contains the original template LICENSE,
    the script will (optionally) remove it and fail the check so the user
    can add an appropriate license for their new project.

Configuration (no hardcoding in code):
    Define policy in pyproject.toml under [tool.cline.license_policy],
    or (fallback) .clinerules/policy/license_policy.json.

    Example (pyproject.toml):
        [tool.cline.license_policy]
        # SHA-256 of the template's LICENSE content (normalized to LF)
        template_license_sha256 = "PUT_YOUR_TEMPLATE_LICENSE_SHA256_HERE"
        # One or more canonical template repo URLs; if origin matches, allow license
        template_repo_urls = ["https://github.com/your-org/cline_project_template"]
        # Automatically remove the template LICENSE in downstream repos
        auto_remove = true
        # If true, don't run enforcement inside the template repo itself
        allow_in_template_repo = true
        # Optional: where to store backups if auto_remove = true
        backup_dir = ".license_backup"

    Fallback (JSON), same keys (strings, booleans, arrays):
        .clinerules/policy/license_policy.json

Environment variable overrides (optional):
    - CLINE_TEMPLATE_LICENSE_SHA256: overrides template_license_sha256
    - CLINE_TEMPLATE_REPO_URLS: comma-separated list of URLs
    - CLINE_LICENSE_AUTO_REMOVE: "1"/"true"/"yes" to enable auto-remove
    - CLINE_LICENSE_ALLOW_IN_TEMPLATE: "1"/"true"/"yes" to allow in template repo
    - CLINE_LICENSE_BACKUP_DIR: path for backups

Behavior:
    - If LICENSE is absent: pass.
    - If policy can't be loaded or hash missing: fail with guidance (explicit policy required).
    - If current repo is the template (origin matches configured URLs): pass (unless allow_in_template_repo = false).
    - If LICENSE hash matches template_license_sha256 in a non-template repo:
        - If auto_remove: move LICENSE to backup_dir with timestamp, then fail with instructions.
        - Else: fail with instructions.
    - Otherwise: pass.

Requirements:
    - Python 3.11+ (uses tomllib)
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

# Constants
LICENSE_PATH = Path("LICENSE")
PYPROJECT_PATH = Path("pyproject.toml")
JSON_POLICY_PATH = Path(".clinerules/policy/license_policy.json")


@dataclass
class LicensePolicy:
    template_license_sha256: str
    template_repo_urls: list[str]
    auto_remove: bool = True
    allow_in_template_repo: bool = True
    backup_dir: str = ".license_backup"


def _stderr(msg: str) -> None:
    sys.stderr.write(msg + "\n")


def normalize_newlines(data: bytes) -> bytes:
    # Normalize CRLF -> LF to keep hash stable across platforms
    return data.replace(b"\r\n", b"\n")


def sha256_of_file(path: Path) -> str:
    data = path.read_bytes()
    data = normalize_newlines(data)
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def parse_bool_env(val: Optional[str]) -> Optional[bool]:
    if val is None:
        return None
    return val.strip().lower() in {"1", "true", "yes", "on"}


def split_env_list(val: Optional[str]) -> Optional[list[str]]:
    if not val:
        return None
    return [s.strip() for s in val.split(",") if s.strip()]


def load_policy_from_pyproject(pyproject_path: Path) -> Optional[LicensePolicy]:
    if not pyproject_path.exists():
        return None
    try:
        import tomllib  # Python 3.11+
    except Exception:
        _stderr("ERROR: Python 3.11+ required (tomllib not available).")
        return None

    try:
        with pyproject_path.open("rb") as f:
            data = tomllib.load(f)
    except Exception as e:
        _stderr(f"ERROR: Failed to parse {pyproject_path}: {e}")
        return None

    tool = data.get("tool", {})
    cline = tool.get("cline", {})
    policy = cline.get("license_policy", {})
    if not isinstance(policy, dict):
        return None

    tls = policy.get("template_license_sha256")
    urls = policy.get("template_repo_urls") or []
    auto_remove = policy.get("auto_remove", True)
    allow = policy.get("allow_in_template_repo", True)
    backup_dir = policy.get("backup_dir", ".license_backup")

    if tls is None:
        return None
    if not isinstance(urls, list):
        _stderr("ERROR: [tool.cline.license_policy].template_repo_urls must be a list.")
        return None

    return LicensePolicy(
        template_license_sha256=str(tls).strip(),
        template_repo_urls=[str(u).strip() for u in urls],
        auto_remove=bool(auto_remove),
        allow_in_template_repo=bool(allow),
        backup_dir=str(backup_dir).strip(),
    )


def load_policy_from_json(json_path: Path) -> Optional[LicensePolicy]:
    if not json_path.exists():
        return None
    try:
        obj = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception as e:
        _stderr(f"ERROR: Failed to parse {json_path}: {e}")
        return None

    tls = obj.get("template_license_sha256")
    urls = obj.get("template_repo_urls") or []
    auto_remove = obj.get("auto_remove", True)
    allow = obj.get("allow_in_template_repo", True)
    backup_dir = obj.get("backup_dir", ".license_backup")

    if tls is None:
        return None
    if not isinstance(urls, list):
        _stderr("ERROR: license_policy.json template_repo_urls must be a list.")
        return None

    return LicensePolicy(
        template_license_sha256=str(tls).strip(),
        template_repo_urls=[str(u).strip() for u in urls],
        auto_remove=bool(auto_remove),
        allow_in_template_repo=bool(allow),
        backup_dir=str(backup_dir).strip(),
    )


def apply_env_overrides(policy: LicensePolicy) -> LicensePolicy:
    tls = os.getenv("CLINE_TEMPLATE_LICENSE_SHA256")
    urls = split_env_list(os.getenv("CLINE_TEMPLATE_REPO_URLS"))
    auto = parse_bool_env(os.getenv("CLINE_LICENSE_AUTO_REMOVE"))
    allow = parse_bool_env(os.getenv("CLINE_LICENSE_ALLOW_IN_TEMPLATE"))
    backup = os.getenv("CLINE_LICENSE_BACKUP_DIR")

    if tls:
        policy.template_license_sha256 = tls.strip()
    if urls:
        policy.template_repo_urls = urls
    if auto is not None:
        policy.auto_remove = auto
    if allow is not None:
        policy.allow_in_template_repo = allow
    if backup:
        policy.backup_dir = backup.strip()
    return policy


def get_repo_origin_url() -> str:
    try:
        out = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out
    except Exception:
        return ""


def origin_matches_template(url: str, template_urls: list[str]) -> bool:
    if not url or not template_urls:
        return False
    # Normalize trivial .git suffix differences
    def norm(u: str) -> str:
        u = u.strip()
        return u[:-4] if u.endswith(".git") else u

    nurl = norm(url)
    return any(norm(tu) == nurl for tu in template_urls)


def ensure_backup_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def backup_and_remove_license(backup_dir: Path, license_path: Path) -> Path:
    ensure_backup_dir(backup_dir)
    ts = time.strftime("%Y%m%d-%H%M%S")
    backup_path = backup_dir / f"LICENSE.template_backup.{ts}"
    shutil.move(str(license_path), str(backup_path))
    return backup_path


def main() -> int:
    # 1) Load policy (pyproject preferred, JSON fallback), then apply env overrides.
    policy = load_policy_from_pyproject(PYPROJECT_PATH) or load_policy_from_json(JSON_POLICY_PATH)
    if policy is None or not policy.template_license_sha256:
        _stderr(
            "ERROR: License policy not configured. Define either:\n"
            "  - [tool.cline.license_policy] in pyproject.toml, or\n"
            "  - .clinerules/policy/license_policy.json\n"
            "Required key: template_license_sha256 (SHA-256 of template LICENSE).\n"
            "Optional keys: template_repo_urls (list), auto_remove (bool), "
            "allow_in_template_repo (bool), backup_dir (str).\n"
        )
        return 2

    policy = apply_env_overrides(policy)

    # 2) If no LICENSE present, nothing to enforce.
    if not LICENSE_PATH.exists():
        return 0

    # 3) Allow inside the template repo if configured so.
    origin_url = get_repo_origin_url()
    if origin_matches_template(origin_url, policy.template_repo_urls):
        if policy.allow_in_template_repo:
            return 0
        # If not allowed in template repo, continue and enforce anyway.

    # 4) Compare LICENSE hash to template fingerprint.
    try:
        current_hash = sha256_of_file(LICENSE_PATH)
    except Exception as e:
        _stderr(f"ERROR: Unable to read LICENSE for hashing: {e}")
        return 2

    if current_hash == policy.template_license_sha256:
        # Template LICENSE detected in a non-template repo (or template enforcement is on).
        if policy.auto_remove:
            backup_dir = Path(policy.backup_dir)
            try:
                backup_path = backup_and_remove_license(backup_dir, LICENSE_PATH)
                _stderr(
                    "Template LICENSE detected and removed (configuration-driven policy).\n"
                    f"Backup saved to: {backup_path}\n"
                    "Action required: add an appropriate LICENSE for this project, "
                    "or intentionally proceed without one if private."
                )
            except Exception as e:
                _stderr(
                    "ERROR: Template LICENSE detected but auto-removal failed.\n"
                    f"Please remove or replace LICENSE manually. Reason: {e}"
                )
                return 1
            # Block the commit to force adding/confirming the correct license.
            return 1
        else:
            _stderr(
                "ERROR: Template LICENSE detected. Remove or replace the LICENSE file before committing.\n"
                "This repository must define its own licensing. See .clinerules/120-license-handling.md."
            )
            return 1

    # 5) Current LICENSE differs from template; pass.
    return 0


if __name__ == "__main__":
    sys.exit(main())
