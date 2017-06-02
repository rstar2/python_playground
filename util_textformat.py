import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]


# The pprint module offers more sophisticated control over printing both
# built-in and user defined objects in a way that is readable by the interpreter.
# When the result is longer than one line, the “pretty printer” adds line breaks
# and indentation to more clearly reveal data structure:
pprint.pprint(t, width=50)

print("----------------")

# ---------------

import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

# The textwrap module formats paragraphs of text to fit a given screen width:
print(textwrap.fill(doc, width=40))