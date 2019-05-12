import click
from flask.cli import FlaskGroup


def cave_create_app():
    from cave.app import create_app
    return create_app()


@click.group(cls=FlaskGroup, create_app=cave_create_app)
def cli():
    """This is a management script for cave"""


if __name__ == "__main__":
    cli()
