import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from pullTweets import pullTweets
from chain import populateWordMap

def main():
    for i in range(10):
        generateTweet()

def generateTweet():
    DEBUG = False
    MAX_CHARS = 280
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    automaTweets = twitter.get_user_timeline(screen_name="AutomaTrump",count=200,tweet_mode='extended')
    tweetSource = pullTweets()

    #now that we have our tweets, we create a new one using Markov Chains

    wordMap = {}
    tweetStarts = []

    for tweet in tweetSource:
        populateWordMap(wordMap, tweetStarts, tweet)


    #now that we have our word counts, synthesize a tweet

    newTweet = ""

    while(len(newTweet) == 0):
        newTweet = assembleTweet(wordMap, tweetStarts, MAX_CHARS).strip()
        for tweet in automaTweets:            
            if(tweet['full_text'] == newTweet):
                print("Already tweeted this, regenerating.")
                newTweet = ""
                break

    #we have our tweet, now we post it

    if(DEBUG):
        print(newTweet)
        print(len(newTweet))
    else:
        twitter.update_status(status=newTweet)

def assembleTweet(wordMap, tweetStarts, MAX_CHARS):
    newTweet = ""
    tweetStart = tweetStarts[random.randrange(0,len(tweetStarts))]
    currentWord = tweetStart
    possibleCrossovers = 0

    while(len(wordMap[currentWord]) > 0):
        nextWord = getRandomNextWord(wordMap, currentWord)

        if(len(wordMap[currentWord]) > 1):
            possibleCrossovers += len(wordMap[currentWord])

        if(currentWord in string.punctuation):
            newTweet += currentWord
        else:
            newTweet += " " + currentWord

        if(isChainTerminated(currentWord, nextWord)):
            break

        currentWord = nextWord

    #check to make sure we haven't gone off the edge and we've had enough variety

    if(len(newTweet) > MAX_CHARS):
        print("Assembling new tweet. Length: " + str(len(newTweet)))
        newTweet = ""
        #assembleTweet(wordMap, tweetStarts, MAX_CHARS)

    if(possibleCrossovers < 5):
        print("Assembling new tweet. Crossovers: " + str(possibleCrossovers))
        newTweet = ""
        #assembleTweet(wordMap, tweetStarts, MAX_CHARS)


    # if(len(newTweet) > MAX_CHARS or possibleCrossovers < 5):
    #     assembleTweet(wordMap, tweetStarts, MAX_CHARS)

    return newTweet

def getRandomNextWord(wordMap, currentWord):
    return wordMap[currentWord][random.randrange(0, len(wordMap[currentWord]))]

def checkCrossovers(possibleCrossovers, wordMap, currentWord):
    if(len(wordMap[currentWord]) > 1):
        possibleCrossovers += len(wordMap[currentWord])

def isChainTerminated(currentWord, nextWord):
    #if we're on a punctuation that isn't part of the word "U.S.", end our tweet
    return nextWord == "EOF" or (currentWord.endswith(".") and currentWord != "U.S.") or currentWord.endswith("!") or currentWord.endswith("?")