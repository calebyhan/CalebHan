'''
Stock
Author: Caleb Han
'''

# imports

import requests
import json
from twilio.rest import Client
import datetime
import os
from twilio.rest import Client

# endpoints used

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# api keys and phone numbers

TWI_NUM = ""
VERI_NUM = ""

ST_APIKEY = ""
NEW_APIKEY = ""
TWI_SID = ""
TWI_AUTH = ""

company_name = ""
st_name = ""

# function that outputs top 10 searches of inputted company name (search bar)
def query_search():
  query = True
  while query:
    # user input
    st_name = input("Enter a company symbol: ")
    print("\n")

    # fetch from api to get top 10 searches
    response = requests.request("GET", "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + st_name + "&apikey=" + ST_APIKEY)
    matches = json.loads(response.text)["bestMatches"]
    # format output
    for i in range(len(matches)):
      print(str(i + 1) + " - " + matches[i]["2. name"] + " (" + matches[i]["1. symbol"] + ")")
    print(str(len(matches) + 1) + " - N/A\n")
    # if chosen a correct output, break
    try:
      new_st_id = int(input("Choose the correct corresponding number: ")) - 1
      st_name = matches[new_st_id]["1. symbol"]
      company_name = matches[new_st_id]["2. name"]
      query = False
    except:
      pass
  # response to pass around other functions
  response = requests.request("GET", "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + st_name + "&apikey=" + ST_APIKEY)
  return st_name, company_name, response.text

# function that decides whether or not to recommend a stock
def recommend_buy(symbol, text):
  # calculate percent increase consecutively over 5 days (true if consecutive)
  prev = float([value for (key, value) in json.loads(text)["Time Series (Daily)"].items()][4]["4. close"])
  for i in range(4, 0, -1):
    daily = float([value for (key, value) in json.loads(text)["Time Series (Daily)"].items()][i - 1]["4. close"])
    if (daily-prev)/prev < 0.01:
      return False
  return True

# function that prints basic information of given stock
def print_info(symbol, text):
  # call recommend function
  recommend = recommend_buy(symbol, text)
  reason = ""
  if recommend:
    reason = "5 consecutive increases of 1% from last closing price"
  else:
    reason = "5 inconsistent increases of 1% from last closing price"
  daily = json.loads(text)["Time Series (Daily)"][str(datetime.date.today() - datetime.timedelta(days=1))]["4. close"]
  # call api for basic company information
  text = requests.request("GET", "https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + symbol + "&apikey=" + ST_APIKEY)
  text = text.text
  # print out all information formatted
  print("\n-------------------")
  print("Symbol: " + json.loads(text)["Symbol"])
  print("\nCompany Name: " + json.loads(text)["Name"])
  print("\nAsset Type: " + json.loads(text)["AssetType"])
  print("\nStock Value: " + str(daily))
  print("\nMarket Capitalization: " + json.loads(text)["MarketCapitalization"])
  print("\nRecommend Buy: " + str(recommend) + " / Reason: " + reason)
  print("\nCompany description: " + json.loads(text)["Description"])
  print("-------------------")

# function that calculates percent increase/decrease from last 2 days
def calculate_percent(text):
  # when stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
  yesterday = json.loads(text)["Time Series (Daily)"][str(datetime.date.today() - datetime.timedelta(days=1))]["4. close"]
  day_before_yesterday = json.loads(text)["Time Series (Daily)"][str(datetime.date.today() - datetime.timedelta(days=2))]["4. close"]
  diff_closing_price = abs(float(yesterday) - float(day_before_yesterday))
  percent_change = diff_closing_price / float(yesterday)
  return percent_change

# function that gets news articles of given company name
def news(percent_change):
  if percent_change > 0.05:      
    news_params = {
      "apiKey": NEW_APIKEY,
      "qInTitle": company_name,
    }
    # fetch news from api
    news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()
    articles = news_response['articles'][0:3]
    # print out content from fetched articles
    for i in articles:
      print(i['content'])
    return articles
  return []

# function that texts said news articles
def text_news(articles):
  # if no articles fetched, return
  if len(articles) == 0:
    return

  # set up texting client
  client = Client(TWI_SID, TWI_AUTH)

  # text out the articles to given phone number
  for i in range(3):
    msg = articles[i]['content']
    message = client.messages \
                  .create(
                       body=msg,
                       from_=TWI_NUM,
                       to=VERI_NUM
                   )
  print("Messages sent")

# main function to control flow
def main():
  st_name, company_name, text = query_search()
  print_info(st_name, text)
  percent = calculate_percent(text)
  articles = news(percent)
  text_news(articles)

main()
