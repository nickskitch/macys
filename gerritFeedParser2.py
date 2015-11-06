__author__ = 'Nick'

import copy
import time
import library
from xml.etree import ElementTree as ET
import subprocess
from bs4 import BeautifulSoup

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass


def message(message):
    cmd2 = "terminal-notifier -message '" + str(message) + "'"
    print cmd2
    subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

#http://wdsgerrit:8080/gitweb?p=MacysUI.git;a=search;h=refs/heads/14D;s=Mark+Blomberg;st=author
lastSummaryText=''
firstPassDone=False
userSearchText='racfid'

repositories=[
    {"name":"MacysUI.git", "summary":""},
    {"name":"NavApp.git", "summary":""},
    {"name":"ShopNServe.git", "summary":""},
]

authors=[
{"name": "Mark Blomberg","RACFID":"m453584","lookup method":"name", "lasttext":{}},
{"name": "Harish Madathil","RACFID":"m458956",'lookup method':'name','lasttext': {}},
{"name": "Karthik Maddu","RACFID":"yc05k1m",'lookup method':'name','lasttext': {}},
{"name": "Vijay Khurana","RACFID":"m615408",'lookup method':'name','lasttext': {}},
]

for author in authors:
    reposCopy = copy.deepcopy(repositories)
    author['lasttext'] = reposCopy




while True:
    for author in authors:
        for repo in author['lasttext']:
            time.sleep(5)
            if firstPassDone : time.sleep(15)

            if author['lookup method'] == 'name':
                userSearchText=str.replace(author['name']," ","+")
            else:
                userSearchText=author['RACFID']
            url ="'http://wdsgerrit:8080/gitweb?p="+repo['name']+";a=search;h=refs/heads/"+BRANCH+";s="+ userSearchText +";st=author' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Connection: keep-alive' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36' -H 'Cache-Control: max-age=0' --compressed"
            curl=r"curl -s " + url
            print curl
            response = subprocess.Popen(curl, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
            if len(response)>0:
                print response[1:300]

                parsed_html = BeautifulSoup(response)
                try:
                    currentSummaryText = parsed_html.body.find('a', {'class':'list subject'}).text
                    print author['name']+' '+currentSummaryText
                except:
                    print time.strftime('%H:%m') + ' exception in bs:'+ author['name']+' '+currentSummaryText
                    break

                if currentSummaryText <> repo['summary']:
                    repo['summary'] = currentSummaryText
                    if firstPassDone:
                        message=str(author['name']) +' checked in to: ' + str(repo['name']) + '< ' + str(repo['summary'])
                        print message
                        message(message)
            else:
                print "no response; no internet?"

    firstPassDone=True
    time.sleep(5)


