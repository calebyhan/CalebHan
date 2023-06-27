import matplotlib.pyplot as plt
import random
import numpy as np

# number of simulation iterations
n = 100000

# setting up the random variables
x_p = [0.4, 0.3, 0.15, 0.10, 0.05]
x_n = [1, 2, 3, 4, 5]
y_p = [0.1, 0.2, 0.4, 0.2, 0.1]
y_n = [1, 2, 3, 4, 5]

set_len = len(x_p)

# showing the probabilistic distributions
plt.bar(np.arange(0, 1, (1 / set_len)), x_p, width=(1 / set_len), align="edge")
plt.show()

plt.bar(np.arange(0, 1, (1 / set_len)), y_p, width=(1 / set_len), align="edge")
plt.show()

# simulating the convolution
output = [0]*(set_len * 2)
for i in range(n):
    output[random.choices(x_n, x_p)[0] + random.choices(y_n, y_p)[0] - 1] += 1

# showing the output
plt.bar(list(range(2, (set_len * 2) + 1)), output[1:])
plt.show()
