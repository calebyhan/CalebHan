# imports
import requests
import os
from datetime import datetime

# file imports
import functions

def forecast():
    # values store api key and other settings
    values = functions.get_values()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # get default or inputted location
        print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit. Press enter for default value.")
        forecast_in = input().strip()
        if forecast_in.lower() == "q":
            return
        elif forecast_in.lower() == "":
            loc = values[1]
        else:
            loc = forecast_in
        params = {
            "key": values[0],
            "q": loc,
            "days": 3
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        # get response object and print information for 3 days
        response = requests.get("https://api.weatherapi.com/v1/forecast.json?", params=params).json()
        print("Location: {0}, {1} ({2}, {3}).".format(response["location"]["name"], response["location"]["country"], response["location"]["lat"], response["location"]["lon"]))
        print("Localtime: {0}, Last Updated: {1} ({2} minutes ago).".format(datetime.strftime(datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), datetime.strftime(datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p"), int((datetime.strptime(response["location"]["localtime"], "%Y-%m-%d %H:%M") - datetime.strptime(response["current"]["last_updated"], "%Y-%m-%d %H:%M")).seconds / 60)))
        for i in range(params["days"]):
            print()
            print("[{0}] Date: {1}".format(i + 1, datetime.strftime(datetime.strptime(response["forecast"]["forecastday"][i]["date"], "%Y-%m-%d"), "%m-%d-%Y")))
            print("Average Temperature: {0} {1}, Highest Temperature: {2} {3}, Lowest Temperature: {4} {5}.".format(response["forecast"]["forecastday"][i]["day"]["avgtemp_" + values[2]], values[2].upper(), response["forecast"]["forecastday"][i]["day"]["maxtemp_" + values[2]], values[2].upper(), response["forecast"]["forecastday"][0]["day"]["mintemp_" + values[2]], values[2].upper()))
            print("Conditions: {0} with {1} {2} of total precipitaion, Average Humidity: {3}%.".format(response["forecast"]["forecastday"][i]["day"]["condition"]["text"], response["forecast"]["forecastday"][i]["day"]["totalprecip_" + values[4]], values[4], response["forecast"]["forecastday"][0]["day"]["avghumidity"]))
            print("Chance of rain: {0}%, Chance of snow: {1}%.".format(response["forecast"]["forecastday"][i]["day"]["daily_chance_of_rain"], response["forecast"]["forecastday"][i]["day"]["daily_chance_of_snow"]))
            print("UV: {0}, Average Visibility: {1} {2}.".format(response["forecast"]["forecastday"][i]["day"]["uv"], response["forecast"]["forecastday"][i]["day"]["avgvis_" + values[6]], values[6]))
        print()
        while True:
            # if the user wants to view hourly forecast
            print("Select a date to view hourly forecast or press enter to continue: ")
            forecast_in_date = input().strip()
            try:
                if forecast_in_date == "":
                    forecast()
                if int(forecast_in_date) in [1, 2, 3]:
                    break
                print("Invalid input.")
            except:
                print("Invalid input.")
        os.system('cls' if os.name == 'nt' else 'clear')
        forecast_in_date = int(forecast_in_date)
        # show every 6 hour forecast
        for i in range(0, 4):
            i = i * 6
            response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]
            print("Localtime: {0}.".format(datetime.strftime(datetime.strptime(response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["time"], "%Y-%m-%d %H:%M"), "%m-%d-%Y %I:%M %p")))
            print("Temperature: {0} {1} (Feels like {2} {3}).".format(response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["temp_" + values[2]], values[2].upper(), response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["feelslike_" + values[2]], values[2].upper()))
            print("Conditions: {0} with {1} {2} of precipitaion, Humidity: {3}%, Clouds: {4}%".format(response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["condition"]["text"], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["precip_" + values[4]], values[4], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["humidity"], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["cloud"]))
            print("Wind: {0} {1} headed {2}.".format(response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["wind_" + values[5]], values[5], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["wind_dir"]))
            print("UV: {0}, Visibility: {1} {2}, Pressure: {3} {4}.".format(response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["uv"], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["vis_" + values[6]], values[6], response["forecast"]["forecastday"][forecast_in_date - 1]["hour"][i]["pressure_" + values[3]], values[3]))
            print()
        input()
