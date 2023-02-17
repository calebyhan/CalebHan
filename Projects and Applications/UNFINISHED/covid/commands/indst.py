import requests
import os

import functions

def stats_today():
    print("What country do you want to retrieve data from?")
    country = functions.find_match(input())
    if country == "united-states":
        functions.united_states("2022-04-26T00:00:00Z")
        # with open ("us.txt")
    url = "https://api.covid19api.com/dayone/country/" + functions.find_match(input()) + "/status/confirmed"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = functions.dataprocess(response.text)
    print(data)
