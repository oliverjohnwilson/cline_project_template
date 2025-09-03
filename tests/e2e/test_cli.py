"""
End-to-end test for CLI adapter.
"""

import subprocess
import sys
from pathlib import Path


def test_cli_creates_entity(tmp_path: Path) -> None:
    """
    Running the CLI with id and name should output the created entity.

    This test calls the CLI as a subprocess to simulate real usage.
    """
    cmd = [
        sys.executable,
        "-m",
        "cline_project_template.cli.main",
        "example",
        "7",
        "Seven",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    assert "Created entity" in result.stdout
    assert "Seven" in result.stdout
