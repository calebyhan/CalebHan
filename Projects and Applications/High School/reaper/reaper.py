"""
Reaper
Author: Caleb Han
"""

# imports
import re
import sys

# debugging variable
DEBUG = False

# multi-line input
x = sys.stdin.readlines()
list1 = []
for item in x:
    item = item.replace("\n", "")
    if DEBUG:
        print(x)
for item in x:
    if re.search(r'(?<=raven.min.js:2 )[.\-\w= :&]+',item)==None:
        item = item
    else:
        r = re.search(r'(?<=raven.min.js:2 )[.\-\w= :&]+',item).group(0)
        list1.append(r)

# processes the data line by line
for item in list1:
    if DEBUG:
        print(item)
    
    # checks if the line is valid for regex
    if item[0] in ("0","1","2","3","4","5","6","7","8","9", "U"):
        item = item
    else:
        if DEBUG:
            print(item)
        
        # assigns data to variables using regex
        time = re.search(r'(?<=time=)[a-zA-Z0-9: ]+', item).group(0)
        username = re.search(r'(?<=user=)[\w\- ]+', item).group(0)
        raw = re.search(r'(?<=raw=)[0-9:]+', item).group(0)
        actual = re.search(r'(?<=actual=)[0-9:]+', item).group(0)
        #print(re.search(r'(?<=bonus=)[0-9]+', item))
        if re.search(r'(?<=bonus=)[0-9]+', item)==None:
            bonus = ""
        else:
            bonus = re.search(r'(?<=bonus=)[0-9]+', item).group(0)
        date=re.search(r'(?<=Jul )[0-9]+',time).group(0)
        time1=re.search(rf'(?<=Jul {date} )[0-9:]+',time,re.IGNORECASE).group(0)
        time="7/{}/2020 {}".format(date,time1)
        hour=re.search(r'(?<=0:)[0-9]',raw).group(0)
        minute=re.search(rf'(?<=0:{hour}:)[0-9]+',raw).group(0)
        if len(minute)==1:
            raw="12:{}:0{}AM".format(hour, minute)
        else:
            raw="12:{}:{}AM".format(hour, minute)
        time="7/{}/2020 {}".format(date,time1)
        hour=re.search(r'(?<=0:)[0-9]',actual).group(0)
        minute=re.search(rf'(?<=0:{hour}:)[0-9]+',actual).group(0)
        if len(minute)==1:
            actual="12:{}:0{}AM".format(hour, minute)
        else:
            actual="12:{}:{}AM".format(hour, minute)
            
        # final output
        print("Time: {} Username: {} Raw: {} Actual: {} Bonus: {}".format(time, username, raw, actual, bonus))
