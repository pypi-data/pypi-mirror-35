import webbrowser
import click


@click.command()
@click.argument('query')
def cli(query):
    """Nanobrain cli"""
    q = '+'.join(query.split(' '))
    url = 'https://nanobrain.io/compute?q={}'.format(q)
    click.echo('\n\t {}'.format(url))
    click.echo('\n\t Opening a default browser...')
    webbrowser.open(url)


if __name__ == '__main__':
    cli()
