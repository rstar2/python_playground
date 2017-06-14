import subprocess
import time

proc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')

#  this will return right now the exit code of the process
# (0 is for success, all others are some kind of error)
retult = proc.poll()

# this will block until subprocess is terminated
retsult = proc.wait()

# Passing argulments -> use list
subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])

# Using OS default/associated programs to open files (as if double-clicked on them)
# for Windows - use 'start'  with shell=True
# for Mac     - use 'open'
# for Linux   - use 'see'

subprocess.Popen(['start', 'hello.txt'], shell=True)
