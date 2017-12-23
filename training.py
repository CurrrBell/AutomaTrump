import csv, sys

from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET


def getTweetsToTrain():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    raw_tweets = twitter.get_user_timeline(screen_name="realDonaldTrump",count=200)
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


    for tweet in raw_tweets:
        print(tweet['text'].translate(non_bmp_map) + ", " + str(len(tweet['entities']['hashtags']) > 0) + ", " + str(len(tweet['entities']['urls']) > 0) + ", " + str(len(tweet['entities']['user_mentions']) > 0))
