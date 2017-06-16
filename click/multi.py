import click
# https://www.youtube.com/watch?v=kNke39OZ2k0


@click.group()
@click.option('--verbose', is_flag=True, help='Number of greetings.')
def cli(verbose):
    """Simple multi command that will call registered subcommands."""
    # This will run before any subcommand, and only when a subcommand runs
    if verbose:
        click.echo('In verbose mode')

@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.argument('file', type=click.File('w'),
                required=False, default="-")   # - is the stdout File in Linux
def hello(count, name, file):
    """Simple subcommand that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name, file=file, color="red")


if __name__ == '__main__':
    cli()

# Usage:
# $ multi.py
# $ multi.py --help
# $ multi.py --verbose
# $ multi.py --help
# $ multi.py hello --help
# $ multi.py hello --count 10
# $ multi.py hello --count 10 --name Rumen
# $ multi.py --verbose help
