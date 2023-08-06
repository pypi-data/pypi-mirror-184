# x-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando vp - variação percentual
@click.command()
@click.argument("preco", type=float)
def vp(preco):
    """Variação percentual para suporte e resistência."""
    r1 = preco * (1 + 0.01)
    r2 = preco * (1 + 0.02)
    s1 = preco * (-1 + 0.01)
    s2 = preco * (-1 + 0.02)
    click.echo("%.2f" % r2)
    click.echo("%.2f" % r1)
    click.echo("%.2f" % preco)
    click.echo("%.2f" % abs(s1))
    click.echo("%.2f" % abs(s2))


if __name__ == "__main__":
    vp()
