import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """Data pipeline playground."""
    click.echo("Hello, world!")
