# problem 1 FHS

n = input("Enter the total amount of change in dollars and cents: ")

dollars, cents = n.split(".")

print("Minimum change consists of:")

print("Dollars: ", dollars)
print("Quarters: ", int(cents)//25)
print("Dimes: ", (int(cents)%25)//10)
print("Nickels: ", ((int(cents)%25)%10)//5)
print("Pennies: ", ((int(cents)%25)%10)%5)
