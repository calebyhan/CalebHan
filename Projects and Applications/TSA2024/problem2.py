# problem 2 FHS

n = int(input("Please enter the first positive integer: "))
m = int(input("Please enter the second positive integer: "))

x = 1
k = max(n, m)
for i in range(1, k + 1):
    if m % i == 0 and n % i == 0:
        x = i
    else:
        continue

print("The Greatest Common Factor (GCF) of ", n, " and ", m, " is: ", x, end="")
