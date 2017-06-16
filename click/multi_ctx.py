import click
# https://www.youtube.com/watch?v=kNke39OZ2k0

# simple shared context class - an instance of it will be created and passed/shared
# between the main command and subcommands


class Context:
    def __init__(self):
        self.add_count = 0


# create a decorater - ensure=True means that a context instance will be
# created the first time when needed if not already created
pass_config = click.make_pass_decorator(Context, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True, help='Verbose mode.')
@click.option('--add-count', default=0, help='Additional count.')
@pass_config   # if added it will pass the created shared context as first argument
def cli(ctx, verbose, add_count):
    """Simple multi command that will call registered subcommands."""
    # This will run before any subcommand, and only when a subcommand runs
    if verbose:
        click.echo('In verbose mode')
    ctx.add_count = add_count


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.argument('file', type=click.File('w'),
                required=False, default="-")   # - is the stdout File in Linux
@pass_config   # if added it will pass the created shared context as first argument
def hello(ctx, count, name, file):
    """Simple subcommand that greets NAME for a total of COUNT times."""

    # add the "add_count" from the context (e.g. from the main command)
    count = count + ctx.add_count

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
