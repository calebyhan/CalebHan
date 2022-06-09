'''
Tictactoe
Author: Caleb Han
'''

# imports
import random

# layout of boards
a_1 = " "
a_2 = " "
a_3 = " "
a_4 = " "
a_5 = " "
a_6 = " "
a_7 = " "
a_8 = " "
a_9 = " "

board = '''{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}'''.format(a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9)

board_choose = '''1|2|3
-----
4|5|6
-----
7|8|9'''

choices = list(range(1, 10))

# bot's X or O
bot_shape = ""

# assigning X or O
while True:
    user_shape = input("Choose O or X. \n")
    if user_shape not in ["O", "X"]:
        print("Invalid option.")
    else:
        if user_shape == "X":
            bot_shape = "O"
            break
        bot_shape = "X"
        break

# main loop
while True:
    # printing board
    print(board_choose)
    print('''{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}'''.format(a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9))
    # user input, error handling
    user_input = int(input("Choose a number from 1-9 that is not on the board. "))
    if user_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Invalid option.")
        break
    else:
        # board piece assignment and winning logic
        choices.remove(user_input)
        if user_input == 1:
            a_1 = user_shape
        elif user_input == 2:
            a_2 = user_shape
        elif user_input == 3:
            a_3 = user_shape
        elif user_input == 4:
            a_4 = user_shape
        elif user_input == 5:
            a_5 = user_shape
        elif user_input == 6:
            a_6 = user_shape
        elif user_input == 7:
            a_7 = user_shape
        elif user_input == 8:
            a_8 = user_shape
        elif user_input == 9:
            a_9 = user_shape
        bot_choose = random.choice(choices)
        choices.remove(bot_choose)
        if bot_choose == 1:
            a_1 = bot_shape
        elif bot_choose == 2:
            a_2 = bot_shape
        elif bot_choose == 3:
            a_3 = bot_shape
        elif bot_choose == 4:
            a_4 = bot_shape
        elif bot_choose == 5:
            a_5 = bot_shape
        elif bot_choose == 6:
            a_6 = bot_shape
        elif bot_choose == 7:
            a_7 = bot_shape
        elif bot_choose == 8:
            a_8 = bot_shape
        elif bot_choose == 9:
            a_9 = bot_shape
        if (a_1 == user_shape) and (a_2 == user_shape) and (a_3 == user_shape):
            print("You win!")
            break
        elif (a_4 == user_shape) and (a_5 == user_shape) and (a_6 == user_shape):
            print("You win!")
            break
        elif (a_7 == user_shape) and (a_8 == user_shape) and (a_9 == user_shape):
            print("You win!")
            break
        elif (a_1 == user_shape) and (a_4 == user_shape) and (a_7 == user_shape):
            print("You win!")
            break
        elif (a_2 == user_shape) and (a_5 == user_shape) and (a_8 == user_shape):
            print("You win!")
            break
        elif (a_3 == user_shape) and (a_6 == user_shape) and (a_7 == user_shape):
            print("You win!")
            break
        elif (a_1 == user_shape) and (a_5 == user_shape) and (a_9 == user_shape):
            print("You win!")
            break
        elif (a_3 == user_shape) and (a_5 == user_shape) and (a_7 == user_shape):
            print("You win!")
            break
        if (a_1 == bot_shape) and (a_2 == bot_shape) and (a_3 == bot_shape):
            print("You lost.")
            break
        elif (a_4 == bot_shape) and (a_5 == bot_shape) and (a_6 == bot_shape):
            print("You lost.")
            break
        elif (a_7 == bot_shape) and (a_8 == bot_shape) and (a_9 == bot_shape):
            print("You lost.")
            break
        elif (a_1 == bot_shape) and (a_4 == bot_shape) and (a_7 == bot_shape):
            print("You lost.")
            break
        elif (a_2 == bot_shape) and (a_5 == bot_shape) and (a_8 == bot_shape):
            print("You lost.")
            break
        elif (a_3 == bot_shape) and (a_6 == bot_shape) and (a_7 == bot_shape):
            print("You lost.")
            break
        elif (a_1 == bot_shape) and (a_5 == bot_shape) and (a_9 == bot_shape):
            print("You lost.")
            break
        elif (a_3 == bot_shape) and (a_5 == bot_shape) and (a_7 == bot_shape):
            print("You lost.")
            break
