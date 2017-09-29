# In general, a descriptor is an object attribute with “binding behavior”,
# one whose attribute access has been overridden by methods in the descriptor protocol.
# Those methods are __get__(), __set__(), and __delete__(). If any of those methods
# are defined for an object, it is said to be a descriptor.
# 
# The default behavior for attribute access is to get, set, or delete the attribute
# from an object’s dictionary.
# For instance, a.x has a lookup chain starting with a.__dict__['x'],
# then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.
# If the looked-up value is an object defining one of the descriptor methods,
# then Python may override the default behavior and invoke the descriptor method instead.
# Where this occurs in the precedence chain depends on which descriptor methods were defined.

# If an object defines both __get__() and __set__(), it is considered a data descriptor.
# Descriptors that only define __get__() are called non-data descriptors.
# Data and non-data descriptors differ in how overrides are calculated with respect to
# entries in an instance’s dictionary:
# !!! If an instance’s dictionary has an entry with the same name as a data descriptor,
#     the data descriptor takes precedence.
#     If an instance’s dictionary has an entry with the same name as a non-data descriptor,
#     the dictionary entry takes precedence.

# ############
# To use a descriptor, instances of the descriptor are placed into a class definition as class
# variables. For example:

# class Book:
#     price = Price()
# b = Book()   

# 1. When we try to evaluate b.price and retrieve the value,
# Python recognizes that price is a descriptor and calls Book.price.__get__.
# 2. When we try to change the value of the price attribute, e.g. b.price = 23 ,
# Python again recognizes that price is a descriptor and substitutes the assignment with a call to Book.price.__set__.
# 3. When we try to delete the price attribute stored against an instance of Book,
# Python automatically interprets that as a call to Book.price.__delete__.

# ############


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point(2, 3, 4)



p.x        # Calls Point.x.__get__(p,Point)
p.y = 5    # Calls Point.y.__set__(p, 5)

p.z = "#$#$#"

p.x = 2.3  # Calls Point.x.__set__(p, 2.3)
# this will throw exceptions