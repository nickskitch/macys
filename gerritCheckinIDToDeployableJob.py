__author__ = 'Nick'
import subprocess
import time

jenkinsJob='NavApp_14G_MCOM_Deploy_'
gerritCheckinID='Added'   #commit id, found in gerrit Patch Set 1
#harish's

cmd = "curl -Ls \'http://buildserver.federated.fds:8080/hudson/job/"+jenkinsJob+"/lastBuild/buildNumber\'"
print cmd
response = int(subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip())
startBuildNumber=response

while True:
    url="http://buildserver.federated.fds:8080/hudson/view/0_NavApp_GitJobs/view/NavApp_Git/view/0_NavApp_14G_Deploy/job/"+jenkinsJob+"/"+ str(startBuildNumber) + "/changes"
    cmd = "curl -Ls \'"+url+"\'" + " | grep " +"'" + gerritCheckinID+"'"
    print cmd
    response = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    if len(response) > 0:
        print "the following build is the first build to contain the dev''s changes: " + url
        exit()
    startBuildNumber-=1
    time.sleep(1)
