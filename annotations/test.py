# Function annotations are a Python 3 feature that lets you add arbitrary metadata
# to function arguments and return value.
# They were part of the original Python 3.0 spec.

def foo(a, b: 'annotating b', c: int) -> float:
    print(a + b + c)

foo('Hello', ', ', 'World!') 
foo(1, 2, 3)   

# Default arguments are specified after the annotation:

def bar(x: 'an argument that defaults to 5' = 5):
    print(x)



bar(7)
bar() 