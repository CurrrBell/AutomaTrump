import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def pullTweets():

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    raw_tweets = twitter.get_user_timeline(screen_name="realDonaldTrump",count=200)

    #get the first 50 tweets Trump wrote himself

    trump_tweets = []

    for tweet in raw_tweets:

        if(tweet['source'] == "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>" and tweet['text'][0].isupper()):
            trump_tweets.append(tweet['text'])

    #randomly select 5 tweets from these to mash up

    using_tweets = []

    while(len(using_tweets) < 5):
        index = random.randrange(0,len(trump_tweets))
        if(trump_tweets[index][-2:] != ".."):
            using_tweets.append(trump_tweets[index])

    return using_tweets
