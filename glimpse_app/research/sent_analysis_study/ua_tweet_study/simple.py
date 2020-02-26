# import tweet crawler modules
import tweepy
import csv
import numpy as np
import pandas as pd

def get_tweets():
# twitter dev credentials here:
    consumer_key = 'sDWaGkbuFxWBWIjlcDziP9Y3K'
    consumer_secret = 'TipNqpxvHD4D9MsrhzNH5BGszEXym7VF6gxBR5MFhkIY7fdjKy'
    access_token = '1218694128260640768-cEm98EYsLbhv8V6P5YRFj0XbLosSLX'
    access_token_secret = 'cAUT1RSKbsHVQ4z1bGJYyMCAjOy4pLD6OXb3t8fvWbU9q'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # open/create a file to append data
    # csvFile = open('tweets.csv', 'a')
    # # use csv Writer
    # csvWriter = csv.writer(csvFile)

    # compile tweets csv to be analyzed
    tweet_array = []
    for tweet in tweepy.Cursor(api.search,q="#happy",count=1,
                            lang="en",
                            since="2020-01-01").items():
        # print (tweet.created_at, tweet.text)
        tweet_array.append({"created": tweet.created_at, "body": tweet.text.encode('utf-8')})
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    return tweet_array

print(get_tweets())