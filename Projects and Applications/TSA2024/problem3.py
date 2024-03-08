# problem 3 FHS

n = int(input())
max = [None, 0, 0]
PI = 3.14159
for i in range(n):
    inputs = input().split()
    if inputs[0] == "cube":
        a = float(inputs[1])**3
        if max[2] < a:
            max = [i + 1, "cube", a]
    elif inputs[0] == "cylinder":
        a = float(inputs[1])** 2 * PI * float(inputs[2])
        if max[2] < a:
            max = [i + 1, "cylinder", a]
    elif inputs[0] == "cone":
        a = float(inputs[1]) ** 2 * PI / 3 * float(inputs[2])
        if max[2] < a:
            max = [i + 1, "cone", a]
    else:
        a = float(inputs[1]) ** 3 * 4 / 3 * PI
        if max[2] < a:
            max = [i + 1, "sphere", a]

print(*max[:2], f"{max[2]: .3f}")
