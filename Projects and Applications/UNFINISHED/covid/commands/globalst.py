import requests
import os

import functions

def stats_today():
    url = "https://api.covid19api.com/summary"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = functions.dataprocess(response.text)["Global"]
    print("GLOBAL DATA FROM TODAY:\nNew Confirmed: {0}\nTotal Confirmed: {1}\nNew Deaths: {2}\nTotal Deaths: {3}\nNew Recovered: {4}\nTotal Recovered: {5}".format(
        data["NewConfirmed"], data["TotalConfirmed"], data["NewDeaths"], data["TotalDeaths"], data["NewRecovered"], data["TotalRecovered"]))
    input("\nPress enter to Continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

def ranked_term():
    ra_ch = 0
    while ra_ch not in [1, 2, 3, 4, 5, 6, 7]:
        print("What do you want to see ranked:")
        print("[1] Daily Confirmed, [2] Daily Deaths, [3] Daily Recovered, [4] Total Confirmed, [5] Total Deaths, [6] Total Recovered [7] Back")
        try:
            ra_ch = int(input().strip())
            if ra_ch not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid input.")
        except:
            print("Invalid input.")
    if ra_ch == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    os.system('cls' if os.name == 'nt' else 'clear')
    data = __ranked_process(ra_ch)
    running = True
    show = 1
    while running:
        if show + 10 > 193:
            print("Showing {0}-{1}".format(show, 193))
        else:
            print("Showing {0}-{1}".format(show, show + 10))
        for i in range(show, show + 11):
            if i == 194:
                break
            print("{0}: {1}".format(data[i - 1][0], data[i - 1][1]))
        ra_ch_r = 0
        while ra_ch_r not in [1, 2, 3]:
            print("[1] Back, [2] Forwards, [3] Back")
            try:
                ra_ch_r = int(input().strip())
                if ra_ch not in [1, 2, 3]:
                    ra_ch_r("Invalid input.")
            except:
                print("Invalid input.")
        os.system('cls' if os.name == 'nt' else 'clear')
        if ra_ch_r == 1:
            if show != 1:
                show -= 10
        elif ra_ch_r == 2:
            if show != 191:
                show += 10
        else:
            running = False

def __ranked_process(type):
    ret = []
    url = "https://api.covid19api.com/summary"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = functions.dataprocess(response.text)["Countries"]
    type -= 1
    for i in data:
        switcher = {
            0: "NewConfirmed",
            1: "NewDeaths",
            2: "NewRecovered",
            3: "TotalConfirmed",
            4: "TotalDeaths",
            5: "TotalRecovered"
        }
        ret.append([i["Country"], i[switcher.get(type, "")]])
    ret.sort(key = lambda x: x[1])
    ret.reverse()
    return ret
