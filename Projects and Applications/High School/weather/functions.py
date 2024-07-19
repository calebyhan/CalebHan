# imports
import json
import os
import requests
from datetime import datetime

# gets api key and other settings
def get_values():
    ret = []
    with open ("info.json", "r") as f:
        data = json.load(f)
        ret = [data["key"], data["loc"], data["temp"], data["pressure"], data["precip"], data["speed"], data["vis"]]
    return ret

# astronomy
def astro():
    # get values for api key and other settings
    values = get_values()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # get default or inputted location
        print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit. Press enter for default value.")
        astro_in = input().strip()
        if astro_in.lower() == "q":
            return
        elif astro_in.lower() == "":
            loc = values[1]
        else:
            loc = astro_in
        params = {
            "key": values[0],
            "q": loc,
            "days": 3 
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        # get response object and print out information for 3 days
        response = requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()
        print("Location: {0}, {1} ({2}, {3}).".format(response["location"]["name"], response["location"]["country"], response["location"]["lat"], response["location"]["lon"]))
        print("Localtime: {0}, Last Updated: {1} ({2} minutes ago).".format(datetime.strftime(datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), datetime.strftime(datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), int((datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M") - datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M")).seconds / 60)))
        for i in range(params["days"]):
            print()
            print("Date: {0}".format(datetime.strftime(datetime.strptime(response["forecast"]["forecastday"][i]["date"], "%Y-%m-%d"), "%m-%d-%Y")))
            print("Sunrise: {0}, Sunset: {1}.".format(response["forecast"]["forecastday"][i]["astro"]["sunrise"], response["forecast"]["forecastday"][i]["astro"]["sunset"]))
            print("Moonrise: {0}, Moonset: {1}.".format(response["forecast"]["forecastday"][i]["astro"]["moonrise"], response["forecast"]["forecastday"][i]["astro"]["moonset"]))
            print("Moon phase: {0}, Moon illumination: {1}%.".format(response["forecast"]["forecastday"][i]["astro"]["moon_phase"], response["forecast"]["forecastday"][i]["astro"]["moon_illumination"]))
        print()
        input()

# air quality
def air():
    # get values for api key and other settings
    values = get_values()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # get default or inputted location
        print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit. Press enter for default value.")
        astro_in = input().strip()
        if astro_in.lower() == "q":
            return
        elif astro_in.lower() == "":
            loc = values[1]
        else:
            loc = astro_in
        params = {
            "key": values[0],
            "q": loc,
            "days": 3,
            "aqi": "yes"
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        # get response object and print out information
        response = requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()
        us = {1:"Good", 2:"Moderate", 3:"Unhealthy for sensitive group", 4:"Unhealthy", 5:"Very Unhealthy", 6:"Hazardous"}
        uk1 = {1:"Low", 2:"Low", 3:"Low", 4:"Moderate", 5:"Moderate", 6:"Moderate", 7:"High", 8:"High", 9:"High", 10:"Very High"}
        uk2 = {1:"0-11", 2:"12-23", 3:"24-35", 4:"36-41", 5:"42-47", 6:"48-53", 7:"54-48", 8:"59-64", 9:"65-70", 10:"71+"}
        print("Location: {0}, {1} ({2}, {3}).".format(response["location"]["name"], response["location"]["country"], response["location"]["lat"], response["location"]["lon"]))
        print("Localtime: {0}, Last Updated: {1} ({2} minutes ago).".format(datetime.strftime(datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), datetime.strftime(datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), int((datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M") - datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M")).seconds / 60)))
        print("Carbon Monoxide: {0} μg/m³, Ozone: {1} μg/m³, Nitroxen Dioxide: {2} μg/m³.".format(str(round(response["current"]["air_quality"]["co"], 2)), str(round(response["current"]["air_quality"]["o3"], 2)), str(round(response["current"]["air_quality"]["no2"], 2))))
        print("Sulphur dioxide: {0} μg/m³, PM2.5: {1} μg/m³, PM10: {2} μg/m³.".format(str(round(response["current"]["air_quality"]["so2"], 2)), str(round(response["current"]["air_quality"]["pm2_5"], 2)), str(round(response["current"]["air_quality"]["pm10"], 2))))
        print("USA EPA Index: {0}, UK DEFRA Index: {1} ({2} µgm⁻³).".format(us[int(response["current"]["air_quality"]["us-epa-index"])], uk1[int(response["current"]["air_quality"]["gb-defra-index"])], uk2[int(response["current"]["air_quality"]["gb-defra-index"])]))
        input()

# alerts
def alerts():
    # get values for api key and other settings
    values = get_values()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # get default or inputted location
        print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit. Press enter for default value.")
        astro_in = input().strip()
        if astro_in.lower() == "q":
            return
        elif astro_in.lower() == "":
            loc = values[1]
        else:
            loc = astro_in
        params = {
            "key": values[0],
            "q": loc,
            "days": 3,
            "alerts": "yes"
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        # get response object and print out information for every alert object
        response = requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()
        if len(response["alerts"]["alert"]) > 0:
            for i in range(len(response["alerts"]["alert"])):
                print("Alert #{0}".format(i + 1))
                print("Headline: {0}".format(response["alerts"]["alert"][i]["headline"]))
                print("Severity: {0}".format(response["alerts"]["alert"][i]["severity"]))
                print("Areas: {0}".format(response["alerts"]["alert"][i]["areas"]))
                print("Event: {0}".format(response["alerts"]["alert"][i]["event"]))
                print("Description: {0}".format(response["alerts"]["alert"][i]["desc"]))
                print("Instructions: {0}".format(response["alerts"]["alert"][i]["instruction"]))
                print()
        else:
            print("No alerts.")
        input()
            
# terminal for miscellaneous functions
def misc():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Select an option: [1] Astronomy, [2] Air quality, [3] Alerts, [4] Back:")
        try:
            misc_in = int(input().strip())
            if misc_in in [1, 2, 3, 4, 5, 6]:
                break
            print("Invalid input.")
        except:
            print("Invalid input.")
    if misc_in == 1:
        astro()
    elif misc_in == 2:
        air()
    elif misc_in == 3:
        alerts()
    else:
        return
