'''
Coding Club Calculator
Authors: Caleb Han and Elynn An
'''

# uses python files in the same directory to shorten main.py
import twds
import thds
import calc
import form
import conversion
import other

# regular imports
import math

# user information
print("Welcome to the calculator and math stuffs.")
print("Enter 'quit' anytime to quit.")

# user input
user_input = input("Choose a directory: [ca]lc, [tw]o-d shapes, [th]ree-d shapes, [f]ormulas, \n[co]nversions ").lower()

# directs user choice to specific file
if user_input == "ca":
  calc.main()
elif user_input == "tw":
  twds.main()
elif user_input == "th":
  thds.main()
elif user_input == "f":
  form.main()
elif user_input == "co":
  conversion.main()
elif user_input == "quit":
  quit()
else:
  print("Wrong input. Try again.")
