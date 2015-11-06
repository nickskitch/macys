import praw
r=praw.Reddit(user_agent='nickbot/1.0 by nicks')
submissions = r.get_subreddit('opensource').get_hot(limit=5)
#[str(x) for x in submissions]