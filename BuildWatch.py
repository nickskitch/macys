__author__ = 'Nick'

import os
import time
import subprocess
import re
import sys
#from sendMessageToSkype import messageToSkype


requestId='46001'
sendtoSkype=False
#jsession1=''

global messageToSkypeCount
messageToSkypeCount=0


# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass


def setToken():
    print 'logging in .. '
    global jsession1    # Needed to modify global copy of globvar
    #cmd = 'curl -c -s cookies.txt -d "userLogin.username=' + USERNAME + '&userLogin.password=' + PASS1 + ' http://mdc2vr4073:9090/MacysOrchestration/logout.html'
    cmd = 'curl -sL -c cookies.txt -d "userLogin.username=' + USERNAME + '&userLogin.password=' + PASS1 + '" "http://mdc2vr4073.federated.fds:9090/MacysOrchestration/logout.html"'
    #print cmd
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    cookie=open('cookies.txt', 'r')
    cookieText = '\n'.join(cookie.readlines())
    validHash = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', cookieText)
    result = [match.group(1) for match in validHash]
    jsession1=result[0]
    print 'session id set: ' + jsession1



def message(message):
    #url=r'http://mdc2vr4073:9090/MacysOrchestration/final-status.html?requestId='+requestId+'" -H "Accept-Encoding: gzip,deflate,sdch" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Cookie: JSESSIONID='+jsession1+'; redirectUrl="/MacysOrchestration/env-live-status.html?requestId='+requestId+'" -H "Connection: keep-alive" --compressed'
    killcommand = "kill -9 "+str(os.getpid());

    url=r'http://mdc2vr4073.federated.fds:9090/MacysOrchestration/final-status.html?requestId='+requestId
    cmd2 = "terminal-notifier -title 'buildWatch' -message '" + str(message) + "' -open '" + url + "'" + " -execute '" + killcommand + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

def messageSkype(message,messageToSkypeCount):
    #skype1.topic = 'test'
    if sendtoSkype == True and messageToSkypeCount<1:
        skype1.sendmessage2('mcominternal5024 deployment is done')
        messageToSkypeCount=+1


setToken()
print requestId
while True:
    cmd = 'curl -Ls \'http://mdc2vr4073.federated.fds:9090/MacysOrchestration/env-live-status.html?requestId='+requestId+'\' -H \'Accept-Encoding: gzip,deflate,sdch\' -H \'Accept-Language: en-US,en;q=0.8\' -H \'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36\' -H \'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\' -H \'Cache-Control: max-age=0\' -H \'Cookie: JSESSIONID='+jsession1+'; redirectUrl="/MacysOrchestration/env-live-status.html?requestId='+requestId+'\' -H \'Connection: keep-alive\' --compressed'
    #print cmd
    response = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    #print response
    if len(response)==0:
        print 'session expired; no response'
        setToken()
        continue


    if (response.find('RUNNING')==-1) and (response.find('NOTSTARTED')==-1):
        if 'COMPLETED' in response:
            message('RAPAD ' + requestId +' Completed status detected')
            if (response.find('FAILED')==-1):
               #skype1 = messageToSkype()

               #messageSkype('Deployment complete. Env is up',messageToSkypeCount)
               pass
        if 'FAILED' in response:
            message('RAPAD ' + requestId + ' Failed status detected')
            #messageSkype('Deployment completed')

        #or (response.find('NOTSTARTED')>1))

    sys.stdout.write('.')


    time.sleep(50)