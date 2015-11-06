__author__ = 'Nick'
import library
import subprocess
import time
import datetime
import httplib
import urllib2
import os, os.path
import sys
import pysftp #pip install pysftp



def rest_call(call,responseContains):
    response = subprocess.Popen(call, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    if responseContains in response:
        print server['name'] + ' rest response looks good'
    else:
        print 'rest response bad ' + response
        messages.append(server['name'] + ' contains and invalid response')


def sftp_login(url, user, password):

    try:
        srv = pysftp.Connection(host=url, username=user, password=password)
        srv.close()
        print 'logging into sftp: ' + server['name']
    except:
        print server['name']+' login error'
        messages.append(server['name'] +  " is down")

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host,timeout=10)
        conn.request("HEAD", path)
        htmlResponse=conn.getresponse().status
        conn.close()
        return htmlResponse
    except StandardError:
        return None

def is_macy_network():
    if library.isPingable('jira') or library.isPingable('buildserver'):
        return True
    else:
        return False

def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()


serverCount=0
messageCount=0
messages=[{message: "", messageCount: messageCount}]


servers=[{'name':'LL2:NavApp', 'uri':'jcie4312','app': 'ping', 'failCounter':0},
        {'name':'cortexica api', 'uri':'curl -s -X POST -F SearchId="10921" -F ApiKey="OG46GI345HIJEFBE56970CE8GR3KRLEBHDY4587FR92DBEVN" -F AppVersion="1.0" -F DeviceName="mobile" --trace-ascii "curl_request.txt" http://apifs-us.cortexica-cloud.com/api/retrievesearch','responseContains':'timeDetail', 'app': 'rest', 'failCounter':0},
        {'name':'cortexica sftp', 'uri':'sftp.cortexica-cloud.com;sftp-user;xAbA#eRa8h','app': 'sftp', 'failCounter':0},
        {'name':'LL2:Legacy', 'uri':'jcie4116','app': 'ping', 'failCounter':0},
        {'name':'LL2:SDP_HOST', 'uri':'jcia5031','app': 'ping', 'failCounter':0},
        {'name':'LL2:SITE-ASYNC-DB2', 'uri':'jcie4185','app': 'ping', 'failCounter':0},
        {'name':'LL2:ASYNC-APP', 'uri':'jcie4365','app': 'ping', 'failCounter':0},
        {'name':'jira',          'uri':'jira','app': 'ping', 'failCounter':0},
        {'name':'confluence', 'uri':'confluence','app': 'ping', 'failCounter':0},
        {'name':'mcomexternal126.fds.com!', 'uri':'mcomexternal126.fds.com','app': 'webserver', 'failCounter':0},
        {'name':'buildserver', 'uri':'buildserver','app': 'ping', 'failCounter':0},
        {'name':'wdsgerrit', 'uri':'wdsgerrit','app': 'ping', 'failCounter':0},
        {'name':'navapp-gerrit', 'uri':'navapp-gerrit','app': 'ping', 'failCounter':0},
]


# ensure we are only ever running one copy of this script
library.singleton(__file__)


while True:
    if is_macy_network():
        for server in servers:
            if 'ping' in server['app']:
                print 'pinging '+server['name']
                if not library.isPingable(server['uri']):
                    server['failCounter'] = server['failCounter']+1
                    serverCount+=1
                    print str(serverCount)
                    messages.append(server['name'] +  " is down\n")
            if 'rest' in server['app']:
                rest_call(server['uri'],server['responseContains'])
            if 'sftp' in server['app']:
                sftp_login(server['uri'].split(';')[0],server['uri'].split(';')[1],server['uri'].split(';')[2])
            if 'webserver' in server['app']:
                responseCode = get_status_code(server['uri'])
                if (responseCode <> 200):
                    server['failCounter'] = server['failCounter']+1
                    serverCount+=1
                    messages.append(server['name'] + ' returning html response code: '+str(responseCode))


    # not currently using this
    for server in servers:
        server['failCounter']=0


    # only msg me if it's not all servers down
    if is_macy_network() and len(messages)>0:
        for msg in messages:
            message(msg)
            time.sleep(5)
    else:
        print 'everything looks good'

    messages=[]
    serverCount=0

    #try:
    #    t1 = datetime.datetime.now()
    #    urllib2.urlopen("http://wdsgerrit:8080/#/q/status:open,n,z",timeout=1)
    #    t2 = datetime.datetime.now()
    #    test=(t2-t1)
    #    if (test.seconds >= 10):
    #         messages.append('wdsgerrit sluggish')
    #except:
    #    message('error loading wdsgerrit')

    time.sleep(2000)

