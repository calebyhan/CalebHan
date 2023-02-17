import requests
import json
from dateutil import parser
import datetime
import csv
import os
import warnings
warnings.simplefilter("ignore", UserWarning)
from fuzzywuzzy import process

states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new-hampshire', 'new-jersey', 'new-mexico', 'new-york', 'north-carolina', 'north-dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode-island', 'south -carolina', 'south-dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west-virginia', 'wisconsin', 'wyoming']

def countries():
    url = "https://api.covid19api.com/countries"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = dataprocess(response.text)
    with open("countries.txt", "w") as f:
        for i in data:
            f.write("{0},{1},{2}\n".format(i["Country"], i["ISO2"], i["Slug"]))

def dataprocess(data):
    data = json.loads(data)
    return data

def today():
    pass

def fromiso(indate):
    return str(parser.parse(indate)).split(" ")[0]

def toiso(indate):
    return indate+"T00:00:00Z"

def find_match(txt):
    with open("countries.txt", "r") as f:
        csvr = csv.reader(f)
        header = next(csvr)
        lst = []
        for row in csvr:
            lst.append(row[2].lower())
        return process.extractOne(txt, lst)[0]

def united_states(datetoday):
    datenow = ""
    dates = {}
    if datetoday == datetime.datetime.now().isoformat():
        return True
    else:
        datetoday = datetime.datetime.now().isoformat()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Constructing data...")
        for i in states:
            url = "https://api.covid19api.com/dayone/country/united-states?province=" + i
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            data = dataprocess(response.text)
            lst = [0, 0, 0, 0]
            for i in data:
                if i["Date"] == datenow:
                    lst[0] += int(i["Confirmed"])
                    lst[1] += int(i["Deaths"])
                    lst[2] += int(i["Recovered"])
                    lst[3] += int(i["Active"])
                else:
                    datenow = i["Date"]
                    if i["Date"] in dates:
                        dates[i["Date"]][0] += lst[0]
                        dates[i["Date"]][1] += lst[1]
                        dates[i["Date"]][2] += lst[2]
                        dates[i["Date"]][3] += lst[3]
                    else:
                        dates[i["Date"]] = list(lst)
    with open("us.txt", "w") as f:
        cnt = 0
        for i in dates:
            cnt += 1
            if cnt == len(dates):
                f.write("{\"Confirmed\":\"" + str(dates[i][0]) + ",\"Deaths\":\"" + str(dates[i][1]) + ",\"Recovered\":\"" + str(dates[i][2]) + ",\"Active\":\"" + str(dates[i][3]) + ",\"Date\":\"" + i + "\"}]")
            else:
                f.write("{\"Confirmed\":\"" + str(dates[i][0]) + ",\"Deaths\":\"" + str(dates[i][1]) + ",\"Recovered\":\"" + str(dates[i][2]) + ",\"Active\":\"" + str(dates[i][3]) + ",\"Date\":\"" + i + "\"},\n")
    os.system('cls' if os.name == 'nt' else 'clear')
