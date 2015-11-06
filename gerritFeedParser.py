__author__ = 'Nick'
import feedparser

import time

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass



#http://wdsgerrit:8080/gitweb?p=MacysUI.git;a=search;h=refs/heads/14D;s=Mark+Blomberg;st=author
lastSummaryText=''
currentSummaryText=''
authors=[
{"name": "Mark+Blomberg", "lastSummaryText": ""},
{"name": "Harish+Madathil", "lastSummaryText": ""}
]


while True:
    for author in authors:

        print author['name']
        url = 'http://wdsgerrit:8080/gitweb?p=MacysUI.git;a=search;h=refs/heads/'+BRANCH+';s=' + author['name'] + ';st=author;a=rss'
        print url
        f = feedparser.parse(url)

        for e in f['entries']:
            currentSummaryText=e.get('summary', '')
            print('hi')
            break
        print currentSummaryText
        if currentSummaryText <> author['lastSummaryText']:
            author['lastSummaryText'] = currentSummaryText
            print author['lastSummaryText']


    time.sleep(5)


