"""
Example database gateway implementation.

Author: Oliver J Wilson
"""

from typing import Protocol


class ExampleRepository(Protocol):
    """Protocol for an example repository."""

    def save(self, data: dict) -> None:
        ...


class InMemoryExampleRepository:
    """
    In-memory implementation of ExampleRepository.

    Suitable for testing or prototyping.
    """

    def __init__(self) -> None:
        self._store: list[dict] = []

    def save(self, data: dict) -> None:
        """Save a record to the in-memory store."""
        self._store.append(data)

    def all(self) -> list[dict]:
        """Return all stored records."""
        return list(self._store)
