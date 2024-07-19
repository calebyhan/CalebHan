'''
Beta testing calculator for future project
Author: Caleb Han
'''

# imports
import math
import time

# add 2 integers
def add(a, b):
    return int(a)+int(b)

# subtract 2 integers
def subtract(a, b):
    return int(a)-int(b)

# multiply 2 integers
def mult(a, b):
    return int(a)*int(b)

# divide 2 integers
def div(a, b):
    return int(a)/int(b)

# exponental power
def ex(a, b):
    return int(a)**int(b)

# sqrt of an integer
def sqrt(a):
    a = int(a)
    return math.sqrt(a)

# check if unput is an integer
def checknum(num):
    if type(int(num)) != int:
        return False
    else:
        return True

running = True

# main loop
while running:
    # get input
    question = input("""What do you want to do? ([A]dd, [S]ubtract, [M]ultiply, [D]ivide, [E]xponents,
[Sq]uare root, [Q]uit? """)
    
    # error handling
    if question.lower() not in ["a", "s", "m", "d", "q", "e", "sq"]:
        print("Sorry, your input was invalid.")
        
    # quit application
    elif question.lower() == "q":
            running = False
    
    # handle arguments
    elif question.lower() == "a":
        print("a+b")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            num2 = input("What is b? Enter q to go quit. ")
            if num2.lower() == "q":
                running = False
            elif checknum(num2):
                print("{} + {} = {}.".format(num1, num2, add(num1, num2)))
        else:
            print("Sorry, your input was invalid.")
    elif question.lower() == "s":
        print("a-b")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            num2 = input("What is b? Enter q to go quit. ")
            if num2.lower() == "q":
                running = False
            elif checknum(num2):
                print("{} - {} = {}.".format(num1, num2, subtract(num1, num2)))
    elif question.lower() == "m":
        print("a*b")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            num2 = input("What is b? Enter q to go quit. ")
            if num2.lower() == "q":
                running = False
            elif checknum(num2):
                print("{} * {} = {}.".format(num1, num2, mult(num1, num2)))
    elif question.lower() == "d":
        print("a/b")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            num2 = input("What is b? Enter q to go quit. ")
            if num2.lower() == "q":
                running = False
            elif checknum(num2):
                print("{} / {} = {}.".format(num1, num2, div(num1, num2)))
    elif question.lower() == "e":
        print("a^b")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            num2 = input("What is b? Enter q to go quit. ")
            if num2.lower() == "q":
                running = False
            elif checknum(num2):
                print("{} ^ {} = {}.".format(num1, num2, ex(num1, num2)))
    elif question.lower() == "sq":
        print("sqrt{a}")
        num1 = input("What is a? Enter q to go quit. ")
        if num1.lower() == "q":
            running = False
        elif checknum(num1):
            print("sqrt\{{}\} = {}.".format(num1, sqrt(num1)))
            
    # sleep and loop
    time.sleep(1)
