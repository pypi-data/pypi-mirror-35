import click
from . import commands
from . import validators


@click.group()
def main():
    """Command-line utility for Django code generation."""
    pass


@main.command(short_help='Generate CMS-like templates.')
@click.argument('directory')
@click.option('--title', default='My Project', help='Project title.')
def templates(directory, title):
    """
    Generate CMS-like generic templates for Index and CRUD Class-Based Views.

    \b
    Includes:
        - base.html
        - index.html
        - list.html
        - form.html
        - confirm_delete.html
        - breadcrumb.html

    \b
    WARNING:
    Please, note that the command will overwrite files
    in the given DIRECTORY if such files already exist.
    If this is the case, make sure that you have a backup.
    """
    commands.templates(directory, title)


@main.command(short_help='Generate Model.')
@click.option('--name', '-n', default='MyModel', help='Model name.')
@click.option('--field', '-f', multiple=True, callback=validators.model.validate_field,
              help='Model field. You can provide multiple -f options.')
def model(name, field):
    """Generate common Model with Meta class and overridden __str__ method."""
    commands.model(name, field)
