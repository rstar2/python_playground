x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10), b(10), sep=',')
# result is 30,30

# The problem here is that the value of x used in the lambda expression is a free variable
# that gets bound at runtime, not definition time. Thus, the value of x in the lambda
# expressions is whatever the value of the x variable happens to be at the time of execution.

# a = lambda y: x + y
# is equal to :
# def a(y): return x + y
# Now the problem is visible - x is avaluated at runtime


# If you want an anonymous function to capture a value at the point of definition and
# keep it, include the value as a default value, like this:
# The functions now capture the value of n at the time of definition.
x = 10
c = lambda y, x=x : x + y
x = 20
d = lambda y, x=x : x + y

print(c(10), d(10), sep=',')
# result is 20,30


# Similar problem - TOO clever code:
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))
# 4
# 4
# 4
# 4
# 4

# Solution : 
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
# 0
# 1
# 2
# 3
# 4