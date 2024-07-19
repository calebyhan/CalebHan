'''
Alarm Clock
Author: Caleb Han
'''

# imports

import time
import datetime
import os
import random
import webbrowser
from os import system, name
from time import sleep

# clear console
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else: 
    _ = os.system('clear')

# convert h:m:s to s
def convertTo(lst):
  if len(lst) == 3:
    return ((lst[0] * 60 * 60) + (lst[1] * 60) + lst[2])
  elif len(lst) == 2:
    return ((lst[0] * 60 * 60) + (lst[1] * 60))
  else:
    return lst[0] * 60 * 60

# convert s to h:m:s
def convertFrom(sec):
  hours = sec // 3600
  minutes = (sec - (hours * 3600)) // 60
  seconds = sec - (hours * 3600) - (minutes * 60)
  return [hours, minutes, seconds]

# main loop
def main():
  # user input
  print("Please enter time in UTC-0")
  time_input = input("What time do you want the alarm to end? (h:m:s) ")
  time_input = list(map(int, time_input.split(":")))
  
  # open sound file, if it doesnt exist, add one with a alarm yt link
  f = open("sound.txt", "r")
  if not os.path.isfile("sound.txt"):
    print("Creating X file")
    f.write("https://www.youtube.com/watch?v=SkgTxQm9DWM")
    
  # assign said link to var
  link = f.readlines()[random.randint(0, len(f.readlines()))]
  
  #number of seconds and temp var
  num_seconds = convertTo(time_input)
  num_seconds1 = num_seconds
  time_convertion = [3600, 60, 1]
  
  # get current time
  start_time = datetime.datetime.now()
  start_time1 = sum([a*b for a,b in zip(time_convertion, [start_time.hour, start_time.minute, start_time.second])])
  
  # get delta time
  num_seconds1 = num_seconds - start_time1

  # print out remaining time until the alarm goes off  
  while True:
    start_time2 = datetime.datetime.now()
    if num_seconds1 <= 0:
      break
    time.sleep(1)
    num_seconds1 -= 1
    formatted_time = convertFrom(num_seconds1)
    print("{}:{}:{}".format(formatted_time[0], formatted_time[1], formatted_time[2]))
  webbrowser.open(link)

# run loop
main()
