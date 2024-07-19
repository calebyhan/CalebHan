import math
import random

p = 61
q = 89


def find_keys(p, q):
    n = p * q

    l = math.lcm(p - 1, q - 1)

    while True:
        e = random.randint(2, int(l ** (1/2)))
        if math.gcd(e, l) == 1:
            break

    d = pow(e, -1, l)

    return d, e, n


def encrypt(message, e, n):
    return (message ** e) % n


def decrypt(c, d, n):
    return (c ** d) % n


d, e, n = find_keys(p, q)

c = encrypt(85, e, n)

print(decrypt(c, d, n))
