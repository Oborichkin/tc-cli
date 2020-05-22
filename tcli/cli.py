import os
import click
from .completion import TeamCityCompleter

completer = TeamCityCompleter(
    os.environ.get("TEAMCITY_URL"),
    os.environ.get("TEAMCITY_USER"),
    os.environ.get("TEAMCITY_PASSWORD")
)


@click.command()
@click.argument("cmd", type=click.STRING, autocompletion=completer, nargs=-1)
def main(cmd):
    click.echo(cmd)
