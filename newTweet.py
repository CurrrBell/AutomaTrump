import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from pullTweets import pullTweets
from chain import chopUpTweet

def generateTweet():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tweetSource = pullTweets()

    #now that we have our tweets, we create a new one using Markov Chains


    wordCount = {}
    tweetStarts = []

    for tweet in tweetSource:
        chopUpTweet(wordCount, tweetStarts, tweet)


    #now that we have our word counts, synthesize a tweet

    newTweet = ""
    tweetStart = tweetStarts[random.randrange(0,len(tweetStarts))]
    currentWord = tweetStart
    possibleCrossovers = 0

    while(len(wordCount[currentWord]) > 0 and (len(newTweet) + len(currentWord))):
        nextWord = wordCount[currentWord][random.randrange(0, len(wordCount[currentWord]))]

        if(len(wordCount[currentWord]) > 1):
            possibleCrossovers += len(wordCount[currentWord])

        if(currentWord in string.punctuation):
            newTweet += currentWord
        else:
            newTweet += " " + currentWord

        if(nextWord == "EOF" or (currentWord.endswith(".") and currentWord != "U.S.") or currentWord.endswith("!") or currentWord.endswith("?")):
            break

        currentWord = nextWord

    #check to make sure we haven't gone off the edge and we've had enough variety

    if(len(newTweet) > 140 or possibleCrossovers < 5):
        generateTweet()

    #we have our tweet, now we post it

    twitter.update_status(status=newTweet)
    #
    # generateTweet()
