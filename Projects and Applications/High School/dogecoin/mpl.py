# imports
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
import csv

# get mouse position on mpl plot
def mouse_event(event):
   print('x: {} and y: {}'.format(event.xdata, event.ydata))

# get all dates from start of the data to now
ds = [[], []]
times = pd.date_range('2014-09-17', periods=len(pd.read_csv("Dogecoin.csv")) + 1, freq='D')

# get all price values
with open("Dogecoin.csv", mode="r") as f:
    count = 0
    for i in csv.reader(f):
        if count != 0 and i[1] != 'null':
            ds[0].append(times[count])
            ds[1].append(float(i[2]))
        count += 1

# set up plot
fig, ax = plt.subplots(figsize=(12, 8))
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=50))
ax.xaxis.set_major_formatter(DateFormatter("%m-%d-%Y"))

cid = fig.canvas.mpl_connect('motion_notify_event', mouse_event)

# plot points
plt.plot(ds[0], ds[1])

# show plot
plt.show()
