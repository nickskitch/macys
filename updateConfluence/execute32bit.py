__author__ = 'Nick'
#!/usr/bin/python

# doing it this way seem to crash on my mac.  was hoping to run in 32bit mode so api doesn't crash
from subprocess import Popen, PIPE, STDOUT

cmd = 'arch -i386 /usr/bin/python ./sendMessage.py'

p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
output = p.stdout.read()

# Process the output
print(output)