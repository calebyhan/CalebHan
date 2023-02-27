import tweepy
from datetime import datetime
import json
import pytz
import csv
import time
from textblob import TextBlob
import requests
import pandas as pd
import matplotlib.pyplot as plt

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
bearer_token = ""

def get_data():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')

    with open("data.csv", "w", newline="", encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text', 'date', 'likes', 'original_id'))
        csv_writer.writeheader()
        params = {
                    "query": f"collegeboard -is:retweet",
                    "max_results": 100,
                    "tweet.fields": "created_at,public_metrics",
                    "expansions": "author_id",
                    "sort_order": "relevancy",
                }
        url = "https://api.twitter.com/2/tweets/search/recent"

        headers = {
                    "Authorization": f"Bearer {bearer_token}"
                }
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["data"]

        for tweet in data:
            row = {'user': tweet["author_id"], 'text': tweet['text'].replace('\n', ' '), 'date': tweet['created_at'], 'likes': tweet["public_metrics"]["like_count"], 'original_id': tweet["id"]}
            csv_writer.writerow(row)


def get_sentiment():
    with open('data.csv', 'r', encoding='utf-8') as input_file, open('sentiment.csv', 'w', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(f, fieldnames=('user', 'text', 'date', 'likes', 'original_id', 'polarity', 'subjectivity', 'expression'))
        writer.writeheader()

        for row in reader:
            blob = TextBlob(row['text'])
            polarity, subjectivity = blob.sentiment
            expression = "Neutral"
            if polarity > 0:
                expression = "Positive"
            elif polarity < 0:
                expression = "Negative"

            writer.writerow({
                'user': row['user'],
                'text': row['text'],
                'date': row['date'],
                'likes': row['likes'],
                'original_id': row['original_id'],
                'polarity': polarity,
                'subjectivity': subjectivity,
                'expression': expression
            })

def display_bar():
    df = pd.read_csv('sentiment.csv')

    counts = df.groupby('expression').size()

    counts.plot(kind='bar')

    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')

    plt.show()

def display_avg():
    df = pd.read_csv('sentiment.csv')

    df['date'] = pd.to_datetime(df['date'])

    avg_polarity = df.groupby(df['date'].dt.date)['polarity'].mean()

    plt.plot(avg_polarity.index, avg_polarity.values)
    plt.xlabel('Date')
    plt.ylabel('Average Polarity')
    plt.xlim(df['date'].min(), df['date'].max())

    plt.show()

display_avg()