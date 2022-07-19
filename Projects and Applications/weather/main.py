# imports
import os
import sys
import json

# other file imports
import realtime
import forecast
import functions

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# terminal for different functions
def terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Select an option: [1] Realtime, [2] 3-day Forecast, [3] Miscellaneous, [4] Back:")
        try:
            ter_in = int(input().strip())
            if ter_in in [1, 2, 3, 4, 5, 6]:
                break
            print("Invalid input.")
        except:
            print("Invalid input.")
    if ter_in == 1:
        realtime.realtime()
        terminal()
    elif ter_in == 2:
        forecast.forecast()
        terminal()
    elif ter_in == 3:
        functions.misc()
        terminal()
    else:
        main()

# change/view settings
# user can choose to toggle/change a certain setting, and the code changes the given input in info.json
def settings():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("info.json", "r") as f:
        data = json.load(f)
        while True:
            print("Select an option to change/toggle: [1] Location, [2] Fahrenheit/Celcius, [3] Measurements, [4] Speed, [5] Visibility, [6] Back:")
            print("Current settings: Location: {0}, Temperature: {1}, Measurements: {2}/{3}, Speed: {4}, Visibility: {5}".format(data["loc"], data["temp"], data["pressure"], data["precip"], data["speed"], data["vis"]))
            try:
                settings_in = int(input().strip())
                if settings_in in [1, 2, 3, 4, 5, 6]:
                    break
                print("Invalid input.")
            except:
                print("Invalid input.")
        if settings_in == 1:
            print("Enter a valid Latitude/Longitude, City name, US Zip code, UK postal code, Canada postal code, Metar, IATA, or IP address. Press q to quit.")
            settings_l_in = input().strip()
            if settings_l_in == "q":
                settings()
            data["loc"] = settings_l_in
        elif settings_in == 2:
            while True:
                print("Toggle Fahrenheit/Celcius? [Y]es/[N]o")
                try:
                    settings_t_in = input().strip().lower()
                    if settings_t_in in ["y", "n"]:
                        break
                    print("Invlid input.")
                except:
                    print("Invalid input.")
            if settings_t_in == "y":
                if data["temp"] == "f":
                    data["temp"] = "c"
                else:
                    data["temp"] = "f"
            else:
                settings()
        elif settings_in == 3:
            while True:
                print("Toggle Imperial/Metric? [Y]es/[N]o")
                try:
                    settings_p_in = input().strip().lower()
                    if settings_p_in in ["y", "n"]:
                        break
                    print("Invlid input.")
                except:
                    print("Invalid input.")
            if settings_p_in == "y":
                if data["pressure"] == "in":
                    data["pressure"] = "mb"
                else:
                    data["pressure"] = "in"
                if data["precip"] == "in":
                    data["precip"] = "mm"
                else:
                    data["precip"] = "in"
            else:
                settings()
        elif settings_in == 4:
            while True:
                print("Toggle Mph/Kph? [Y]es/[N]o")
                try:
                    settings_s_in = input().strip().lower()
                    if settings_s_in in ["y", "n"]:
                        break
                    print("Invlid input.")
                except:
                    print("Invalid input.")
            if settings_s_in == "y":
                if data["speed"] == "mph":
                    data["speed"] = "kph"
                else:
                    data["speed"] = "mph"
            else:
                settings()
        elif settings_in == 5:
            while True:
                print("Toggle Miles/Kilometers? [Y]es/[N]o")
                try:
                    settings_s_in = input().strip().lower()
                    if settings_s_in in ["y", "n"]:
                        break
                    print("Invlid input.")
                except:
                    print("Invalid input.")
            if settings_s_in == "y":
                if data["vis"] == "miles":
                    data["vis"] = "km"
                else:
                    data["vis"] = "niles"
            else:
                settings()
        else:
            main()
    with open("info.json", "w") as f:
        json.dump(data, f)
    settings()
    
# show credits
def credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Powered by WeatherAPI (https://www.weatherapi.com/)")
    print("Author of code: Caleb Han")
    input()
    main()

# main loop
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Select an option: [1] View commands, [2] Change settings, [3] View credits, [4] Quit:")
        try:
            main_in = int(input().strip())
            if main_in in [1, 2, 3, 4]:
                break
            print("Invalid input.")
        except:
            print("Invalid input.")
    if main_in == 1:
        return terminal()
    elif main_in == 2:
        return settings()
    elif main_in == 3:
        return credits()
    else:
        sys.exit()

# run main loop
main()
