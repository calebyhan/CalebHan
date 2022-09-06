'''
USACO 2020 January Contest, Bronze
Problem 2. Photoshoot

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=988
'''

with open("photo.in", "r") as f:
    n = int(f.readline().strip())
    lst = list(map(int, f.readline().strip().split(" ")))

for i in range(1, n + 1):
    output = []
    output.append(i)
    for j in range(n - 1):
        output.append(lst[j] - output[-1])
    test = list(range(1, n + 1))
    if sorted(output) == test:
        break

with open("photo.out", "w") as f:
    f.write(" ".join(list(map(str, output))))