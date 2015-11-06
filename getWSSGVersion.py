# attempt to read in credentials from file that will not be checked in to vcs
import os
import sys
import subprocess

try:
   from dev_settings import *
except ImportError:
   pass


def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

env='mcomexternal116.fds.com'




url = 'http://services.'+ env +'/v2/utility/feedback'
headers=' -H "x-macys-webservice-client-id: testclient_1.0_kweu3w323a"' + ' -H "x-macys-customer-id: testclient_1.0_kweu3w323a"' + ' -H "Accept: application/json"' + ' -H "Content-Type: application/json"'
url = url + headers

curl=r"curl -s " + url
print curl
response = subprocess.Popen(curl, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

print response

