import weakref
import gc

#  just a simple class for creating objects/references
class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


# create a reference
a = A(10)

# create weakref map
d = weakref.WeakValueDictionary()

d['primary'] = a            # does not create a reference
print(d['primary'])         # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

# print(d['primary'])         # entry was automatically removed

#  ---------------------------------------

# creating a weakref from exsiting referant
class Object:
    pass

# creat referance
o = Object()

# creat weakref
r = weakref.ref(o)

# get a refrence if still alive
o2 = r()
o is o2    # True

#  remove all referances to the specific referant
del o, o2

# get a new refrence to the referenat if still alive - will not be in this case as no references are 
o3 = r()    # will be None
print(o3)