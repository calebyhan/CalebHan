# imports
import math
import other

# defining pi
pi = math.pi

# direct user input to functions
def main():
  x = input("Choose an option: [ci]rcle, [re]ctangle, [sq]uare, [tri]angle, [tra]pezoid, [rh]ombus,  ").lower()
  if x == "ci":
    circle()
  elif x == "re":
    rectangle()
  elif x == "sq":
    square()
  elif x == "tri":
    triangle()
  elif x == "tra":
    trapezoid()
  elif x == "rh":
    rhombus()
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

# functions of formulas for circles, rectangles, squares, triangles, trapezoids, rhombuses
def circle():
  print("Area = pi*radius^2")
  print("Circumference = 2*pi*radius")
  x = input("What do you know: [a]rea, [r]adius, or [c]ircumference ").lower()
  if x == "a":
    y = float(input("What is the area? "))
    print("Radius: {}".format(other.rec([y/pi],"√")))
    print("Circumference: {}".format(2*other.rec([y/pi],"√")*pi))
  elif x == "r":
    y = float(input("What is the radius? "))
    print("Area: {}".format(pi*(y**2)))
    print("Circumference: {}".format(pi*2*y))
  elif x == "c":
    y = float(input("What is the circumference? "))
    print("Radius: {}".format(y/(2*pi)))
    print("Area: {}".format(pi*(y/(2*pi)**2)))
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

def rectangle():
  print("Area = side1*side2")
  print("Perimeter = 2*(side1+side2)")
  print("Diagonal = sqrt(side1^2+side2^2)")
  x = input("What do you know: [s]ides, [a]rea and side, [p]erimeter and side, [d]iagonal and side ").lower()
  if x == "s":
    y = float(input("What is side 1? "))
    z = float(input("What is side 2? "))
    print("Area: {}".format(y*z))
    print("Perimeter: {}".format(2*(y+z)))
    print("Diagonal: {}".format(other.rec([(y**2)+(z**2)], "√")))
  elif x == "a":
    y = float(input("What is the area? "))
    z = float(input("What is the side? "))
    print("Other side: {}".format(y/z))
    print("Perimeter: {}".format(2*(z+(y/z))))
    print("Diagonal: {}".format(other.rec([((y/z)**2)+(z**2)], "√")))
  elif x == "p":
    y = float(input("What is the perimeter? "))
    z = float(input("What is the side? "))
    print("Other side: {}".format((y/2)-z))
    print("Area: {}".format(((y/2)-z)*z))
    print("Diagonal: {}".format(other.rec([(((y/2)-z)**2)+(z**2)], "√")))
  elif x == "d":
    y = float(input("What is the diagonal? "))
    z = float(input("What is the side? "))
    print("Other side: {}".format(other.rec([(y**2)-(z**2)], "√")))
    print("Area: {}".format(other.rec([(y**2)-(z**2)], "√")*z))
    print("Perimeter: {}".format(2*((other.rec([(y**2)-(z**2)], "√"))+z)))
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

def square():
  print("Area = side^2")
  print("Perimeter = 4*side")
  print("Diagonal = sqrt(2*(side)^2)")
  x = input("What do you know: [s]ide, [a]rea, [p]erimeter, [d]iagonal ").lower()
  if x == "s":
    y = float(input("What is the side? "))
    print("Area: {}".format(y**2))
    print("Perimeter: {}".format(4*y))
    print("Diagonal: {}".format(other.rec([2*(y**2)], "√")))
  elif x == "a":
    y = float(input("What is the area? "))
    print("Side: {}".format(other.rec([y], "√")))
    print("Perimeter: {}".format(4*other.rec([y], "√")))
    print("Diagonal: {}".format(2*(other.rec([y], "√"))))
  elif x == "p":
    y = float(input("What is the perimeter? "))
    print("Side: {}".format(y/4))
    print("Area: {}".format((y/4)**2))
    print("Diagonal: {}".format(other.rec([2*((y/4)**2)], "√")))
  elif x == "d":
    y = float(input("What is the diagonal? "))
    print("Side: {}".format(other.rec([(y**2)/2], "√")))
    print("Area: {}".format(other.rec([(y**2)/2], "√")**2))
    print("Perimeter: {}".format(4*other.rec([(y**2)/2], "√")))
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

def triangle():
  v = input("Right triangle? [y]es or [n]o ").lower()
  if v == "y":
    print("leg1^2+leg2^2 = hypotenuse^2")
    print("(base*height)/2 = area")
    print("leg1+leg2+hypotenuse = perimeter")
    x = input("What do you know: [l]eg and leg, [h]ypotenuse and leg, [a]rea and leg ").lower()
    if x == "l":
      y = float(input("What is leg 1? "))
      z = float(input("What is leg 2? "))
      print("Hypotenuse: {}".format(math.sqrt((y**2)+(z**2))))
      print("Area: {}".format((y*z)/2))
      print("Perimeter: {}".format(math.sqrt((y**2)+(z**2))+y+z))
    elif x == "h":
      y = float(input("What is the leg? "))
      z = float(input("What is the hypotenuse? "))
      print("Other leg: {}".format(math.sqrt(z^2-y^2)))
      print("Area: {}".format((math.sqrt(z^2-y^2)*y)/2))
      print("Perimeter: {}".format(math.sqrt(z^2-y^2)+y+z))
    elif x == "a":
      y = float(input("What is the leg? "))
      z = float(input("What is the area? "))
      g = z/y
      print("Other leg: {}".format(g))
      print("Hypotenuse: {}".format(math.sqrt((y**2)+(g**2))))
      print("Perimeter: {}".format(g+y+(math.sqrt((y**2)+(g**2)))))
    elif x == "quit":
      quit()
    else:
      print("Wrong input. Try again.")
  elif v == "n":
    print("(base*altitude)/2 = area")
    print("leg1+leg2+leg3 = perimeter")
    x = input("What do you know: [l]egs, [a]rea and altitude/base, [p]erimeter and 2 legs ").lower()
    if x == "l":
      y = float(input("What is leg 1? "))
      z = float(input("What is leg 2? "))
      g = float(input("What is leg 3? "))
      print("Perimeter: {}".format(y+z+g))
    elif x == "a":
      y = float(input("What is the altitude or base? "))
      z = float(input("What is the area? "))
      print("Other component: {}".format((2*z)/y))
    elif x == "p":
      y = float(input("What is the perimeter? "))
      g = float(input("What is leg 1? "))
      z = float(input("What is leg 2? "))
      print("Other leg: {}".format(y-g-z))
    elif x == "quit":
      quit()
    else:
      print("Wrong input. Try again.")
  elif v == "quit":
    quit()
  else:
    print("Wrong input. Try again.")
