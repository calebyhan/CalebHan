'''
USACO 2020 December Contest, Bronze
Problem 2. Daisy Chains

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=1060
'''

import sys

data = sys.stdin.readlines()
n = int(data[0].strip())
p = list(map(int, data[1].strip().split(" ")))

output = 0
for i in range(n):
    for j in range(i, n):
        petals = 0
        for k in range(i, j + 1):
            petals += p[k]
        av = False
        for k in range(i, j + 1):
            if p[k] * (j - i + 1) == petals:
                av = True
        if av:
            output += 1
print(output)