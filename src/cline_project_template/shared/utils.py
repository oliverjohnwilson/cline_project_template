"""
Generic utility functions.

Author: Oliver J Wilson
"""

import logging
from typing import Any


def get_logger(name: str) -> logging.Logger:
    """
    Get a configured logger.

    Args:
        name: Logger name.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def deep_merge_dicts(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    """
    Recursively merge two dictionaries.

    Args:
        a: Base dictionary.
        b: Dictionary to merge into a.

    Returns:
        dict: Merged dictionary.
    """
    result = dict(a)
    for key, value in b.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
