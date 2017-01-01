import time
import sched
import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from pullTweets import pullTweets
from chain import chopUpTweet
from newTweet import generateTweet

def main():

    scheduler = sched.scheduler(time.time, time.sleep)



    def randomTweet():
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        tweetSource = pullTweets()

        #now that we have our tweets, we create a new one using Markov Chains


        wordCount = {}
        tweetStarts = []

        for tweet in tweetSource:
            chopUpTweet(wordCount, tweetStarts, tweet)

        generateTweet()

    def schedule_tweet():
        scheduler.enter(0, 1, randomTweet, ())
        scheduler.run()
        print("tweet", time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(random.randrange(21600, 86400))

    while True:
        schedule_tweet()
