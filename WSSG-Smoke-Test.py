__author__ = 'Nick'

# attempt to read in credentials from file that will not be checked in to vcs
import os
import sys
import subprocess
import json
import requests
from time import *
from datetime import datetime


try:
   from dev_settings import *
except ImportError:
   pass


def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

env='mcomexternal109.fds.com'

url='http://services.'+env+'/v1/app/version'


payload = {'feedbackPageName': 'VisualSearch', 'feedbackPageVersion': '1', 'userId': '2156387656','feedbackDescription': 'testing feedback api'}
headers = {'x-macys-webservice-client-id': 'testclient_1.0_kweu3w323a','x-macys-customer-id':'testclient_1.0_kweu3w323a','Accept':'application/json','Content-Type':'application/json'}
r = requests.get(url, headers = headers)
print url
#print r.content

data=json.loads(r.content)
#data = json.load(json_data)

print '\n'
print 'POM version of WSSG: '+data['pomVersion']
print 'Build timestamp: '+data['timestamp']


