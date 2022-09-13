'''
USACO 2019 February Contest, Bronze
Problem 2. The Great Revegetation

WIP

http://www.usaco.org/index.php?page=viewproblem2&cpid=916
'''

with open("revegetate.in", "r") as f:
    n, m = map(int, f.readline().strip().split(" "))
    cows = []
    for i in range(m):
        cows.append(sorted(list(map(int, f.readline().strip().split(" ")))))

print(cows)