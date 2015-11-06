#!/usr/bin/env python

import jenkins
from datetime import datetime


# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass


username = SERVICE_USERNAME
password = SERVICE_PASSWORD
base_url='http://11.120.101.188:8080/jenkins/'
j = jenkins.Jenkins(base_url, username, password)


j.build_job('MCOM_Dev_WishList', {'daServiceAccountUser': 'da-MCOM-WDSDevOps', 'daServiceAccountPasswd': 'ph8pumaK95he', 'targetEnv': 'mcominternal5024', 'project': 'Wishlist', 'tags': '@'+ BRANCH, 'gitBranch': 'master'})


f = open('/Users/Nick/scripts/macys/triggerBrightBuildHistory.txt','a')
f.write('\nexecuted at: ' + '{:%Y-%m-%d %I:%M%p}'.format(datetime.now()))
f.close()
