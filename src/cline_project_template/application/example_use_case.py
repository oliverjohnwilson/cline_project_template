"""
Example application use case.
"""

from ..domain.example_entity import ExampleEntity


class ExampleUseCase:
    """
    Example use case that creates an ExampleEntity.

    This class demonstrates the application layer's role in orchestrating
    domain logic without depending on infrastructure.
    """

    def execute(self, id: int, name: str) -> ExampleEntity:
        """
        Create a new ExampleEntity.

        Args:
            id: Unique identifier.
            name: Name for the entity.

        Returns:
            ExampleEntity: The created entity.
        """
        return ExampleEntity(id=id, name=name)
