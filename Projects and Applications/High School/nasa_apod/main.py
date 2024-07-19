import requests
from datetime import datetime
import shutil
import random

# api keys
NASA_API = ""

# get date
date = input("Enter a date to search (YYYY-MM-DD) if left empty, random image: ")
if date == "":
    data = random.choice(requests.get("https://api.nasa.gov/planetary/apod?", params={"count": 1, "api_key": NASA_API}).json())
else:
    date = datetime.strptime(date, "%Y-%m-%d")
    if len(str(date.day)) > 1:
        date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    else:
        date = str(date.year) + "-" + str(date.month) + "-0" + str(date.day)
    data = requests.get("https://api.nasa.gov/planetary/apod?", params={"api_key": NASA_API, "date": date}).json()

# get photo data
photo = requests.get(data["hdurl"], stream=True, params={"api_key": NASA_API})

# output data
print("Title: " + data["title"])
print("Date: " + data["date"])
print("Explanation: " + data["explanation"])
print("Copyright: " + data["copyright"])

# download photo
with open("img.jpg", "wb") as f:
    shutil.copyfileobj(photo.raw, f)
