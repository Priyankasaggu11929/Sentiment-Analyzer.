import tweepy
from textblob import TextBlob

##Make a Twitter Developer Account and create an application to obtion the auth_keys and auth_tokens
consumer_key = '#'
consumer_secret = '#'

access_token = '#'
access_token_secret = '#'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
hashtag=input("Enter the topic on which you want to perform sentiment Analysis: \n ")
public_tweets = api.search(hashtag)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
~                                                                     
~                                                                     
~                                                                     
~                                 
