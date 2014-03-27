#!/usr/bin/python

import sys, string, xmlrpclib, re
from datetime import datetime

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass

pageid = '56001477'
server = xmlrpclib.ServerProxy('http://confluence/rpc/xmlrpc')
token = server.confluence1.login(USERNAME, PASS1)
page = server.confluence1.getPage(token, pageid)
if page is None:
   exit("Could not find page " + pageid);

content = page['content'];

content = content + '\n|' + '{:%Y-%m-%d %I:%M%p}'.format(datetime.now()) + ' | 2.30.574 | | 2.31.271 | 1.26.783 |'
print content

pattern = re.compile('^\|\|.*\n(?!\|)', re.MULTILINE);
content = pattern.sub('\g<0>' + content + '\n', content);

page['content'] = content;
server.confluence1.storePage(token, page);