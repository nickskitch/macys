__author__ = 'Nick'
import library
import subprocess
import time
import datetime
import httplib
import urllib2
import requests



def get_status_code(host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

serverCount=0
messages=[]

while True:
    if library.isPingable('google.com'):
        serverName='jira'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        serverName='confluence'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        serverName='mcominternal5024.fds.com'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        serverName='buildserver'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        serverName='wdsgerrit'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        serverName='navapp-gerrit'
        if not library.isPingable(serverName):
            serverCount+=1
            messages.append(serverName +  " is down\n")
        if (serverCount <6) and (serverCount > 0):
            messageText='\n'.join(messages)
            message(messageText)

    #time.sleep(5)
    messages=[]
    serverCount=0
    serverName='mcominternal5024.fds.com'
    if get_status_code(serverName) == 500:
        messages.append(serverName + "is returning a 500 error code")
        serverCount=+1

    if (serverCount <2) and (serverCount > 0):
        messageText='\n'.join(messages)
        message(messageText)
    else:
        print 'everything looks good'


    #try:
    #    t1 = datetime.datetime.now()
    #    urllib2.urlopen("http://wdsgerrit:8080/#/q/status:open,n,z",timeout=1)
    #    t2 = datetime.datetime.now()
    #    test=(t2-t1)
    #    if (test.seconds >= 10):
    #         messages.append('wdsgerrit sluggish')
    #except:
    #    message('error loading wdsgerrit')

    time.sleep(500)

