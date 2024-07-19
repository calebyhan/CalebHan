'''
Password Generator
Author: Caleb Han
'''

# imports
import random

# list of available characters to generate a password
lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "|", "\\", "`", "`", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?"]

def pwdGen(string, ln):
  # opens file to put sample passwords in
  f = open("password.txt", "a")
  
  # if password is right length
  if len(string) == ln:
    # write to file and close
    f.write(string + "\n")
    f.close()
    return
  # recursive loop to add characters until max hit
  main(string + lst[random.randint(0, len(lst) - 1)])
  
# delete everything in sample file
f = open("password.txt", "w")
f.close()

# get user input
user_input1 = int(input("How many passwords? "))
user_input2 = int(input("Length of password? "))

# generate x amount of passwords
for i in range(user_input):
  pwdGen("", user_input2)
