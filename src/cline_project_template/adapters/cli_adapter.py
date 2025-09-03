"""
CLI adapter for the ExampleUseCase.

Author: Oliver J Wilson
"""

import click
from ..application.example_use_case import ExampleUseCase


@click.command()
@click.argument("id", type=int)
@click.argument("name")
def main(id: int, name: str) -> None:
    """
    CLI entrypoint to create an ExampleEntity.

    Args:
        id: Unique identifier.
        name: Name for the entity.
    """
    entity = ExampleUseCase().execute(id, name)
    click.echo(f"Created entity: {entity}")
