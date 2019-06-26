import praw
import os
from dotenv import load_dotenv

# Environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")
REDDIT_TEST_ACCOUNT = os.getenv("REDDIT_TEST_ACCOUNT")

# Reddit API init
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

for comment in reddit.redditor(REDDIT_TEST_ACCOUNT).comments.new(limit=None):
    #TODO: Regex that filters anything but natural language
    print(comment.body)