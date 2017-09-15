
# To allow multiple constractor - use "class methods"

import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# use the primary constractor
date = Date(1977, 9, 21)

# use the other constractor through the class method
date_now = Date.today()


# 2. use class-methods and not static-methods
# as class-methods work well with inheritance

class NewDate(Date):
    pass


# Creates an instance of Date (cls=Date)
date_obj = Date.today()

# Creates an instance of NewDate (cls=NewDate)
newdate_obj = NewDate.today()
