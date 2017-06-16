import click
# https://www.youtube.com/watch?v=kNke39OZ2k0


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.argument('file', type=click.File('w'),
                required=False, default="-")   # - is the stdout File in Linux
def hello(count, name, file):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name, file=file, color="red")


if __name__ == '__main__':
    hello()

# Usage:
# $ hello.py
# $ hello.py --help
# $ hello.py --count 10
# $ hello.py --count 10 --name Rumen
