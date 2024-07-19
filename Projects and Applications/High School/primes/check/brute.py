import math
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
 
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import generate.sieves

def brute(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

df = []

for i in range(10):
    num = generate.sieves.sieve_of_atkin(10 ** i)[-1]

    start = time.time()

    brute(num)

    end = time.time()

    df.append(end - start)
    print("DONE: " + str(i + 1) + "/10")

print(df)

small_value = 1e-10
df = np.log10([x + small_value for x in df])

plt.plot(list(range(10)), df)


plt.xlabel("Power of 10")
plt.ylabel("Time for execute")
plt.title("Execute time for Brute Method")
plt.show()

print(df)