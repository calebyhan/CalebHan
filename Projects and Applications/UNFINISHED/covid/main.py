import requests
import os
import sys
import functions

import commands.globalst as globalst
import commands.indst as indst

os.system('cls' if os.name == 'nt' else 'clear')

def terminal():
    te_ch_m = 0
    while te_ch_m not in [1, 2, 3, 4]:
        print("Choose a type of command:")
        print("[1] Global, [2] Individual countries, [3] Comparing Countries, [4] Back")
        try:
            te_ch_m = int(input().strip())
            if te_ch_m not in [1, 2, 3, 4]:
                te_ch_m("Invalid input.")
        except:
            print("Invalid input.")
    os.system('cls' if os.name == 'nt' else 'clear')
    if te_ch_m == 1:
        te_ch_g = 0
        while te_ch_g not in [1, 2, 3]:
            print("Choose a command:")
            print("[1] Today/total, [2] Ranked, [3] Back")
            try:
                te_ch_g = int(input().strip())
                if te_ch_g not in [1, 2, 3]:
                    te_ch_g("Invalid input.")
            except:
                print("Invalid input.")
        os.system('cls' if os.name == 'nt' else 'clear')
        if te_ch_g == 1:
            globalst.stats_today()
        if te_ch_g == 2:
            globalst.ranked_term()
        else:
            terminal()
    elif te_ch_m == 2:
        te_ch_i = 0
        while te_ch_i not in [1, 2, 3, 4, 5]:
            print("Choose a command:")
            print("[1] Today, [2] All Data, [3] Certain Date, [4] Certain Date Range, [5] Back")
            try:
                te_ch_i = int(input().strip())
                if te_ch_i not in [1, 2, 3, 4, 5]:
                    te_ch_i("Invalid input.")
            except:
                print("Invalid input.")
            os.system('cls' if os.name == 'nt' else 'clear')
            if te_ch_i == 1:
                pass
            elif te_ch_i == 2:
                pass
            elif te_ch_i == 3:
                pass
            elif te_ch_i == 4:
                pass
            else:
                terminal()
    elif te_ch_m == 4:
        help_menu()

def credits():
    url = "https://api.covid19api.com/version"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print("API Provider: https://covid19api.com/\nAPI Version: {0}".format(response.text[1:-2]))

def help_menu():
    hm_ch = 0
    while hm_ch not in [1, 2, 3]:
        print("Welcome to the database! What do you want to do:")
        print("[1] View commands, [2] View credits/info, [3] Quit")
        try:
            hm_ch = int(input().strip())
            if hm_ch not in [1, 2, 3]:
                hm_ch("Invalid input.")
        except:
            print("Invalid input.")
    os.system('cls' if os.name == 'nt' else 'clear')
    if hm_ch == 1:
        return terminal()
    elif hm_ch == 2:
        return credits()
    else:
        sys.exit()

def run():
    running = True
    while running:
        help_menu()

# run()
indst.stats_today()
