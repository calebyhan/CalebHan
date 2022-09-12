'''
USACO 2020 December Contest, Bronze
Problem 3. Stuck in a Rut

WIP

http://www.usaco.org/index.php?page=viewproblem2&cpid=1061
'''


import sys

data = sys.stdin.readlines()
n = int(data[0].strip())
cows = []
for i in range(n):
    line = data[i + 1].strip().split(" ")
    cows.append([line[0], list(map(int, line[1:]))])

def inter(cow1, cow2):
    if cow1[0] == cow2[0]:
        return False
    if cow1[0] == "E":
        if cow2[1][1] < cow1[1][1] and cow2[1][0] < cow1[1][0]:
            return False
        elif cow2[1][1] > cow1[1][1] and cow2[1][0] > cow1[1][0]:
            return False
        else:
            if abs(cow1[1][0] - cow2[1][0]) == abs(cow1[1][1] - cow2[1][1]):
                return False
            elif abs(cow1[1][0] - cow2[1][0]) > abs(cow1[1][1] - cow2[1][1]):
                return 1
            else:
                return 0
    else:
        if cow2[1][0] < cow1[1][0] and cow2[1][1] < cow1[1][1]:
            return False
        elif cow2[1][1] > cow1[1][1] and cow2[1][0] > cow1[1][0]:
            return False
        else:
            if abs(cow1[1][0] - cow2[1][0]) == abs(cow1[1][1] - cow2[1][1]):
                return False
            elif abs(cow1[1][0] - cow2[1][0]) < abs(cow1[1][1] - cow2[1][1]):
                return 2
            else:
                return 0

output = ["Infinity"]*n
stopped = [False]*n
for i in range(n):
    least = 100000000000000000000000000000
    for j in range(n):
        if i == j:
            pass
        elif stopped[j]:
            pass
        else:
            result = inter(cows[i], cows[j])
            print(cows[i], cows[j], result)
            if result == False:
                pass
            elif result == 2:
                least = min(least, abs(cows[i][1][1] - cows[j][1][1]))
            elif result == 1:
                least = min(least, abs(cows[i][1][0] - cows[j][1][0]))
    if least != 100000000000000000000000000000:
      output[i] = least

print(output)