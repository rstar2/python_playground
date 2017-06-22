# Function annotations are a Python 3 feature that lets you add arbitrary metadata
# to function arguments and return value.
# They were part of the original Python 3.0 spec.
# Default arguments are specified after the annotation:

# https://code.tutsplus.com/tutorials/python-3-function-annotations--cms-25689


def foo(a, b: 'annotating b', c: int,
        d: 'an argument that defaults to 5' = 5) -> float:
    print(a + b + c)


foo('Hello', ', ', 'World!')
foo(1, 2, 3)

# -----------------------------
# Accessing Function Annotations - it is a Dictionary type

print(foo.__annotations__) 
# {'b': 'annotating b', 'c': <class 'int'>, 'd': 'an argument that defaults to 5', 'return': <class 'float'>}

for name, annotation in foo.__annotations__.items():
    print(name, annotation)

# -----------------------------
# Dynamic Annotations - Annotations are just a dict attribute of a function.

def add(a, b) -> 0:
    result = a + b
    add.__annotations__['return'] += result
    return result