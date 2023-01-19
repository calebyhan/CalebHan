import sys

data = sys.stdin.readlines()
n = int(data[0].strip())
c = list(map(int, data[1].strip().split(" ")))

if n == 1:
    print(c[0], c[0])
else:
    c.sort()

    max = (c[0], c[0])
    same = 0
    
    for i in range(n):
        if c[i] == c[i - 1]:
            same += 1
        else:
            same = 0
        if (n-i+same)*c[i] > max[0]:
            max = ((n-1+same)*c[i], c[i])

    print("{} {}".format(max[0], max[1]))