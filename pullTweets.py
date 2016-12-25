from twython import Twython

def main():
    APP_KEY = 'PtIsqf9tSAXqMO1EiwQ1yyWfT'
    APP_SECRET = 'MCaPnJpc2q2bQJgm9yc2U275Tzu98WRyPv1H8tTFYsgfdoYLqC'
    OAUTH_TOKEN = '812765448685154304-GEyoxEGDJzEJsaVLP5uyD4kXYbcY0e2'
    OAUTH_TOKEN_SECRET = 'TnJEyf5pSLay3HqHQ677ocj7ADJMAoMK4y4Twms25kpiC'

    twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#    user_timeline = twitter.get_user_timeline(screen_name="realDonaldTrump",count=20)
#    for tweet in user_timeline:
#        if(tweet['source'] == "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>"):
#            print (tweet['text'])
#            print (tweet['source'])
#            print ()


#    for tweet in twitter.get_home_timeline():
#        print(tweet['text'])

    twitter.update_status(status='beep boop')        
