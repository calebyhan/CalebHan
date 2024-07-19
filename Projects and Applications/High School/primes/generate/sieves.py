import math
import time
import matplotlib.pyplot as plt
import numpy as np

def sieve_of_eratosthenes(n):
    nums = [False, False]
    nums += [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i]:
            j = 0
            while (i ** 2) + (j * i) <= n:
                nums[(i ** 2) + (j * i)] = False
                j += 1
    return nums


def sieve_of_sundaram(n):
    if n < 3:
        if n < 2:
            return 0
        else:
            return 1    
    k = (n - 3) // 2 + 1

    nums = [False, False]
    nums += [True] * (n - 1)

    for i in range((int(math.sqrt(n)) - 3) // 2 + 1):
            p = 2 * i + 3
            s = (p * p - 3) // 2

            for j in range(s, k, p):
                nums[j] = False
    return nums


def sieve_of_atkin(n):
    P = [2,3]
    r = range(1,int(math.sqrt(n))+1)
    sieve=[False] * (n + 1)
    for x in r:
        for y in r:
            i = x * x
            j = y * y
            k = 3 * i
            l = 4 * i + j
            if l <= n and (l % 12 == 1 or l % 12 == 5):
                sieve[l] = not sieve[l]
            l = k + j
            if l <= n and n % 12 == 7 :
                sieve[l] = not sieve[l]
            l = k - j
            if x > y and l <= n and l % 12 == 11:
                sieve[l] = not sieve[l]
    for x in range(5, int(math.sqrt(n))):
        if sieve[x]:
            i = x * x
            for y in range(i, n + 1, i):
                sieve[y] = False
    for p in range(5,n):
        if sieve[p]:
            P.append(p)
    return P


# df = []

# for i in range(10):
#     start = time.time()

#     sieve_of_sundaram(10 ** i)

#     end = time.time()

#     df.append(end - start)
#     print("DONE: " + str(i + 1) + "/10")

# print(df)

# small_value = 1e-10
# df = np.log10([x + small_value for x in df])

# plt.plot(list(range(10)), df)

# plt.xlabel("Power of 10")
# plt.ylabel("Time for execute")
# plt.title("Execute time for Sieve of Atkin")
# plt.show()

# print(df)