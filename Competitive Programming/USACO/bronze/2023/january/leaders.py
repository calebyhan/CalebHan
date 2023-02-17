n = int(input().strip())
s = input().strip()
e = list(map(int, input().strip().split(" ")))

lst = []

for i in range(n):
    lst.append(list(range(i, e[i])))

def check_cows(i):
    breed = s[i]
    num = s.count(breed)
    for j in lst[i]:
        if s[j] == breed:
            num -= 1
    if num == 0:
        return True
    return False

def check_leader(i):
    for j in lst[i]:
        if check_cows(j):
            return [True, j]
    return [False, 0]

def stop(i):
    new_str = s[:i]
    if "G" in new_str and "H" in new_str:
        return True
    return False

ret = [0, 0]
for i in range(n):
    if stop(i):
        break
    if s[i] == "G":
        if check_cows(i) or check_leader(i)[0]:
            ret[0] += 1
    else:
        if check_cows(i) or check_leader(i)[0]:
            ret[1] += 1

print(ret[0]*ret[1])