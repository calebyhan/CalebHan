import math
import matplotlib.pyplot as plt
import numpy as np

def e_approx(x, n):
    approx = 0
    for i in range(n):
        approx += x ** i / math.factorial(i)
    return approx

def sin_approx(x, n):
    approx = 0
    for i in range(n):
        approx += (-1) ** i * (x ** (2 * i + 1) / math.factorial(2 * i + 1))
    return approx

def cos_approx(x, n):
    approx = 0
    for i in range(n):
        approx += (-1) ** i * (x ** (2 * i) / math.factorial(2 * i))
    return approx

def atan_approx(x, n):
    approx = 0
    for i in range(n):
        approx += (-1) ** i * (x ** (2 * i + 1) / (2 * i + 1))
    return approx

def ln_approx(x, n):
    approx = 0
    for i in range(1, n):
        approx += (-1) ** (i - 1) * ((x - 1) ** (i) / i)
    return approx

def determine_error(function, original, c):
    i = 1
    error = 2
    while error > 1e-16:
        approx = function(c, i)
        exact = original(c)
        error = abs(approx - exact)
        print(f'{i} terms: Approx = {approx}, Exact = {exact}, Error = {error}')
        i += 1

def plot(function, npfunc, xbounds, ybounds):
    x = np.arange(xbounds[0], xbounds[1], 0.1)
    p = lambda x: npfunc(x)

    fig, ax = plt.subplots()
    ax.plot(x, p)

    for i in range(1, 10, 2):
        t = [function(x1,i) for x1 in x]
        ax.plot(x,t)
    ax.set_ylim(ybounds)
    ax.legend(['ln() function', 'Taylor Series - 1 term', 'Taylor Series - 2 terms', 'Taylor Series - 3 terms', 'Taylor Series - 4 terms', 'Taylor Series - 5 terms'])

    plt.show()

determine_error(ln_approx, math.log, 1.5)
plot(ln_approx, np.log, [-2, 2], [-6, 2])
