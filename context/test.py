from urllib.request import urlopen

# Common example using open() function
with open('output.txt', 'w') as f:
    f.write('Hi there!')


# Context Manager as a Class - e.g. to be used in "with"
class Closable:
    def __init__(self, thing):
        self._thing = thing

    def __enter__(self):
        # self._thing.enter()
        return self._thing

    def __exit__(self, type, value, traceback):
        self._thing.close()


#  so usage is :
with Closable(urlopen('http://www.python.org')):
    pass

# Context Manager as a Generator - e.g. to be used in "with"

from contextlib import contextmanager


@contextmanager
def closing(thing):
    # thing.enter()
    try:
        yield thing
    finally:
        thing.close()


# and usage is :
with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("foo")
# this will print :
# <h1>
# foo
# </h1>


# Useful staff

# I. suppress
# Temporary suppress the specified exception while in the 'with' statement
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')
with suppress(FileNotFoundError):
    os.remove('someotherfile.tmp')

# equivalent to :
# try:
#     os.remove('somefile.tmp')
# except FileNotFoundError:
#     pass


# I. redirect_stdout, redirect_stderr
# Temporary redirect the out/err to a new place while in the 'with' statement

from contextlib import redirect_stdout, redirect_stderr

with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)


# A base class that enables a context manager to also be used as a decorator.
from contextlib import ContextDecorator


class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

# apply the decorator


@mycontext()
def func():
    print('The bit in the middle')


func()
# this will print:
# Starting
# The bit in the middle
# Finishing

# use as context-manager
with mycontext():
    print('The bit in the middle')

# this will print the same result:
# Starting
# The bit in the middle
# Finishing
