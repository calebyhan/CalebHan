'''
USACO 2020 January Contest, Bronze
Problem 1. Word Processor

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=987
'''

with open("word.in", "r") as f:
    n, k = map(int, f.readline().strip().split(" "))
    sentence = list(map(str, f.readline().strip().split(" ")))

def characters(line):
    sum = 0
    for i in line:
        sum += len(i)
    return sum

output = ""
line = []
i = 0
while i < n:
    line.append(sentence[i])
    if characters(line) > k:
        line.pop(-1)
        output += " ".join(line) + "\n"
        line = []
    else:
        i += 1

output += " ".join(line) + "\n"

with open("word.out", "w") as f:
    f.write(output)