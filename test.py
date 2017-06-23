import numpy

print(r'C:\some\name')

x = numpy.array([1, 2, 3, 4])
print(x)
print(type(x))

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print(w)


l = [1, 2, 3, 4, 5]
print(len(l))
l.remove(3)
print(len(l))


def f(a, L=None):
    """ Dummy """
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(1, [2, 3]))


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000, 'dasdasd')
