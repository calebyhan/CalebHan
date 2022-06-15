# imports
import math
import sympy

# arithmatic on lists
def rec(lst, func):
  answer = 0
  if func == "+":
    for num in lst:
      answer += num
  elif func == "-":
    answer = lst[0]
    lst.remove(lst[0])
    for num in lst:
      answer = answer - num
  elif func == "*":
    answer = lst[0]
    lst.remove(lst[0])
    for num in lst:
      answer = answer * num
  elif func == "/":
    answer = lst[0]
    lst.remove(lst[0])
    for num in lst:
      answer = answer / num
  elif func == "!":
    answer = 1
    for i in range(int(lst[0])):
      answer = answer * (i + 1)
  return answer

# simplifying radicals
def simprad(n):
  nabs = abs(n)
  trial = math.floor(nabs**0.5)
  coeff = 1
  while trial > 1:
    if n % (trial**2) == 0:
      coeff = trial
      trial = 0
    trial -= 1
  remainder = nabs // coeff**2
  return [coeff, remainder]

# solve y=mx+b for b
def mxb(m, x, y):
  x = sympy.symbols('b')
  return sympy.solve((m * x) + b - y)
