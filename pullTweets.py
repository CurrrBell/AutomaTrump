from twython import Twython

def main():
    APP_KEY = 'i5yVTADf633De8I7fgjXDh6SY'
    APP_SECRET = 'fVJkx7NvVmZDtMSKDXvaPwfjrRhp2yUkwNfuEMJrYa1C4yKZfB'

    twitter = Twython(APP_KEY, APP_SECRET)

    user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",count=20)
    for tweet in user_timeline:
        if(tweet['source'] == "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"):
            print (tweet['text'])
            print (tweet['source'])
            print ()
