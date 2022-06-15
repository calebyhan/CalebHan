# imports
import math
import other

# number storage
NUMS = []

# directs user input to a function
def main():
  x = input("Choose an option: [a]dd, [s]ubtract, [m]ultiply, [d]ivide, [e]xponent, [sq]are root, [fa]ctorial ").lower()
  if x == "a":
    add()
  elif x == "s":
    subtract()
  elif x == "m":
    multiply()
  elif x == "d":
    divide()
  elif x == "e":
    exponent()
  elif x == "sq":
    sqrt()
  elif x == "fa":
    factorial()
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

# functions for adding, subtracting, multiplying, dividing, x to the power, square root, and factorial
def add():
  answer = 0
  a_for= int(input("How many number(s) do you want to add? "))
  if a_for == "quit":
    quit()
  for i in range(a_for):
    NUMS.append(float(input("Number: ")))
  answer = other.rec(NUMS, "+")
  print("Answer: {}".format(answer))

def subtract():
  answer = 0
  a_for= int(input("How many number(s) do you want to subtract? "))
  if a_for == "quit":
    quit()
  for i in range(a_for):
    NUMS.append(float(input("Number: ")))
  answer = other.rec(NUMS, "-")
  print("Answer: {}".format(answer))

def multiply():
  answer = 0
  a_for= int(input("How many number(s) do you want to multiply? "))
  if a_for == "quit":
    quit()
  for i in range(a_for):
    NUMS.append(float(input("Number: ")))
  answer = other.rec(NUMS, "*")
  print("Answer: {}".format(answer))

def divide():
  answer = 0
  a_for= int(input("How many number(s) do you want to divide? "))
  if a_for == "quit":
    quit()
  for i in range(a_for):
    NUMS.append(float(input("Number: ")))
  answer = other.rec(NUMS, "/")
  print("Answer: {}".format(answer))

def exponent():
  answer = 0
  a_for = float(input("Base: "))
  if a_for == "quit":
    quit()
  NUMS.append(a_for)
  a_for = float(input("Power: "))
  if a_for == "quit":
    quit()
  NUMS.append(a_for)
  answer = other.rec(NUMS, "^")
  print("Answer: {}".format(answer))

def sqrt():
  answer = 0
  a_for = float(input("Number: "))
  if a_for == "quit":
    quit()
  NUMS.append(a_for)
  answer = other.rec(NUMS, "√")
  print("Answer: {}".format(answer))

def factorial():
  answer = 0
  a_for = float(input("Number: "))
  if a_for == "quit":
    quit()
  NUMS.append(a_for)
  answer = other.rec(NUMS, "!")
  print("Answer: {}".format(answer))
