import csv
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET


def getTweetsToTrain():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    raw_tweets = twitter.get_user_timeline(screen_name="realDonaldTrump",count=200)

    for tweet in raw_tweets:
        print(tweet['id_str'] + ", " + len(tweet['entities']['hashtags']).toString())
