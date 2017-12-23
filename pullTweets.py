import re, random, string, json, sys
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def pullTweets():

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    rawTweets = twitter.get_user_timeline(screen_name="realDonaldTrump",count=200,tweet_mode='extended')

    trumpTweets = []

    for tweet in rawTweets:

        tweetText = tweet['full_text']

        if(isTrumpTweet(tweet)):
            trumpTweets.append(tweetText)

    #randomly select 5 tweets from these to mash up

    tweetsToUse = []

    while(len(tweetsToUse) < 5):
        index = random.randrange(0,len(trumpTweets))
        if(not isMultiTweetRant(trumpTweets[index])):
            tweetsToUse.append(trumpTweets[index])

    return tweetsToUse


def isMultiTweetRant(text):
    return text[-2:] == ".."

def isProperSentence(text):
    return text[0].isupper()

def isTrumpStaff(tweet):
    return len(tweet['entities']['hashtags']) > 0 or ("media" in tweet['entities'].keys())

def isTrumpTweet(tweet):
    if(not isProperSentence(tweet['full_text'])):
        return False

    if(tweet['is_quote_status'] or ("retweeted_status" in tweet.keys()) or ("possibly_sensitive" in tweet.keys())):        
        return False

    if(isTrumpStaff(tweet)):
        return False

    return True

