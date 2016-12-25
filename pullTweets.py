from twython import Twython
from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def main():


    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",count=20)
    for tweet in user_timeline:
        if(tweet['source'] == "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"):
            print (tweet['text'])
            print (tweet['source'])
            print ()


#    for tweet in twitter.get_home_timeline():
#        print(tweet['text'])

#    twitter.update_status(status='beep boop')
