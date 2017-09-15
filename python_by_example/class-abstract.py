from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 1. cannot create instacnces of an abstract class

try:
    a = IStream()
except:
    # TypeError: Can't instantiate abstract class
    # IStream with abstract methods read, write
    pass

# 2. Type checking is OK

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


ss = SocketStream()
isinstance(ss, IStream)
# Returns True

# 3. Even other outside classes can be "registered"
# as implementing the same interface

import io

# Register the built-in I/O classes as supporting our interface
IStream.register(io.IOBase)
# Open a normal file and type check
f = open('foo.txt')
isinstance(f, IStream)
# Returns True