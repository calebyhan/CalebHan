import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().strip().split(" "))

cows = []
air = []

for i in range(n):
    cows.append(list(map(int, input().strip().split(" "))))

for i in range(m):
    air.append(list(map(int, input().strip().split(" "))))

# print(cows)

air = sorted(air, key=lambda x: x[3])

# print(air)

def solve(ranges, airs, price, which, i):
    if i == len(air):
        return [price, which]
    # print(price, which)
    for i in range(len(cows)):
        for j in range(len(ranges)):
            if ranges[j][0] >= cows[i][0] and ranges[j][0] <= cows[i][1] and ranges[j][1] >= cows[i][2]:
                return [price, which]                    
            else:
                pass
    
    ranges1 = list(ranges)
    airs1 = list(airs)
    price1 = price
    which1 = list(which)

    for i in range(airs1[0][0], airs1[0][1] + 1):
        found = False
        for j in ranges1:
            if i == j[0]:
                j[1] += airs1[0][3]
                found = True
        if not found:
            ranges1.append([i, airs1[0][3]])
        found = False
    which1.append(air.index(airs1[0]))
    price1 += airs1[0][3]
    airs1 = airs1[1:]
    print(ranges1, airs1, price1, which1)
    return min(price, solve(ranges1, airs1, price1, which1, i + 1)[0]), [which, which1]

print(solve([], list(air), 0, [], 0))