'''
Morse Code
Author: Caleb Han
'''

# imports
import time
import sys
import pygame

# regular characters to morse dictionary
code = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
  'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",
  'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
  'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
  'x': "-..-", 'y': "-.--", 'z': "--..",
  '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....",
  '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----",
  ' ': "/", '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.",
  '@': ".--.-.", '-': "-....-", '"': ".-..-.", ':': "---...", ';': "---...",
  '=': "-...-", '!': "-.-.--", '/': "-..-.", '(': "-.--.", ')': "-.--.-"
}

def encoder(mc_input):
  output = ""
  for i in range(len(mc_input)):
    # checks if character is newline, return that if
    if mc_input[i] == "\n":
      output += "\n"
    # checks if character is space, return that if
    elif mc_input[i] == " ":
      output += "/"
    # if not in dictionary, throw error
    elif mc_input[i].lower() not in code:
      print("Character {} not supported.".format(mc_input[i]))
      break
    else:
      # else, translate from dictionary
      output += code[mc_input[i]]
    output += " "
  # return output
  return output

def decoder(mc_input):
  output = ""
  mc_input1 = mc_input.split(" ")
  for i in range(len(mc_input1)):
    # if character is backslash, add a space
    if mc_input1[i] == "/":
      output += " "
    # if character is newline, return that
    elif mc_input1[i] == "\n":
      output += "\n"
    try:
      # if character is in the dict, translate
      temp = list(code.keys())[list(code.values()).index(mc_input1[i])]
      output += temp
    except:
      # error throws if not
      print("Character {} not supported.".format(mc_input1[i]))
      break
  # return output
  return output

# pygame setup
FREQUENCY = 44100 
BITSIZE = -16
CHANNELS = 2
BUFFER = 1024
FRAMERATE = 60

def main():
  # set up pygame
  pygame.init()
  pygame.mixer.init(FREQUENCY, BITSIZE, CHANNELS, BUFFER)
  sound = pygame.mixer.Sound("dash.ogg")
  clock = pygame.time.Clock()
  sound.play()
  while pygame.mixer.get_busy():
    clock.tick(FRAMERATE)
    
  # get user input
  m_type = input("[E]ncode or [D]ecode? ")
  m_str = input("What is the text you want to translate? ")
  if m_type.lower() == "e":
    print(encoder(m_str))
  elif m_type.lower() == "d":
    print(decoder(m_str))
  else:
    print("Incorrect type.")

# main loop
while True:
  main()
  exit = input("Do you want to exit? [y]es/[n]o ")
  if exit.lower() == "y":
    break
  elif exit.lower() == "n":
    continue
  print("Incorrect type.")
  break
