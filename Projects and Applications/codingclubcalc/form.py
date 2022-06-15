#imports
import math
import other

import sympy

# direct user put to functions
def main():
  x = input("Choose an option: [tr]iangle inequality, [q]uadratic formula, [v]ietas, [f]ibonacci, [sl]ope, \n[sol]ve mxb, [di]stance, [mi]dpoint, [py]hagorean theorum ").lower()
  if x == "tr":
    triangle()
  elif x == "q":
    quadratic()
  elif x == "v":
    vietas()
  elif x == "f":
    fibonacci()
  elif x == "sl":
    slope()
  elif x == "sol":
    solvemxb()
  elif x == "di":
    dist()
  elif x == "mi":
    midpoint()
  elif x == "py":
    pytha()
  elif x == "quit":
    quit()
  else:
    print("Wrong input. Try again.")

# formulas for triangles, quadratics, vietas, fibonacci, slope, slope equations, distance, midpoint, and pythagorean
def triangle():
  print("AB + BC > CA")
  print("BC + CA > AB")
  print("CA + AB > BC")
  x = float(input("What is side 1? "))
  y = float(input("What is side 2? "))
  z = float(input("What is side 3? Enter 0 if unknown "))
  if z == 0:
    print("{} < x < {}".format(abs(x-y)+1, (x+y)-1))
  else:
    if ((x+y)>z) and ((y+z)>x) and ((z+x)>y):
      print("ABC is a triangle.")
    else:
      print("ABC is not a triangle.")

def quadratic():
  print("Note: some answers may be needing further minor simplification.")
  print("y = ax^2+bx+c")
  print("x = (-b±sqrt(b^2-4ac))/2a")
  a = float(input("What is a? "))
  b = float(input("What is b? "))
  c = float(input("What is c? "))
  x = (b**2)-(4*a*c)
  if x > 0:
    print("Root 1: ({}+{}*sqrt({}))/{}".format(-b, other.simprad(x)[0], other.simprad(x)[1], 2*a))
    print("Root 2: ({}-{}*sqrt({}))/{}".format(-b, other.simprad(x)[0], other.simprad(x)[1], 2*a))
  elif x == 0:
    print("Root: {}".format((-b)/(2*a)))
  elif x < 0:
    print("Root 1: ({}+{}i*sqrt({}))/{}".format(-b, other.simprad(x)[0], other.simprad(x)[1], 2*a))
    print("Root 2: ({}-{}i*sqrt({}))/{}".format(-b, other.simprad(x)[0], other.simprad(x)[1], 2*a))
  else:
    print("Error.")

def vietas():
  lst = []
  print("y = a_(n)x^(k)+a_(n-1)x^(k-1) ··· a_(1)x+a_(0)")
  x = int(input("What is the degree of x? "))
  for i in range(x+1):
    lst.append(float(input("Coefficient of x^{}: ".format(x-i))))
  print("Sum of roots: {}".format(-(lst[1]/lst[0])))
  print("Product of roots: {}".format(lst[-1]/lst[0]))

def fibonacci():
  output = [0, 1]
  num = int(input("How many terms? (above 2) "))
  if x in [0, 1, 2]:
    if x == 0:
      print([])
      quit()
    print(output[0:(x)])
    quit()
  for i in range(x-2):
      output.append(int(output[i+1])+int(output[i]))
  print(output)

def slope():
  print("m = (y2-y1)/(x2-x1)")
  x1 = float(input("x1: "))
  x2 = float(input("x2: "))
  y1 = float(input("y1: "))
  y2 = float(input("y2: "))
  if x2-x1 == 0:
    z = "undefined"
    print("Slope: {}".format(z))
    print("Equation: x = {}".format(x1))
  else:
    z = (y2-y1)/(x2-x1)
    print("Slope: {}".format(z))
    print("Equation: y = {}x {}".format(z, other.mxb(z, x1, y1)[0]))

def solvemxb():
  print("0 = mx + b")
  m = float(input("m: "))
  b = float(input("b: "))
  x = sympy.symbols('x')
  print(sympy.solve((m * x) + b))

def dist():
  print("distance = sqrt((x1-x2)^2+(y1-y2)^2)")
  x1 = float(input("x1: "))
  x2 = float(input("x2: "))
  y1 = float(input("y1: "))
  y2 = float(input("y2: "))
  print("Distance: {}".format(math.sqrt((x1-x2)**2+(y1-y2)**2)))

def midpoint():
  print("midpoint = ((x1+x2)/2, (y1+y2)/2)")
  x1 = float(input("x1: "))
  x2 = float(input("x2: "))
  y1 = float(input("y1: "))
  y2 = float(input("y2: "))
  print("Midpoint: ({}, {})".format((x1+x2)/2, (y1+y2)/2))

def pytha():
  print("a^2 + b^2 = c^2")
  x = input("What do you know: [l]egs or [h]ypotenuse? ")
  if x.lower() == "l":
    a = float(input("a: "))
    b = float(input("b: "))
    print("Hypotenuse: {}".format(math.sqrt((a**2)+(b**2))))
  elif x.lower() == "h":
    a = float(input("a: "))
    c = float(input("c: "))
    print("Other leg: {}".format(math.sqrt((c**2)-(a**2))))
