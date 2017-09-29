class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair(3, 4)


print(p) # __str__() output
# (3, 4)

print(repr(p))  # __repr__() output
# Pair(3, 4)

# 1. It is standard practice for the output of __repr__() to produce text such that
# eval(repr(x)) == x.
# If this is not possible or desired, then it is common to create a
# useful textual representation enclosed in < and > instead.
#  For example:
f = open(__file__)
print(repr(f))
# <_io.TextIOWrapper name='d:\\websites\\python\\learn\\python_by_example\\class__repr__.py' mode='r' encoding='cp1252'>

# 2. If no __str__() is defined, the output of __repr__() is used as a fallback.

# 3. The use of format() in the solution might look a little funny, but the format code {0.x}
# specifies the x-attribute of argument 0. So, in the following function, the 0 is actually
# the instance self:

# 4. Specifically, the special !r formatting code indicates that the
# output of __repr__() should be used instead of __str__(), the default.
