# problem 4 FHS

num = input("Enter hexadecimal number: ")
sum = 0
for power, digit in enumerate(reversed(num)):
    sum += 16**power * "0123456789ABCDEF".index(digit)
print("In decimal: ", sum)
