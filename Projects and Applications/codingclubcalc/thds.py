# imports
import math
import other

# defining pi
pi = math.pi

# directing user input to functions
def main():
  x = input("Choose an option: [c]ube  ").lower()
  if x == "c":
    cube()
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

# forumulas for cube
def cube():
  print("side^3 = volume")
  print("side^2 = face area")
  print("base*6 = surface area")
  print("sqrt(2*(side^2) = face diagonal")
  print("sqrt(3)*side = cube diagonal")
  x = input("What do you know: [s]ide, [f]ace area, [v]olume, [su]rface area, [fa]ce diagonal, [c]ube diagonal ").lower()
  if x == "s":
    y = float(input("What is the side?" ))
    print("Volume: {}".format(y**3))
    print("Face area: {}".format(y**2))
    print("Surface area: {}".format(2*(side**2)))
    print("Face diagonal: {}".format(other.sqrt([2*(y**2)], "√")))
    print("Cube diaonal: {}".format(y*other.sqrt([3], "√")))
  elif x == "f":
    y = float(input("What is the face area?" ))
    z = other.rec([y], "√")
    print("Side: {}".format(z))
    print("Volume: ".format(z**3))
    print("Surface area: {}".format(6*z))
    print("Face diagonal: {}".format(other.sqrt([2*(z**2)], "√")))
    print("Cube diagonal: {}".format(math.sqrt(3)*z))
  elif x == "v":
    y = float(input("What is the volume?" ))
    z = y**(1/3)
    print("Side: {}".format(z))
    print("Face area: ".format(z**2))
    print("Surface area: {}".format(6*z))
    print("Face diagonal: {}".format(other.sqrt([2*(z**2)], "√")))
    print("Cube diagonal: {}".format(math.sqrt(3)*z))
  elif x == "su":
    y = float(input("What is the surface area?" ))
    z = y/6
    print("Side: {}".format(z))
    print("Face area: {}".format(y**2))
    print("Volume: ".format(z**3))
    print("Face diagonal: {}".format(other.sqrt([2*(z**2)], "√")))
    print("Cube diagonal: {}".format(math.sqrt(3)*z))
  elif x == "fa":
    y = float(input("What is the face diagonal?" ))
    z = other.sqrt([(y**2)/2],"√")
    print("Side: {}".format(z))
    print("Face area: {}".format(y**2))
    print("Volume: ".format(z**3))
    print("Surface area: {}".format(z*6))
    print("Cube diagonal: {}".format(math.sqrt(3)*z))
  elif x == "c":
    y = float(input("What is the cube diagonal?" ))
    z = y/(math.sqrt(3))
    print("Side: {}".format(z))
    print("Face area: {}".format(y**2))
    print("Volume: ".format(z**3))
    print("Surface area: {}".format(z*6))
    print("Face diagonal: {}".format(other.sqrt([2*(z**2)], "√")))
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")
