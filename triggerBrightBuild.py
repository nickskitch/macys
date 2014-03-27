#!/usr/bin/env python

import jenkins
from datetime import datetime

username = 'da-MCOM-WDSDevOps'
password = 'ph8pumaK95he'
base_url='http://11.120.101.188:8080/jenkins/'
j = jenkins.Jenkins(base_url, username, password)

#j.build_job('MCOM_Dev_WishList', {'daServiceAccountUser': 'da-MCOM-WDSDevOps', 'daServiceAccountPasswd': 'ph8pumaK95he', 'targetEnv': 'mcominternal5024', 'project': 'Wishlist', 'tags': '@14C', 'gitBranch': 'master'})


f = open('triggerBrightBuildHistory.txt','a')
f.write('\nexecuted at: ' + '{:%Y-%m-%d %I:%M%p}'.format(datetime.now()))
f.close()
