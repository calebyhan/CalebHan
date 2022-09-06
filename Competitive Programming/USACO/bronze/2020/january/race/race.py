'''
USACO 2020 January Contest, Bronze
Problem 3. Race

1/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=989
'''

with open("race.in", "r") as f:
    k, n = map(int, f.readline().strip().split(" "))
    x = []
    for i in range(n):
        x.append(int(f.readline().strip()))

def solve(dist, speed, time, end):
    if dist >= k and speed <= end:
        return time
    elif dist >= k and speed > end:
        return 100000000000000000000000000000000
    if speed > 1:
        downspeed = solve(dist + speed - 1, speed - 1, time + 1, end)
        samespeed = solve(dist + speed, speed, time + 1, end)
        upspeed = solve(dist + speed + 1, speed + 1, time + 1, end)
        return min(downspeed, samespeed, upspeed)
    elif speed == 1:
        samespeed = solve(dist + speed, speed, time + 1, end)
        upspeed = solve(dist + speed + 1, speed + 1, time + 1, end)
        return min(samespeed, upspeed)
    return solve(dist + speed + 1, speed + 1, time + 1, end)

output = []
for i in x:
    output.append(solve(0, 0, 0, i))

with open("race.out", "w") as f:
    for i in output:
        f.write(str(i) + "\n")