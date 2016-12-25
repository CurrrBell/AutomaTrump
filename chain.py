import re
import random
import string

def main():
    tweetbase = ["The big loss yesterday for Israel in the United Nations will make it much harder to negotiate peace.Too bad, but we will get it done anyway!", "Vladimir Putin said today about Hillary and Dems: \"In my opinion, it is humiliating. One must be able to lose with dignity.\"  So true!", "slaughter you. This is a purely religious threat, which turned into reality. Such hatred! When will the U.S., and all countries, fight back?", "The terrorist who killed so many people in Germany said just before crime, \"by God\'s will we will slaughter you pigs, I swear, we will......", "As to the U.N., things will be different after Jan. 20th.", "my presidency. Isn't this a ridiculous shame? He loves these kids, has raised millions of dollars for them, and now must stop. Wrong answer!", "My wonderful son, Eric, will no longer be allowed to raise money for children with cancer because of a possible conflict of interest with...", "The so-called \"A\" list celebrities are all wanting tixs to the inauguration, but look what they did for Hillary, NOTHING. I want the PEOPLE!", "Based on the tremendous cost and cost overruns of the Lockheed Martin F-35, I have asked Boeing to price-out a comparable F-18 Super Hornet!", ".@FoxNews - \"Objectified\" tonight at 10:00 P.M. Enjoy!"]
    wordCount = {}
    words = []
    tweetStarts = []

    for i in range(len(tweetbase)):
        thisTweet = re.findall(r"[@a-zA-Z0-9\"'-]+|[.,!?;:]|[0-9]+", tweetbase[i])
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



    # for i in wordCount.keys():
    #     print(i, wordCount[i])
    #
    # for i in tweetStarts:
    #     print(i)



    def generateTweet():
        tweet = ""
        tweetStart = tweetStarts[random.randrange(0,len(tweetStarts))]

        print("Tweet start: " + tweetStart)

        currentWord = tweetStart

        while(len(wordCount[currentWord]) > 0 and (len(tweet) + len(currentWord)) < 140):
            nextWord = wordCount[currentWord][random.randrange(0, len(wordCount[currentWord]))]

            if(currentWord in string.punctuation):
                tweet += currentWord
            else:
                tweet += " " + currentWord

            currentWord = nextWord

        print("Tweet: " + tweet)

    generateTweet()
    generateTweet()
    generateTweet()
    generateTweet()
    generateTweet()
