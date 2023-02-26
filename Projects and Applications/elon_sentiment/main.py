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

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

user = api.get_user(user_id='44196397')

def get_tweets():
    max_tweets = 200

    all_tweets = []

    new_tweets = api.user_timeline(user_id=user.id, count=max_tweets)
    start_date = datetime(2022, 10, 27, tzinfo=pytz.timezone('US/Eastern'))

    while True:
        all_tweets.extend(new_tweets)
        new_tweets = api.user_timeline(user_id=user.id, count=max_tweets, max_id=all_tweets[-1].id - 1)
        if len(new_tweets) == 0:
            break

    tweets = []
    for tweet in all_tweets:
        tweets.append(tweet._json)

    tweets = [tweet for tweet in tweets if datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y') >= start_date and tweet["in_reply_to_status_id"] is None]

    with open("tweets.json", "w") as f:
        f.write(json.dumps(tweets, indent=4))

def get_replies():
    data = json.load(open("tweets.json", "r"))
    with open ('replies.csv', 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text', 'date', 'likes', 'original_id'))
        csv_writer.writeheader()
        for tweet in data:
            params = {
                "query": f"conversation_id:{tweet['id']} -is:retweet",
                "max_results": 100,
                "tweet.fields": "created_at,public_metrics",
                "expansions": "author_id",
                "sort_order": "relevancy",
            }

            url = "https://api.twitter.com/2/tweets/search/recent"

            headers = {
                "Authorization": f"Bearer {bearer_token}"
            }

            while True:
                try:
                    response = requests.get(url, headers=headers, params=params)
                    response.raise_for_status()
                    data = response.json()
                    if "data" in data:
                        tweets = data["data"]
                        for reply in tweets:
                            row = {'user': reply["author_id"], 'text': reply['text'].replace('\n', ' '), 'date': reply['created_at'], 'likes': reply["public_metrics"]["like_count"], 'original_id': tweet["id"]}
                            csv_writer.writerow(row)
                    if "meta" in data and "next_token" not in params:
                        break
                    if "meta" in data and "next_token" in params:
                        params["next_token"] = data["meta"]["next_token"]
                    else:
                        break
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 429:
                        print("Rate limit reached. Sleeping for 15 minutes...")
                        time.sleep(15*60)
                    else:
                        raise e

def get_sentiment():
    with open('replies.csv', 'r', encoding='utf-8') as input_file, open('sentiment.csv', 'w', newline='', encoding='utf-8') as f:
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
    plt.show()
