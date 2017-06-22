# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html

# https://code.tutsplus.com/tutorials/deep-dive-into-python-decorators--cms-25629
# https://code.tutsplus.com/tutorials/write-your-own-python-decorators--cms-25630


# Using functions

def entry_exit(f):
    def decorated(*args, **kwargs):
        print("Entering", f.__name__)
        result = f(*args, **kwargs)
        print("Exited", f.__name__)
        return result
    return decorated


@entry_exit
def foo():
    print("inside foo()")


foo()


# -------------------
# Using Classes - create a class that is Callabale , e.g. hash "call" attribute (__call__)

class entry_exit_ex(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Entering", self.f.__name__)
        result = self.f(*args, **kwargs)
        print("Exited", self.f.__name__)
        return result


@entry_exit_ex
def bar():
    print("inside bar()")


bar()

# -------------------------
# adding arguments to the decorators

import time


def minimum_runtime(t):
    def decorated(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            runtime = time.time() - start
            if runtime < t:
                time.sleep(t - runtime)
            return result
        return wrapper
    return decorated


def multiply(x, y):
    print(x * y)


@minimum_runtime(1)
def slow_multiply(x, y):
    multiply(x, y)


@minimum_runtime(3)
def slower_multiply(x, y):
    multiply(x, y)

# -------------------------
# Python 3 class decorators - annotate a whole class,
# which is the same as if each its method is decorated


def authorized(f):
    def decorated(*args, **kwargs):
        print("Entering", f.__name__)
        result = f(*args, **kwargs)
        print("Exited", f.__name__)
        return result
    return decorated


@authorized
class MyClass(object):
    def f_1(self):
        pass

    def f_2(self):
        pass

    def f_3(self):
        pass


# --------------
#  some built-in decorators

class A(object):
    @classmethod
    def foo(cls):
        print(cls.__name__)

    @staticmethod
    def bar():
        print('I have no use for the instance or class')


A.foo()
A.bar()
