'''
USACO 2019 December Contest, Bronze
Problem 1. Cow Gymnastics

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=963
'''

with open("gymnastics.in", "r") as f:
    k, n = map(int, f.readline().strip().split(" "))
    rankings = []
    for i in range(k):
        rankings.append(list(map(int, f.readline().strip().split(" "))))

pairs = []
output = 0

for i in range(k):
    group = []
    for j in range(n):
        for l in range(n - j - 1):
            group.append([rankings[i][j], rankings[i][l + j + 1]])
    pairs.append(group)

for i in pairs[0]:
    include = True
    for j in range(1, len(pairs)):
        if i not in pairs[j]:
            include = False
    if include:
        output += 1

with open("gymnastics.out", "w") as f:
    f.write(str(output))