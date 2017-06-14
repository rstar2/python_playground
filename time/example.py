
import time


# the Unix epoch (12 AM on January 1, 1970 UTC) timestamp - in seconds
time.time()

#  make the thread sleep AND BLOCK for certain seconds
time.sleep(2)


# ------------------------------
# Using datetime

import datetime

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)

halloween2015 == oct31_2015 # True
halloween2015 > newyears2016 # False

now = datetime.datetime.now()
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

now2 = datetime.datetime.fromtimestamp(time.time())

# ------------------------------
# Using timedelta

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

#  arithmetic
thousandDays = datetime.timedelta(days=1000)
now = datetime.datetime.now()
later = now + thousandDays

# ------------------------------
# Converting/Formatting dates

# formatting: date -> string
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S')) # '2015/10/21 16:29:00'
print(oct21st.strftime('%I:%M %p'))          # '04:29 PM'
print(oct21st.strftime("%B of '%y"))         # "October of '15"

# parsing: string-> date
parsedDt = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(parsedDt)
