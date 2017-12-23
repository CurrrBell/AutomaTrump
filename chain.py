import re
import random
import string

def populateWordMap(wordMap, tweetStarts, tweet):
    wordsInTweet = re.findall(r"\b[A-Z][a-zA-Z\.]*[A-Z]\b\.?|[0-9:0-9]+|[@a-zA-Z0-9'-_]+|[.,!?;:]", tweet)
    if(wordsInTweet[0] == "."):
        tweetStarts.append(wordsInTweet[1])
    else:
        tweetStarts.append(wordsInTweet[0])

    for i in range(len(wordsInTweet)):
        thisWord = wordsInTweet[i]
        nextWord = "EOF"

        if(i < len(wordsInTweet) - 1): #if we're not actually at the end of the tweet
            nextWord = wordsInTweet[i+1]

        if(thisWord in wordMap.keys()):
            wordMap[thisWord].append(nextWord)
        else:
            wordMap[thisWord] = [nextWord]

        if(nextWord == "EOF"):
            break
