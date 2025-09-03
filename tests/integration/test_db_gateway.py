"""
Integration tests for InMemoryExampleRepository.
"""

from cline_project_template.infrastructure.db_gateway import InMemoryExampleRepository


def test_save_and_retrieve_records() -> None:
    """Saving records should make them retrievable via all()."""
    repo = InMemoryExampleRepository()
    record = {"id": 1, "name": "Record"}
    repo.save(record)
    all_records = repo.all()
    assert record in all_records
    assert len(all_records) == 1
