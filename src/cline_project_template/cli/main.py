"""
Main CLI entrypoint.
"""

import click
from ..adapters.cli_adapter import main as example_main


@click.group()
def cli() -> None:
    """cline_project_template CLI."""
    pass


# Register subcommands
cli.add_command(example_main, name="example")


if __name__ == "__main__":
    cli()
