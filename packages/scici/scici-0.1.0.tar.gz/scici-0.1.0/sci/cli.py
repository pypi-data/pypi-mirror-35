import click
from blindspin import spinner


@click.group()
def cli():
    pass

@cli.command()
def create():
    pass

@cli.commmand()
def copy():
    pass

@cli.command()
def run():
    pass

@cli.command()
def up():
    pass

@cli.command()
def install():
    pass

@cli.group()
def instrument():
    pass

@instrument.command()
def connect():
    pass

@cli.group()
def sync():
    pass

@sync.command()
def remote():
    pass

