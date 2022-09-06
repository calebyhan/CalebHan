'''
USACO 2020 February Contest, Bronze
Problem 1. Triangles

5/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=1011
'''

with open("triangles.in", "r") as f:
    n = int(f.readline().strip())
    points = []
    for i in range(n):
        points.append(list(map(int, f.readline().strip().split(" "))))

def tri(i, j, k):
    if (i[0] == j[0] and i[1] == k[1]) or (i[0] == k[0] and i[1] == j[1]):
        return True
    elif (j[0] == i[0] and j[1] == k[1]) or (j[0] == k[0] and j[1] == i[1]):
        return True
    elif (k[0] == j[0] and k[1] == i[1]) or (k[0] == i[0] and k[1] == j[1]):
        return True
    return False

def check(i, j, k):
    if (i[0] == j[0] and i[1] == k[1]) or (i[0] == k[0] and i[1] == j[1]):
        return abs(j[0] - i[0]) + abs(k[0] - i[0]) * abs(j[1] - i[1]) + abs(k[1] - i[1])
    elif (j[0] == i[0] and j[1] == k[1]) or (j[0] == k[0] and j[1] == i[1]):
        return abs(k[0] - j[0]) + abs(i[0] - j[0]) * abs(k[1] - j[1]) + abs(i[1] - j[1])
    elif (k[0] == j[0] and k[1] == i[1]) or (k[0] == i[0] and k[1] == j[1]):
        return abs(i[0] - k[0]) + abs(j[0] - k[0]) * abs(i[1] - k[1]) + abs(j[1] - k[1])
    return 0

output = 0
for i in range(len(points)):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            output = max(check(points[i], points[j], points[k]), output)

with open("triangles.out", "w") as f:
    f.write(str(output))