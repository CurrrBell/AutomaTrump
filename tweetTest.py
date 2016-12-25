import re
import random
import string
from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def main():
    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    raw_tweets = twitter.get_user_timeline(screen_name="realDonaldTrump",count=200)

    #only deal with the ones Trump wrote himself

    trump_tweets = []

    for tweet in raw_tweets:
        if(tweet['source'] == "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"):
            trump_tweets.append(tweet['text'])

    #select 30 random tweets to use as our Based

    using_tweets = []

    for i in range(3):
        index = random.randrange(0,len(trump_tweets))
        using_tweets.append(trump_tweets[index])
        print(index)


    #now that we have our tweets, we create a new one using Markov Chains

    wordCount = {}
    words = []
    tweetStarts = []

    for i in range(len(trump_tweets)):
        thisTweet = re.findall(r"[@a-zA-Z0-9'-]+|[.,!?;:]|[0-9]+", trump_tweets[i])
        tweetStarts.append(thisTweet[0])

        for k in thisTweet:
            words.append(k)

    for i in range(len(words)):

        thisWord = words[i]
        nextWord = ""

        if(i < len(words) - 1):
            nextWord = words[i+1]

            if(thisWord in wordCount.keys()):
                wordCount[thisWord].append(nextWord)
            else:
                wordCount[thisWord] = [nextWord]

        else:
            wordCount[thisWord] = []

    #now that we have our word counts, synthesize a tweet

    def generateTweet():
        newTweet = ""
        tweetStart = tweetStarts[random.randrange(0,len(tweetStarts))]
        currentWord = tweetStart
        wordCounter = 1

        while(len(wordCount[currentWord]) > 0 and (len(newTweet) + len(currentWord)) < 140):
            nextWord = wordCount[currentWord][random.randrange(0, len(wordCount[currentWord]))]

            if(currentWord == "." and wordCounter > 1):
                if(random.randrange(0,2) > 0):
                    newTweet += currentWord
                    break
            elif(currentWord in string.punctuation):
                newTweet += currentWord
            else:
                newTweet += " " + currentWord

            currentWord = nextWord
            wordCounter += 1

        #we have our tweet, now we post it

        print(newTweet)

    generateTweet()
