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



url='http://mdc2vr4074:9999/MacysOrchestrationRestApi/orchestrationService/addOrchestration'


payload = {
    "OrchestratorBO": {
        "userId": "yc14ns1",
        "release": "14F",
        "environmentType": "vCloud",
        "site": "mcomexternal113",
        "apolloJboss": "jcia6213",
        "sdpJboss": "jcia5129",
        "jiraNumber": "",
        "product": "MCOM",
        "stage": "NOTREQUIRED",
        "operation": {
            "deployRecycle": "true",
            "customDate": "false",
            "test": "false"
        },
        "applications": [
            {
                "moduleName": "NavApp",
                "version": "2.34.353",
                "properties": "true",
                "assets": "true",
                "code": "true",
                "recycle": "false",
                "sdpServer": "jcia5129",
                "sdpPort": "8080",
                "is_uDeploy": "false"
            }
        ]
    }
}


headers = {'Accept':'application/json','Content-Type':'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print url
#print r.content
print r.content

#data=json.loads(r.content)
#data = json.load(json_data)







