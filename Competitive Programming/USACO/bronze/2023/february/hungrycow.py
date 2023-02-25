n, t = map(int, input().strip().split(" "))

d = []
b = []

for i in range(n):
    inp = list(map(int, input().strip().split(" ")))
    d.append(inp[0])
    b.append(inp[1])

current = 0
ret = 0
for i in range(t + 1):
    i += 1
    if i - 1 in d:
        current += b[d.index(i - 1)]
    if current > 0:
        current -= 1
        ret += 1

print(ret)