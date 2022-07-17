'''
Number Guess
Author: Caleb Han
'''

# imports
import random

# setup running variables
n = True
i = True

while n:
    # reset counter
    count = 0
    
    # user input and random number
    num = int(input("Pick a number for your maximum. "))
    secret_number = random.randint(0, num)
    
    # reset i
    i = True
    
    # set up difficulty with corresponding max guesses
    difficulty = input("Do you want to pick a difficulty? y/n ")
    if difficulty == "y":
        difficulty_choose = input("What difficulty do you want: [E]asy, [I]ntermediate, or [H]ard? ")
        if difficulty_choose.lower() == "e":
            max_guess = 10
            max_guess -= 1
            print("You will start with 10 tries.")
        elif difficulty_choose.lower() == "i":
            max_guess = 7
            max_guess -= 1
            print("You will start with 7 tries.")
        elif difficulty_choose.lower() == "h":
            max_guess = 4
            max_guess -= 1
            print("You will start with 4 tries.")
    elif difficulty == "n":
        max_guess = int(input("Enter the maximum number of tries. Enter 0 if you don't want a maximum number of tries. "))
        if max_guess == "0":
            max_guess = 100000
        else:
            max_guess -= 1
            
    # main game
    while i:
        # print out number of tries left and get user input
        print("You have %d tries left." % int(max_guess + 1 - count))
        guess = int(input("Guess an integer from 1 to %d! (If you are continuing, it is the same number. If you won previously, it is a different number.)  " % num))
        
        # if run out of guesses
        if max_guess == count:
            print("That was incorrect. ")
            print("Game over. You have reached the maximum number of tries, %d " % int(count + 1))
            i = False
            n = False
        
        # if correct guess
        elif guess == secret_number:
            count += 1
            print("You got it!")
            print("It took you", count, "tries!")
            secret_number = random.randint(0, num)
            yn = input("Do you want to try again? y/n ")
            if yn == "y":
                i = False
            elif yn == "n":
                i = False
                n = False

        # compare guess to correct answer
        else:
            difference = abs(secret_number - guess)
            count += 1
            if (guess > secret_number) and (difference >= (num / 2)):
                print("You guessed too high.")
            elif (guess > secret_number) and (difference <= (num / 10)):
                print("You guessed a little high.")
            elif (guess > secret_number):
                print("You guessed high.")
            elif (guess < secret_number) and (difference <= (num / 10)):
                print("You guessed a little low.")
            elif (guess < secret_number) and (difference >= (num / 2)):
                print("You guessed too low.")
            elif (guess < secret_number):
                print("You guessed low.")
