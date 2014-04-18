__author__ = 'Nick'

import time
import subprocess

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass


#curl -c -s cookies.txt -d "userLogin.username=yc14ns1&userLogin.password=nisum2019" http://mdc2vr4073:9090/MacysOrchestration/logout.html




def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()


while True:

    time.sleep(30)