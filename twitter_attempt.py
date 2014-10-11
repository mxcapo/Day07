import twitter
import os

api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=os.environ.get('TWITTER_API_KEY'), consumer_secret=os.environ.get('TWITTER_API_SECRET'),
    access_token_key=os.environ.get('TWITTER_ACCESS_TOKEN'), access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))