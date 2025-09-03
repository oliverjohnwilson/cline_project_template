"""
Unit tests for ExampleEntity.

Covers creation, immutability, and equality semantics.
"""

import pytest
from cline_project_template.domain.example_entity import ExampleEntity


def test_entity_creation_and_attributes() -> None:
    """Entity should store id and name as given."""
    e = ExampleEntity(id=1, name="Test")
    assert e.id == 1
    assert e.name == "Test"


def test_entity_is_immutable() -> None:
    """Entity should be frozen and raise on attribute mutation."""
    e = ExampleEntity(id=1, name="Immutable")
    with pytest.raises(AttributeError):
        # type: ignore[attr-defined]
        e.name = "Changed"


def test_entity_equality() -> None:
    """Entities with same id and name should be equal."""
    e1 = ExampleEntity(id=1, name="Same")
    e2 = ExampleEntity(id=1, name="Same")
    assert e1 == e2
    assert hash(e1) == hash(e2)
