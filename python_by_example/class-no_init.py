# A bare uninitialized instance can be created
# by directly calling the __new__() method
# of a class. For example, consider this class:


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# using the __init__
date_init = Date(1977, 9, 21)

# bypassing __init__
date_no_init = Date.__new__(Date)

# note - it will not have attributes like 'year', 'month', 'day'
# they have to be attached additionally
date_no_init.year = 1977
date_no_init.month = 9
date_no_init.day = 21

# 1. useful for constracting from serialized data
d = Date.__new__(Date)
data = {'year': 2012, 'month': 8, 'day': 29}
for key, value in data.items():
    setattr(d, key, value)

# 2. or for when creatting addional constractors

from time import localtime


class DateTwo:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


date_today = Date.today()
