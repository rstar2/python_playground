# Making an N-Argument Callable Work As a Callable with Fewer Arguments

# If you need to reduce the number of arguments to a function, you should use func
# tools.partial() . The partial() function allows you to assign fixed values to one or
# more of the arguments, thus reducing the number of arguments that need to be supplied
# to subsequent calls.

from functools import partial

# The new callable accepts the still unassigned arguments, combines them
# with the arguments given to partial() , and passes everything to the original function.


def spam(a, b, c, d):
    print(a, b, c, d)


spam_fixed = partial(spam, "A") # a = "A"
# this will be as if spam("Fixed",2,3,4)
spam_fixed(2, 3, 4)
# A 2 3 4


spam_fixed_d = partial(spam, d="D") # d = "D"
# this will be as if spam("Fixed",2,3,4)
spam_fixed_d(2, 3, 4)
# 2 3 4 D

spam_fixed_more = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
spam_fixed_more('3')
# 1 2 3 42