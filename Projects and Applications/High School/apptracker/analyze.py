import matplotlib.pyplot as plt
import json
import datetime

f = json.load(open("data.json"))

today = datetime.date.today().strftime("%d-%m-%Y")

try:
    date = input("Input date to view, enter for today: ")
except:
    raise ValueError("Invalid input")

if date == "":
    date = today

if date not in f:
    raise ValueError("Date not in data")

plt.bar(f[date].keys(), [i / 60 for i in f[date].values()])

plt.xlabel("Process")
plt.xlabel("Minutes")
plt.title(f"Screen Time on {date}")
plt.show()
