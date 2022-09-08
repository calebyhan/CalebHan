'''
USACO 2020 February Contest, Bronze
Problem 2. Mad Scientist

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=1012
'''
with open("breedflip.in", "r") as f:
    n = int(f.readline().strip())
    a = f.readline().strip()
    b = f.readline().strip()

ranges = []
on = False
for i in range(len(b)):
    if b[i] != a[i]:
        if not on:
            on = True
            ranges.append([i, i])
        else:
            ranges[-1][1] = i
    else:
        if on:
            on = False

with open("breedflip.out", "w") as f:
    f.write(str(len(ranges)))