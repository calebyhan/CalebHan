'''
USACO 2019 February Contest, Bronze
Problem 1. Sleepy Cow Herding

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=915
'''

with open("herding.in", "r") as f:
    b, e, m = map(int, f.readline().strip().split(" "))

minimum = 0
maximum = 0

if m - e == 1 and e - b == 1:
    minimum = 0
elif m - e == 2 or e - b == 2:
    minimum = 1
else:
    minimum = 2

maximum = max(m - e, e - b) - 1

with open("herding.out", "w") as f:
    f.write(str(minimum) + "\n" + str(maximum))