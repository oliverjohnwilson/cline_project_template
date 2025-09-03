"""
Example domain entity.

Author: Oliver J Wilson
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExampleEntity:
    """
    Immutable value object representing an example entity.

    Attributes:
        id: Unique identifier for the entity.
        name: Human-readable name for the entity.
    """

    id: int
    name: str
