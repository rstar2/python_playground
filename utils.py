import os
pwd = os.getcwd()
print(pwd)
os.chdir('..')
print(pwd)

# ----------

import glob
x = glob.glob('**')
print(x)

# ----------

import sys
print(sys.argv)

# ----------

s = b'witch which has which witches wrist watch'
print(s)