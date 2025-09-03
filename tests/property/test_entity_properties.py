"""
Property-based tests for ExampleEntity.
"""

from hypothesis import given, strategies as st
from cline_project_template.domain.example_entity import ExampleEntity


@given(id=st.integers(), name=st.text())
def test_entity_round_trip(id: int, name: str) -> None:
    """Creating an entity should preserve id and name exactly."""
    e = ExampleEntity(id=id, name=name)
    assert e.id == id
    assert e.name == name
