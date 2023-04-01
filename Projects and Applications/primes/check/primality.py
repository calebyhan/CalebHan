import math
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
 
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import generate.sieves

def aks(n):
    if n==2:return True
    c=1
    for i in range(n//2+1):
        c=c*(n-i)//(i+1)
        if c%n:return False
    return True

df = []

for i in range(10):
    num = generate.sieves.sieve_of_atkin(10 ** i)[-1]

    print(num)

    start = time.time()

    aks(num)

    end = time.time()

    df.append(end - start)
    print("DONE: " + str(i + 1) + "/10")

print(df)

small_value = 1e-10
df = np.log10([x + small_value for x in df])

plt.plot(list(range(10)), df)


plt.xlabel("Power of 10")
plt.ylabel("Time for execute")
plt.title("Execute time for AKS Primality test")
plt.show()

print(df)