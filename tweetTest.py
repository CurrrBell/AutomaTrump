import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from pullTweets import pullTweets
from chain import chopUpTweet

def main():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tweetSource = pullTweets()

    #now that we have our tweets, we create a new one using Markov Chains


    wordCount = {}
    tweetStarts = []

    for tweet in tweetSource:
        chopUpTweet(wordCount, tweetStarts, tweet)


    #now that we have our word counts, synthesize a tweet

    #now that we have our word counts, synthesize a tweet

    def generateTweet():
        newTweet = ""
        tweetStart = tweetStarts[random.randrange(0,len(tweetStarts))]
        currentWord = tweetStart

        while(len(wordCount[currentWord]) > 0 and (len(newTweet) + len(currentWord)) < 140):
            nextWord = wordCount[currentWord][random.randrange(0, len(wordCount[currentWord]))]

            if(currentWord in string.punctuation):
                newTweet += currentWord
            else:
                newTweet += " " + currentWord

            if(nextWord == "EOF" or currentWord.endswith(".") or currentWord.endswith("!") or currentWord.endswith("?")):
                break

            currentWord = nextWord

        #we have our tweet, now we post it

        print(newTweet)

    generateTweet()
    generateTweet()
    generateTweet()
    generateTweet()
    generateTweet()
    
