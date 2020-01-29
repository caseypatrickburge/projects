# import sentiment analysis modules
import spacy
import vaderSentiment.vaderSentiment as vader

# import tweet crawler modules
import tweepy
import csv
import pandas as pd

# function that pulls tweets
def get_tweets():
# twitter dev credentials here:
    consumer_key = 'zIBVTTzH7JJECyk13IX4NhEwA'
    consumer_secret = ''
    access_token = '1218694128260640768-8htRlFCLm99PMtvhJYFwJSR0GhvNwD'
    access_token_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    # open/create a file to append data
    # csvFile = open('tweets.csv', 'a')
    # # use csv Writer
    # csvWriter = csv.writer(csvFile)

    # compile tweets csv to be analyzed
    tweet_array = []
    for tweet in tweepy.Cursor(api.search,q="#nike",count=5,
                            lang="en",
                            since="2020-01-01").items():
        # print (tweet.created_at, tweet.text)
        tweet_array.append({"created": tweet.created_at, "body": tweet.text.encode('utf-8')})
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    return tweet_array

    
# call get_tweets()
tweet_list = get_tweets()

# sentiment analysis function 
analyzer = vader.SentimentIntensityAnalyzer()
english = spacy.load("en_core_web_sm")

# define get_sentiments function to process tweets
def get_sentiments(text_list):
    text = "\n".join([str(tweet["body"]) for tweet in text_list])
    result = english(text)
    print(result)
    sentences = [str(sent) for sent in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sentences]
    return sentiments    

# define analyze_tweets function
def analyze_tweets(tweet_list):
    # open and analyze sentiment of tweets
    # data = open('tweets.csv', 'r')
    # text = data.read()
    text = tweet_list
    sentiments = get_sentiments(text)

    # open/create a file to append data
    csvFile = open('sentiment.csv', 'a')
    fieldnames = ["neg", "neu", "pos", "compound"]
    # use csv Writer
    csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)

    # compile tweets csv to be analyzed
    csvWriter.writeheader()
    for sent in sentiments:
        print(sent)
        csvWriter.writerow(sent)

analyze_tweets(tweet_list)