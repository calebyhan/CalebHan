import game
import time
import board

# instructions and starting game
playAgain = "y"
print("\nWelcome to Tic-Tac-Toe. Place your marker by selecting a number on this refernce board, provided that the space is not occupied already. The board will be updated every turn. Have fun!\n")
print(" 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8 \n")
input("Enter anything to continue once you understand the rules.\n")

while playAgain != "n":
    game()
    playAgain = input("Would you like to play again? (y/n): ")
    print()

def game():
    '''
    Runs the game itself
    '''

    board1 = board.Board()
    end = True
    if board1.assign == "You":
        print(board1)
    while end:
        if board1.assign == "You":
            print("Your move.")
            while True:
                user_input = int(input("Enter your move: "))
                if board1.place(user_input) == False:
                    print("That place is taken. Try again.")
                else:
                    break
            print(board1)
        else:
            print("My turn.\n")
            time.sleep(2)
            board1.botMove()
            print(board1)

        check_end = board1.check_end()
        if check_end == -1:
            print("You have drawed.")
            end = False
        elif check_end == 1:
            print("You win.")
            end = False
        elif check_end == 0:
            print("You lost.")
            end = False