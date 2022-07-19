# imports
import requests
import os
from datetime import datetime

# file imports
import functions

def realtime():
    # values store api key and other settings
    values = functions.get_values()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # get default or input location
        print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit. Press enter for default value.")
        realtime_in = input().strip()
        if realtime_in.lower() == "q":
            return
        elif realtime_in.lower() == "":
            loc = values[1]
        else:
            loc = realtime_in
        params = {
            "key": values[0],
            "q": loc
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        # get response object and print out information
        response = requests.get("https://api.weatherapi.com/v1/current.json?", params=params).json()
        print("Location: {0}, {1} ({2}, {3}).".format(response["location"]["name"], response["location"]["country"], response["location"]["lat"], response["location"]["lon"]))
        print("Localtime: {0}, Last Updated: {1} ({2} minutes ago).".format(datetime.strftime(datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), datetime.strftime(datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), int((datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M") - datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M")).seconds / 60)))
        print("Temperature: {0} {1} (Feels like {2} {3}).".format(response["current"]["temp_" + values[2]], values[2].upper(), response["current"]["feelslike_" + values[2]], values[2].upper()))
        print("Conditions: {0} with {1} {2} of precipitaion, Humidity: {3}%, Clouds: {4}%".format(response["current"]["condition"]["text"], response["current"]["precip_" + values[4]], values[4], response["current"]["humidity"], response["current"]["cloud"]))
        print("Wind: {0} {1} headed {2}.".format(response["current"]["wind_" + values[5]], values[5], response["current"]["wind_dir"]))
        print("UV: {0}, Visibility: {1} {2}, Pressure: {3} {4}.".format(response["current"]["uv"], response["current"]["vis_" + values[6]], values[6], response["current"]["pressure_" + values[3]], values[3]))
        input()
