'''
Oregon trail
Authors: Ocra004, Shadowfax13 (Caleb Han), Ripsticker321, LJCoder619, Undefined_Error, DatMathBoy
'''

# imports
import random
import time
import sys

# main variables
oxen = 0
food = 0
ammo = 0
clothes = 0
parts = 0
miles_to_go = 2000

# introduction
print("OREGON TRAIL")
time.sleep(1)
print("By Ocra004, Shadowfax13, Ripsticker321, LJCoder619, Undefined_Error, DatMathBoy")
time.sleep(1)

# determine probabilities of getting stolen
def prob_theft(money):
    answer = ""
    if money >= 1000:
        rint = random.randint(1, 5)
        if rint == 1:
            answer = "$100 was stolen."
    elif (money > 500) and (money < 1000):
        rint = random.randint(1, 7)
        if rint == 1:
            answer = "$75 was stolen."
    else:
        rint = random.randint(1, 10)
        if rint == 1:
            answer = "$50 was stolen."
    return answer

# set dictionary for types of supplies
def supplies(money, oxen, food, ammo, clothes, parts):
    supplies_dict = {"money:": money, "oxen:": oxen, "food:": food, "ammo:": ammo, "clothes:": clothes, "parts:": parts}
    return supplies_dict

running = True
money = 6000
while running:
    print("Welcome to the Oregon Trail!")
    start_loop = True
    while start_loop:
        start = input("Would you like to 1: Leave or 2: Play? ")
        if start == "1":
            sys.exit()
        elif start == "2":
            start_loop = False
            running = False
        else:
            print("I do not recognise {}. Please try again.".format(start))
        shop = True
print("Loading...")
time.sleep(2)

# set up people
name_health = 100
name1_health = 100
name2_health = 100
name3_health = 100
name4_health = 100
name = input("What is the name of the leader: ")
name_1 = input("Name of second person: ")
name_2 = input("Name of third person: ")
name_3 = input("Name of fourth person: ")
name_4 = input("Name of fifth person: ")

# set up occupation
print("Great!")
print("Who do you want to be?")
print("1. Banker")
print("2. Storekeeper")
print("3. Worker at a factory")
print("4. Carpenter")
print("5. Silversmith")
choice = input("Role(number): ")
if choice == '1':
    print("Good Choice!")
    money = 6000
elif choice == '2':
    print("Nice")
    money = 5000
elif choice == '3':
    print("Ok!")
    money = 4000
elif choice == '4':
    print("Sure!")
    money = 3500
elif choice == '5':
    print("Crafty!")
    money = 5000
else:
    sys.exit()

# set up time
print("Select the month do you want to leave you must get to your destination before winter comes.")
print("1. February")
print("2. March")
print("3. April")
print("4. May")
print("5. June")
print("6. July")
print("7. August")
print("8. September")
month = input("What month?(put the number): ")
if month == '1':
    print("ok!")
    month = 'February 2'
elif month == '2':
    print("ok!")
    month = 'March 20'
elif month == '3':
    print("ok!")
    month = 'April 29'
elif month == '4':
    print("ok!")
    month = 'May 16'
elif month == '5':
    print("ok!")
    month = 'June 20'
elif month == '6':
    print("ok!")
    month = 'July 15'
elif month == '7':
    print("ok!")
    month = 'August 19'
elif month == '8':
    print("ok!")
    month = 'September 23'
else:
    sys.exit()

# buy supplies
print("Let's first go to the shop to buy supplies!")
shop_go = input("Type 1 to go!: ")
if shop_go == '1':
    shop = True
    while shop:
        oxen_choice = True
        food_choice = True
        ammo_choice = True
        clothes_choice = True
        parts_choice = True
        print("Welcome to Bob's Hardware shop! Select what you want to buy.")
        print("1.Yokes of oxen (150 dollars each)")
        print("2.Food (1 dollar per pound)")
        print("3.Ammunition (2 dollars per box)")
        print("4.Clothing (5 dollars per set)")
        print("5.Spare Parts (10 dollars each)")
        print('Enter "." to leave.')
        print('You have', money, "to spend")
        print('You have', oxen, "oxen")
        print("You have", food, "pounds of food")
        print("You have", ammo, "boxes of ammo")
        print("You have", clothes, "sets of clothes")
        print("You have", parts, "spare parts")
        shop_choice = input("What is your choice?: ")

        if shop_choice == ".":
            shop = False
        elif shop_choice == "1":
            while oxen_choice:
                oxen = int(input("How many yokes would you like to buy? "))
                if oxen < 0:
                    print("Please purchase a positive integer.")
                elif (oxen * 150) > money:
                    print("You do not have enough money.")
                else:
                    print("You purchased {} oxen.".format(oxen))
                    money = money - (oxen * 150)
                    oxen_choice = False

        elif shop_choice == "2":
            while food_choice:
                food = int(input("How many pounds of food would you like to buy? "))
                if food < 0:
                    print("Please purchase a positive integer.")
                elif food > money:
                    print("You do not have enough money.")
                else:
                    print("You purchased {} pounds of food.".format(food))
                    money = money - food
                    food_choice = False

        elif shop_choice == "3":
            while ammo_choice:
                ammo = int(input("How many boxes of ammunition would you like to buy? "))
                if ammo < 0:
                    print("Please purchase a positive integer.")
                elif (ammo * 2) > money:
                    print("You do not have enough money.")
                else:
                    print("You purchased {} boxes of ammo.".format(ammo))
                    money = money - (ammo * 2)
                    ammo_choice = False

        elif shop_choice == "4":
            while clothes_choice:
                clothes = int(input("How many sets of cloths would you like to buy? "))
                if clothes < 0:
                    print("Please purchase a positive integer.")
                elif (clothes * 5) > money:
                    print("You do not have enough money.")
                else:
                    print("You purchased {} sets of clothes.".format(clothes))
                    money = money - (clothes * 5)
                    clothes_choice = False

        elif shop_choice == "5":
            while parts_choice:
                parts = int(input("How many spare parts would you like to buy?(9 max) "))
                if parts < 0:
                    print("Please purchase a positive integer.")
                elif (parts * 10) > money:
                    print("You do not have enough money.")
                else:
                    print("You purchased {} spare parts.".format(parts))
                    money = money - (parts * 10)
                    parts_choice = False

else:
    sys.exit()

# initiate game
print("Let's go!")
print("Today is,", month, 1854)
go = input("Want to go?(y/n): ")
game = True
if go == 'y':
    while game:
        print("                  __________________ ")
        print("       (_ ___    /------------------\ ")
        print("       (*]_~_|\  |-/---\------/---\-| ")
        print("       .// .ll     \---/      \---/")
        print("1. Check supplies")
        print("2. Trade")
        print("3. Rest")
        print("4. Exit")
        choices = input("What do you want to do? ")
        if choices == "1":
            print(supplies(money, oxen, food, ammo, clothes, parts))
        elif choices == "2":
            # do trade function here
        elif choices == "3":
            if name_health <= 94:
                name_health += 5
            elif name1_health <= 94:
                name1_health += 5
            elif name2_health <= 94:
                name2_health += 5
            elif name3_health <= 94:
                name3_health += 5
            elif name4_health <= 94:
                name4_health += 5
        elif choices == "4":
            sys.exit()

# exit game
elif go == "n":
    sys.exit()
