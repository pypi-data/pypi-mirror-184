"""Command-line interface."""
import textwrap

import click

from hypermodern import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option(
    "-l",
    "--language",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
def main(language: str) -> None:
    """Entry point for Wikipedia random fact."""
    page = wikipedia.random_page(language=language)
    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
