'''
Port scan practice
Author: Caleb Han
'''

# imports

import socket
import sys
import datetime

# if there are 2 shell arguments (file and target)
if len(sys.argv) == 2: 
  # get target object
  target = socket.gethostbyname(sys.argv[1])

  # output target and time
  print("----------------------------------------")
  print("Scanning target: " + target + "\n")
  print("Time started: " + str(datetime.datetime.now()) + "")
  print("----------------------------------------")
else:
  # if there are not enough arguments in shell command
  print("Invalid amount of arguments")
  print("Syntax: python3 main.py <ip>")

try: 
  # port scan 1-80 and print port if it is open
  for port in range(1, 81):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print("Port " + str(port) + " is open")
    s.close()

  # output time
  print("----------------------------------------")
  print("Scanning ended\n")
  print("Time Ended: " + str(datetime.datetime.now()) + "")
  print("----------------------------------------")
    
# if user exits by ctrl-c
except KeyboardInterrupt:
  print("\nExiting program")
  sys.exit()

# if hostname is not resolved
except socket.gaierror: 
  print("Hostname could not be resolved")
  sys.exit()

# if connection fails
except socket.error: 
  print("Could not connect to server")
  sys.exit() 
