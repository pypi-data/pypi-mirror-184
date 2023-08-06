import click


@click.command()
def pp():
    click.echo("ponto pivo")


if __name__ == "__main__":
    pp()
