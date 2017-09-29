# You want an object to support customized formatting through the format() function
# and string method.


# So overwite the __format__ method

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __format__(self, code):
        if code == '':
            code = 'full'

        if code == 'full':
            return '{0.name} {0.last_name}'.format(self)
        elif code == 'last':
            return self.last_name
        else:
            return self.name


person = Person('Rumen', 'Neshev')


print('Here was {}'.format(person))
print('Here was {:last}'.format(person))
print('Here was {:bug}'.format(person))

# or
print(format(person))
print(format(person, 'last'))
print(format(person, 'bug'))

# readl Python example is :
from datetime import date
d = date(2012, 12, 21)

format(d)
# '2012-12-21'

format(d, '%A, %B %d, %Y')
# 'Friday, December 21, 2012'

'The end is {:%d %b %Y}. Goodbye'.format(d)
# 'The end is 21 Dec 2012. Goodbye'
