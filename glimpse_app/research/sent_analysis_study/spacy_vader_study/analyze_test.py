import os
from datetime import datetime

# import sentiment analysis modules
import spacy
import vaderSentiment.vaderSentiment as vader

# import tweet crawler modules
import tweepy
import csv
import numpy as np
import pandas as pd

# import visualization modules
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.close('all')

# function that pulls tweets
def get_tweets():
# twitter dev credentials here:
    consumer_key = '4c1PSnBoANc3gZCcqM8QgWJCB'
    consumer_secret = 'PFcsPoYNTGrdiDiPlU58jirNJteKXkuzPTM8poFQGNlbwU6QKV'
    access_token = '1218694128260640768-EHEP7n8eYQnMes7KwzRG4AHFDzqeJS'
    access_token_secret = 'RQX9Hp1uAr8VgxGocAwFjFpUoLFHgxdLoMqQVIRcf4VNE'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

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

    
# call get_tweets()
tweet_list = get_tweets()

# sentiment analysis function 
analyzer = vader.SentimentIntensityAnalyzer()
english = spacy.load("en_core_web_sm")

# define get_sentiments function to process tweets
def get_sentiments(text_list):
    text = "\n".join([str(tweet["body"]) for tweet in text_list])
    result = english(text)
    # print(result)
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
        # print(sent)
        csvWriter.writerow(sent)

analyze_tweets(tweet_list)

def find_sent_mean():
    df = pd.read_csv("sentiment.csv")
    mean = df.mean()
    mean = mean.drop(["neu", "compound"])
    neg = float(mean[0]) * 100
    pos = float(mean[1]) * 100
    neg = format(neg,'.1f')
    pos = format(pos,'.1f')
    print("\n----------- Tweet Sentiment -----------\n")
    print(f"Negative: {neg}\nPositive: {pos}")
    os.remove("sentiment.csv")
# call find_sent_mean function
find_sent_mean()
# define generate_wordcloud function
def generate_wordcloud(tweet_list):
    # define now for naming wordcloud.png
    now = datetime.now()
    # create wordcloud from tweet_list
    # remove stopwords & irrelevant phrases
    WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color="steelblue").generate_from_text(" ".join([r for _d in tweet_list for r in _d['body'].decode('utf-8').replace('https', "").replace('photo', '').replace('RT', '').split() if r not in set(nltk.corpus.stopwords.words("english"))])).to_file(f"wordcloud{now.hour}{now.minute}{now.second}.png")
    
generate_wordcloud(tweet_list)