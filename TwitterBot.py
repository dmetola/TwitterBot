import tweepy
import time

auth = tweepyAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
            time.sleep(300)

#Liking Block
        
search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#Retweeting Block

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.retweet()
        print('I retweeted that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
