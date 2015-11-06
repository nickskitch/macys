__author__ = 'Nick'
import praw
import re

regexp_link = r'''</?a((s+w+(s*=s*(?:".*?"|'.*?'|[^'">s]+))?)+s*|s*)/?>w+</a>'''

r = praw.Reddit('Sierra Nevada automation')
user = r.get_redditor('SierraNevada_')
all_comments = user.get_comments(limit=None)


for comment in all_comments:
    print comment.body