__author__ = 'Nick'
import praw
import re
import sys

#http://www.reddit.com/r/AskReddit/comments/hywsk/what_is_your_way_of_making_money_on_the_side/
r = praw.Reddit('Sierra Nevada automation')
submission = r.get_submission(submission_id='2517xc')


flat_comments = praw.helpers.flatten_tree(submission.comments)


submission.replace_more_comments(limit=None, threshold=0)
flat_comments = praw.helpers.flatten_tree(submission.comments)

for comment in flat_comments:
    #print comment.body
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', comment.body)
    #print len(urls)
    #print urls
    for item in urls:
        print item
        sys.stdout.write('.')
