import requests
from datetime import datetime
import math
import shutil

# api keys
NASA_API = "EaMt8EVyiRHMnIsmQCn4ahzqrvlgfxON2txlxaEw"
COORDS_API = "5ebf502c2b1602950b1595862ea3d565"

# format user input for city
while True:
    loc = input("Enter the city or latitude/longitude of the location without a comma: ")

    try:
        loc = list(map(int(loc.split(" "))))
        break
    except:
        coords = requests.get("http://api.openweathermap.org/geo/1.0/direct?", params={"q": loc, "limit": 1, "appid": COORDS_API}).json()
        try:
            coords[0]['name']
            loc = [coords[0]['lat'], coords[0]['lon']]
            break
        except:
            print("Error: invalid location. Try again.")

# get date
date = input("Enter a date to search or nothing to get a random date (YYYY-MM-DD): ")
date = datetime.strptime(date, "%Y-%m-%d")
if len(str(date.day)) > 1:
    date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
else:
    date = str(date.year) + "-" + str(date.month) + "-0" + str(date.day)

# get data from that date
if date == "":
    data = requests.get("https://api.nasa.gov/EPIC/api/natural", params={"api_key": NASA_API}).json()
else:
    data = requests.get("https://api.nasa.gov/EPIC/api/natural/date/" + date, params={"api_key": NASA_API}).json()

# find closest img
closest = ["", [0, 0], 10000]
for i in data:
    if math.dist(closest[1], [float(i["centroid_coordinates"]["lat"]), float(i["centroid_coordinates"]["lon"])]) < closest[2]:
        closest = [i['identifier'], [float(i["centroid_coordinates"]["lat"]), float(i["centroid_coordinates"]["lon"])], math.dist(closest[1], [float(i["centroid_coordinates"]["lat"]), float(i["centroid_coordinates"]["lon"])])]

date_for = "/".join(date.split("-"))

for i in data:
    if i['identifier'] == closest[0]:
        img = i['image']

# download photo
photo = requests.get("https://api.nasa.gov/EPIC/archive/natural/" + date_for + "/jpg/" + img + ".jpg", stream=True, params={"api_key": NASA_API})

with open("img.jpg", "wb") as f:
    shutil.copyfileobj(photo.raw, f)
