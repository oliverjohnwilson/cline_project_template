"""
Integration test: ExampleUseCase with a repository.
"""

from cline_project_template.application.example_use_case import ExampleUseCase
from cline_project_template.infrastructure.db_gateway import InMemoryExampleRepository


def test_use_case_creates_entity_and_repo_saves() -> None:
    """Use case should create entity and repository should persist it."""
    repo = InMemoryExampleRepository()
    use_case = ExampleUseCase()

    entity = use_case.execute(id=42, name="Persisted")
    repo.save({"id": entity.id, "name": entity.name})

    stored = repo.all()
    assert {"id": 42, "name": "Persisted"} in stored
