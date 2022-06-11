'''
A swiss knife of codes
Authors: Caleb Han and Elynn An
'''

# imports
import random
import math
import datetime
import time
import re
from IPython.display import clear_output
from playsound import playsound

# convert secods to hours, minutes, and seconds
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  sec = str(sec)[0:2]
  if re.search(r"[.]", sec) == None:
    sec = sec
  else:
    sec = "0" + sec[0:1]
  hours = mins // 60
  mins = mins % 60
  return("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

# add two numbers
def add(x, y):
  return float(float(x) + float(y))

# subtract two numbers
def subtract(x, y):
  return float(float(x) - float(y))

# multiply two numbers
def multiply(x, y):
  return float(float(x) * float(y))

# divide two numbers
def divide(x, y):
  return float(float(x) / float(y))

# sqrt of a number
def sqrt(x):
  return math.sqrt(float(x))

# exponent power
def exponent(x, y):
  return float(float(x) ** float(y))

# pythagorean of two bases
def pythagorasbb(base1, base2):
  return sqrt(float(float(base1)**2)+float(float(base2)**2))

# pythagorean of one base and hypotenuse
def pythagorasbh(base1, hypotenuse):
  return sqrt(float(float(hypotenuse)**2)-float(float(base1)**2))

# log base of a number
def log(x, base):
  return math.log(float(x), float(base))

# user input for which program to run
user_input = input('''Please choose an option: [st]opwatch, [ca]lculator, [di]ce game, [ti]me, [tic]-tac-toe, 
[con]nect5, [mor]se code, [cea]sar cipher, [bl]ackjack, ''')

# checks if the input is valid
if user_input.lower() not in ["st", "ca", "di", "ti", "tic", "con", "mor", "cea", "bl"]:
  print("Please choose a valid option.")

# stopwatch
if user_input.lower() == 'st':
  input("Press enter to begin. ")
  start_time = time.time()
  input("Press enter to stop the stopwatch. ")
  end_time = time.time()
  lapsed_time = end_time - start_time
  print(time_convert(lapsed_time))

# simple calculator
elif user_input.lower() == 'ca':
  # choosing option
  calc_input = input("Please choose an option: [a]dd, [s]ubtract, [m]ultiply, [d]ivide, [e]xponent, [sq]rt, [py]thagoras, [lo]g,  ")
  
  # error handling
  if calc_input.lower() not in ["a", "s", "m", "d", "e", "sq", "py", "lo"]:
    print("Please choose a valid option")
    
  # different options
  elif calc_input.lower() == "a":
    print("x + y")
    x = input("x: ")
    y = input("y: ")
    print("{} + {} = {}".format(x, y, add(x, y)))
  elif calc_input.lower() == "s":
    print("x - y")
    x = input("x: ")
    y = input("y: ")
    print("{} - {} = {}".format(x, y, subtract(x, y)))
  elif calc_input.lower() == "m":
    print("x * y")
    x = input("x: ")
    y = input("y: ")
    print("{} * {} = {}".format(x, y, multiply(x, y)))
  elif calc_input.lower() == "d":
    print("x / y")
    x = input("x: ")
    y = input("y: ")
    print("{} / {} = {}".format(x, y, divide(x, y)))
  elif calc_input.lower() == "e":
    print("x ^ y")
    x = input("x: ")
    y = input("y: ")
    print("{} ^ {} = {}".format(x, y, exponent(x, y)))
  elif calc_input.lower() == "sq":
    print("√x")
    x = input("x: ")
    print("√{} = {}".format(x, sqrt(x)))
  elif calc_input.lower() == "py":
    c_py_input = input("What do you know: base and base or base and hypotenuse (bb or bh) ")
    if c_py_input.lower() == "bb":
      x = input("Base 1: ")
      y = input("Base 2: ")
      print("Hypotenuse: {}".format(pythagorasbb(x, y)))
    elif c_py_input.lower() == "bh":
      x = input("Base 1: ")
      y = input("Hypotenuse: ")
      print("Base 2: {}".format(pythagorasbh(x, y)))
    else:
      print("Invalid choice.")
  elif calc_input.lower() == "lo":
    print("log_base x")
    x = input("x: ")
    y = input("Base: ")
    print("log_{} {} = {}".format(y, x, log(x, y)))

# dice game
elif user_input.lower() == "di":
  print("Rolling...")
  time.sleep(2)
  
  # choosing user and bot dice
  user_dice = random.choice([1, 2, 3, 4, 5, 6])
  bot_dice = random.choice([1, 2, 3, 4, 5, 6])
  print("Bot rolling...")
  time.sleep(2)
  
  # winning conditions
  if user_dice > bot_dice:
    print("You win! You rolled {} and the bot rolled {}.".format(user_dice, bot_dice))
  elif user_dice < bot_dice:
    print("You lost. You rolled {} and the bot rolled {}.".format(user_dice, bot_dice))
  else:
    print("Tie! Both contestants rolled {}.".format(user_dice))

# time
elif user_input.lower() == "ti":
  today = datetime.datetime.now()
  print(today.strftime("%A, %B, %d, %Y, %I:%M:%S %p"))

# tic-tac-toe (same as previously uploaded tic-tac-toe, just copied)
elif user_input.lower() == "tic":
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

  choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  bot_shape = ""

  while True:
      user_shape = input("Choose O or X. ")
      if user_shape not in ["O", "X"]:
          print("Invalid option.")
      else:
          if user_shape == "X":
              bot_shape = "O"
              break
          bot_shape = "X"
          break

  while True:
    print(board_choose)
    print('''{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}'''.format(a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9))
    user_input = int(input("Choose a number from 1-9 that is not on the board. "))
    if user_input not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Invalid option.")
        break
    else:
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
      if choices == []:
        print("Tie!")
        break
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
    print('''{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}'''.format(a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9))


# connect 5 (never implemented)
elif user_input.lower() == "con":
  def display_board(board):
    clear_output()

# morse_code
elif user_input.lower() == "mor":
  # dictionary of numeric-alphabetical translation to morse
  print('''A: .-
B: -...
C: -.-.
D: -..
E: .
F: ..-.
G: --.
H: ....
I: ..
J: .---
K: -.-
L: .-..
M: --
N: -.
O: ---
P: .--.
Q: --.-
R: .-.
S: ...
T: -
U: ..-
V: ...-
W: .--
X: -..-
Y: -.--
Z: --..
1: .----
2: ..---
3: ...--
4: ....-
5: .....
6: -....
7: --...
8: ---..
9: ----.
0: -----
  
Please separate digits/letters with a space and words/numbers with a /.''')

  morse_dict = {"A": ".-","B": "-...",
  "C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7":"--...","8": "---..","9": "----.","0": "-----"}
  print(morse_dict.values())
  
  # user chooses from encoding or decoding
  m_ed = input("[E]ncode or [D]ecode? ")
  m_e_output = ""
  m_d_output = ""
  
  # encoding choice
  if m_ed.lower() == "e":
    # user input
    m_e = input("What do you want to encode? ")
    
    # loop through each character
    for char in m_e:
      # if character is vaid
      if char.lower() in "abcdefghijklmnopqrstuvwxyz":
        m_e_output += morse_dict[char.upper()]
        m_e_output += " "
      elif char in "1234567890":
        m_e_output += morse_dict[char.upper()]
        m_e_output += " "
      elif char == " ":
        m_e_output += "/"
      else:
        print("Your string has non-acceptable characters.")
        break
    
    # print output
    print(m_e_output)
  
  # decoding choice
  elif m_ed.lower() == "d":
    m_letter = ""
    # user input
    m_d = input("What do you want to decode? ")
    m_d += " "
    
    # loop through each character
    for char in m_d:
      # sort through what type of character it is
      if char == " ":
        itemsList = morse_dict.items()
        for item in itemsList:
          if item[1] == m_letter:
            m_d_output += item[0]
        m_letter = ""
      elif char == "/":
        itemsList = morse_dict.items()
        for item in itemsList:
          if item[1] == m_letter:
            m_d_output += item[0]
        m_letter = ""
        m_d_output += " "
      elif char not in[".", "-"]:
        print("Error.")
        break
      else:
        m_letter += char
  else:
    print("Wrong input. Please enter E or D.")
  
  # print output
  print(m_d_output)

# caesar cipher
elif user_input.lower() == "cea":
  # translation dictionary
  ceasar_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
  
  # user input
  c_input = input("[E]ncode or [D]ecode? ")
  
  # encoding choice
  if c_input.lower() == "e":
    c_e_output = ""
    
    # user input
    c_e_string = input("What do you want to encode? Only letters, numbers, and ['.', ',', '?', '!'] ")
    
    # getting the rotate key
    c_e_input = int(input("Choose a number from 0-26. "))
    
    # error handling
    if (c_e_input > 26) or (c_e_input < 0):
      print("Wrong input. Please enter a number from 0-26.")
    else:
      new_c_dict = {}
      
      # rotating the caesar cipher
      for item in ceasar_dict.items():
        value = item[1]-c_e_input
        if value > 26:
          value = value - 26
        elif value < 1:
            value += 26
        new_c_dict[item[0]] = (value)
        
      # getting new string
      for char in c_e_string:
        if char in [".", ",", "?", "!", " "]:
          c_e_output += char
        elif type(char) == int:
          c_e_output += char
        elif type(char) == float:
          c_e_output += char
        else:
          for item in ceasar_dict.items():
            if item[0] == char.upper():
              c_a = item[1]
              for item in new_c_dict.items():
                if c_a == item[1]:
                  c_e_output += item[0]
    
    # print output
    print(c_e_output)
    
  # decoding choice
  elif c_input.lower() == "d":
    c_d_output = ""
    
    # user input
    c_d_string = input("What do you want to decode? Only letters, numbers, and ['.', ',', '?', '!'] ")
    c_d_input = int(input("Choose a number from 0-26. "))
    
    # error handling
    if (c_d_input > 26) or (c_d_input < 0):
      print("Wrong input. Please enter a number from 0-26.")
    else:
      new_c_dict = {}
      
      # create rotated dictionary
      for item in ceasar_dict.items():
        value = item[1]-c_d_input
        if value > 26:
          value = value - 26
        elif value < 1:
            value += 26
        new_c_dict[item[0]] = (value)
        
      # iterate through each character in input
      for char in c_d_string:
        if char in [".", ",", "?", "!", " "]:
          c_d_output += char
        elif type(char) == int:
          c_d_output += char
        elif type(char) == float:
          c_d_output += char
        else:
          for item in ceasar_dict.items():
            if item[0] == char.upper():
              c_a = item[1]
              for item in new_c_dict.items():
                if c_a == item[1]:
                  c_d_output += item[0]
    
    # print output
    print(c_d_output)
  else:
    print("Wrong input. Please enter E or D.")

# blackjack
elif user_input.lower() == "bl":
  # set up user and bot hands
  b_set = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
  b_u_1 = random.choice(b_set)
  b_u_2 = random.choice(b_set)
  b_b_1 = random.choice(b_set)
  b_b_2 = random.choice(b_set)
  
  # ace handling (score +1 or +11
  if b_u_1 == "A":
    x = input("1 or 11 ")
    if x == "1":
      b_u_1 = 1
    else:
      b_u_1 = 11
  elif b_u_2 == "A":
    x = input("1 or 11 ")
    if x == "1":
      b_u_2 = 1
    else:
      b_u_2 = 11
  elif b_b_1 == "A":
    x = random.choice([1, 11])
    b_b_1 = x
  elif b_b_2 == "A":
    x = random.choice([1, 11])
    b_b_2 = x
  b_u = [b_u_1, b_u_2]
  b_b = [b_b_1, b_b_2]
  
  # print cards
  print("Your cards: {}, {}".format(b_u_1, b_u_2))
  print("Bot's cards: {}, ?".format(b_b_1))
  
  # main loop
  while True:
    bu_sum = 0
    for num in b_u:
      if num in ["K", "Q", "J"]:
        bu_sum += 10
      else:
        bu_sum += int(num)
    bb_sum = 0
    
    # check if face card
    for num in b_b:
      if num in ["K", "Q", "J"]:
        bb_sum += 10
      else:
        bb_sum += int(num)
        
    # winning conditions
    if (bu_sum == 21) and (bb_sum == 21):
      print("Tie! Both got 21.")
      break
    elif bu_sum == 21:
      print("You won! You got 21.")
      break
    elif bb_sum == 21:
      print("You lost. The bot got 21.")
      break
    elif (bu_sum > 21) and (bb_sum > 21):
      print("Tie! Both exceeded 21.")
      break
    elif bu_sum > 21:
      print("You lost. Your sum exceeded 21.")
      break
    elif bb_sum > 21:
      print("You won! The bot's sum exceeded 21.")
      break
    
    # print cards and get user input
    print("Your cards: {}".format(b_u))
    print("The bot's cards: {}".format(b_b))
    b_hosu = input("[H]it or [S]tand? ")
    
    # if user chooses hit
    if b_hosu.lower() == "h":
      x = random.choice(b_set)
      if x == "A":
        x = input("1 or 11 ")
        if x == "1":
          b_u.append(1)
        else:
          b_u.append(11)
      else:
        b_u.append(x)
      bu_sum = 0
      for num in b_u:
        if num in ["K", "Q", "J"]:
          bu_sum += 10
      if bu_sum > 21:
        print("You lost. Your sum exceeded 21.")
        break
      x = random.choice(b_set)
      if x == "A":
        x = random.choice([1, 11])
        if x == 1:
          b_b.append(1)
        else:
          b_b.append(11)
      else:
        b_b.append(x)
      bu_sum = 0
      for num in b_u:
        if num in ["K", "Q", "J"]:
          bu_sum += 10
        else:
          bu_sum += int(num)
      bb_sum = 0
      for num in b_b:
        if num in ["K", "Q", "J"]:
          bb_sum += 10
        else:
          bb_sum += int(num)
       
      # winning conditions
      if (bu_sum == 21) and (bb_sum == 21):
        print("Tie! Both got 21.")
        break
      elif bu_sum == 21:
        print("You won! You got 21.")
        break
      elif bb_sum == 21:
        print("You lost. The bot got 21.")
        break
      elif (bu_sum > 21) and (bb_sum > 21):
        print("Tie! Both exceeded 21.")
        break
      elif bu_sum > 21:
        print("You lost. Your sum exceeded 21.")
        break
      elif bb_sum > 21:
        print("You won! The bot's sum exceeded 21.")
        break
    
    # if user chooses stand
    elif b_hosu.lower() == "s":
      bu_sum = 0
      for num in b_u:
        if num in ["K", "Q", "J"]:
          bu_sum += 10
        else:
          bu_sum += int(num)
      bb_sum = 0
      for num in b_b:
        if num in ["K", "Q", "J"]:
          bb_sum += 10
        else:
          bb_sum += int(num)
          
      # winning conditions
      if (bu_sum == 21) and (bb_sum == 21):
        print("Tie! Both got 21.")
        break
      elif bu_sum == 21:
        print("You won! You got 21.")
        break
      elif bb_sum == 21:
        print("You lost. The bot got 21.")
        break
      elif (bu_sum > 21) and (bb_sum > 21):
        print("Tie! Both exceeded 21.")
        break
      elif bu_sum > 21:
        print("You lost. Your sum exceeded 21.")
        break
      elif bb_sum > 21:
        print("You won! The bot's sum exceeded 21.")
        break
      elif bu_sum > bb_sum:
        x = random.choice(b_set)
        if x == "A":
          x = random.choice([1, 11])
          if x == 1:
            b_b.append(1)
          else:
            b_b.append(11)
        else:
          b_b.append(x)
        bb_sum = 0
        for num in b_b:
          if num in ["K", "Q", "J"]:
            bb_sum += 10
          else:
            bb_sum += int(num)
        
        # winning conditions
        if bb_sum > 21:
          print("You won! The bot's sum exceeded 21.")
          break
        else:
          if bu_sum > bb_sum:
            print("You won! You have more points than the bot!")
            break
          else:
            print("You lost. The bot has more points than you.")
            break
      elif bb_sum > bu_sum:
        print("You lost. The bot has more points than you.")
        break
    elif b_hosu.lower() == "hehe":
      print("You won....")
      break
  print("Your cards: {}".format(b_u))
  print("The bot's cards: {}".format(b_b))
