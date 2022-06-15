# imports
import math
import other

# direct user input to functions
def main():
  x = input("Choose an option: [me]tric, [l]ength, [v]olume, [ti]me, [te]mperature, [m]ass ").lower()
  if x == "me":
    metric()
  elif x == "l":
    length()
  elif x == "v":
    volume()
  elif x == "ti":
    time()
  elif x == "te":
    temp()
  elif x == "m":
    mass()
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

# conversions for metric conversions
def metric():
  metric_conversions = {"a": 1000000000000000000, "f": 1000000000000000, "p": 1000000000000, "n": 1000000000, "μ": 1000000, "m": 1000, "c": 100, "d": 10, "b": 1, "da": 1/10, "h": 1/100, "k": 1/1000, "M": 1/1000000, "G": 1/1000000000, "T": 1/1000000000000, "P": 1/1000000000000000, "E": 1/1000000000000000000}
  print("Units: a, f, p, n, μ, m, c, d, [b]ase, da, h, k, M, G, T, P, E")
  print("Note: from and to has to be specific.")
  x = float(input("Value: "))
  y = input("From: ").lower()
  z = input("To: ").lower()
  print("{} --> {} = {}".format(str(x)+y, z, x*metric_conversions[y]/metric_conversions[z]))

# didn't finish project
def length():
  print()

def volume():
  print()

def time():
  print()

def temp():
  print()

def mass():
  print()
