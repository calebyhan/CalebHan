# imports
import sys

# function to check if a given credit card number is valid, with or without a checknum
def validate(ccnum, check):
  ccnum = str(ccnum)
  # if checknum is in the credit card number retrieve the checknum
  if check:
    payload = ccnum[0:-1]
  else:
    payload = ccnum
  count = 0
  sum = 0
  # sum every digit backwards, multiply the digit added by 2 if its an even counted digit
  for i in range(len(payload) - 1, -1, -1):
    if count % 2 == 0:
      if len(str(int(payload[i]) * 2)) == 2:
        sum += int(str(int(payload[i]) * 2)[0]) + int(str(int(payload[i]) * 2)[1])
      else:
        sum += int(payload[i]) * 2
    else:
      sum += int(payload[i])
    count += 1
  # final check to see if the credit card number is valid or not
  if check:
    if int(ccnum[-1]) == 0 and 10 - (sum % 10) == 10:
      return True
    elif (10 - (sum % 10)) == int(ccnum[-1]):
      return True
    else:
      return False
  else:
    return (10 - (sum % 10))

# get a popular credit card company's name (visa, american express, discover, mastercard) given the credit card number
def getCCcompany(ccnum):
  ccnum = str(ccnum)
  if int(ccnum[0]) == 4 and len(ccnum) in [13, 16]:
    return "Visa"
  elif int(ccnum[0:2]) in [34, 37] and len(ccnum) == 15:
    return "American Express"
  elif (int(ccnum[0:4]) == 6011 or int(ccnum[0:2]) == 65 or 644 <= int(ccnum[0:3]) <= 649) and len(ccnum) == 16:
    return "Discover"
  elif (51 <= int(ccnum[0:2]) <= 55 or 2221 <= int(ccnum[0:4]) <= 2720) and len(ccnum) == 16:
    return "MasterCard"
  else:
    return "an unrecognizable company."

# main loop
def main():
  while True:
    m_in_cc = input("Enter a credit card number to check: ").strip()
    try:
      ccnum = int(m_in_cc)
      break
    except:
      print("Invalid input.")
  while True:
    m_in_cd = input("Does the credit card number contain the check digit? y/n: ").strip()
    if m_in_cd.lower() == "y":
      m_in_cd = True
      break
    elif m_in_cd.lower == "n":
      m_in_cd = False
      break
    else:
      print("Invalid input.")
  print("\nChecking number...\n")
  if validate(ccnum, m_in_cd):
    print("The credit card is a valid number.")
    print("The credit card is from " + getCCcompany(ccnum))
  else:
    print("The credit card is not a valid number.")
  print()

# run main loop and check if user wants to quit
while True:
  main()
  q = input("Quit? y/n: ")
  if q.lower() == "y":
    break

# testing ==================
test = [4556857035088593,
4532194370989196,
4916142787482772,
4716996653305967,
4446420946774563,
5570903387732195,
5555565726700800, #-
5291028627564659,
5299777232263410, #-
5310938002745169,
6011323958405128,
6011805985729686,
6011208874496410, #-
6011648445464191,
6011282383818158,
373641552245490, #-
371676861728622,
349189395252985,
371341691826019,
376467605622858]

# for i in test:
#   print("TESTING: {}. VALID: {}. FROM: {}".format(i, validate(i, True), getCCcompany(i)))
