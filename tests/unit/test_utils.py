"""
Unit tests for shared utilities.
"""

from cline_project_template.shared.utils import deep_merge_dicts, get_logger


def test_deep_merge_dicts_merges_nested() -> None:
    """deep_merge_dicts should merge nested dicts recursively."""
    a = {"outer": {"inner": 1}, "keep": True}
    b = {"outer": {"inner": 2, "new": 3}}
    merged = deep_merge_dicts(a, b)
    assert merged["outer"]["inner"] == 2
    assert merged["outer"]["new"] == 3
    assert merged["keep"] is True


def test_get_logger_returns_configured_logger() -> None:
    """get_logger should return a logger with a handler and correct name."""
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"
    assert logger.handlers  # at least one handler attached
