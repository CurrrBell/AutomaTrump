import re
import random
import string

def chopUpTweet(wordCount, tweetStarts, tweet):
    wordsInTweet = re.findall(r"[@a-zA-Z0-9'-]+|[.,!?;:]|[0-9]+", tweet)
    if(wordsInTweet[0] == "."):
        tweetStarts.append(wordsInTweet[1])
    else:
        tweetStarts.append(wordsInTweet[0])

    for i in range(len(wordsInTweet)):
        thisWord = wordsInTweet[i]
        nextWord = "EOF"

        if(i < len(wordsInTweet) - 1): #if we're not actually at the end of the tweet
            nextWord = wordsInTweet[i+1]

        if(thisWord in wordCount.keys()):
            wordCount[thisWord].append(nextWord)
        else:
            wordCount[thisWord] = [nextWord]

        if(nextWord == "EOF"):
            break
