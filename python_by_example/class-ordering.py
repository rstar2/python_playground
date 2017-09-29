# Python classes can support comparison by implementing a special method for each
# comparison operator. For example, to support the >= operator, you define a __ge__()
# method in the classes. Although defining a single method is usually no problem, it
# quickly gets tedious to create implementations of every possible comparison operator.

# ( __eq__, __lt__ , __le__ , __gt__ , or __ge__ )


# The functools.total_ordering decorator can be used to simplify this process. To use
# it, you decorate a class with it, and define __eq__() and one other comparison method
# ( __lt__ , __le__ , __gt__ , or __ge__ ). The decorator then fills in the other comparison
# methods for you.

from functools import total_ordering


@total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    @property
    def square_feet(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.square_feet == other.square_feet

    def __ge__(self, other):
        return self.square_feet >= other.square_feet


roomA = Room("One", 10, 10)
roomB = Room("One", 10, 20)
print(roomA.square_feet)
print(roomB.square_feet)
print(roomA >= roomB)
print(roomA < roomB)
