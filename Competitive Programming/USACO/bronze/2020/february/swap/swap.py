'''
USACO 2020 February Contest, Bronze
Problem 3. Swapity Swap

6/13

http://www.usaco.org/index.php?page=viewproblem2&cpid=1013
'''

with open("swap.in", "r") as f:
    n, k = map(int, f.readline().strip().split(" "))
    a = list(map(int, f.readline().strip().split(" ")))
    b = list(map(int, f.readline().strip().split(" ")))

output = list(range(1, n + 1))
for i in range(k):
    if a[0] == 1:
        output = output[a[1] - 1::-1] + output[a[1]:]
    else:
        output = output[:a[0] - 1] + output[a[1] - 1:a[0] - 2:-1] + output[a[1]:]
    if b[0] == 1:
        output = output[b[1] - 1::-1] + output[b[1]:]
    else:
        output = output[:b[0] - 1] + output[b[1] - 1:b[0] - 2:-1] + output[b[1]:]

with open("swap.out", "w") as f:
    for i in output:
        f.write(str(i) + "\n")