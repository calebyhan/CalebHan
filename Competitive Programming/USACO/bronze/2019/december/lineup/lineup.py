'''
USACO 2019 December Contest, Bronze
Problem 3. Livestock Lineup

4/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=965
'''

with open("lineup.in", "r") as f:
    n = int(f.readline().strip())
    constraints = []
    for i in range(n):
        line = f.readline().strip().split(" ")
        constraints.append([line[0], line[-1]])

cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
output = []

counter = 0
nexttoB = []

for i in constraints:
    if "Beatrice" in i:
        counter += 1
        remove = list(i)
        remove.remove("Beatrice")
        nexttoB.append(remove[0])

if counter == 1:
    output.append("Beatrice")
    output.append(nexttoB[0])
    cows.remove("Beatrice")
    cows.remove(nexttoB[0])
elif counter == 2:
    output.append(sorted(nexttoB)[0])
    cows.remove(nexttoB[0])
    output.append("Beatrice")
    cows.remove("Beatrice")
    output.append(sorted(nexttoB)[1])
    cows.remove(nexttoB[1])

def check(cow):
    where = []
    for i in constraints:
        if cow in i:
            remove = list(i)
            remove.remove(cow)
            where.append(remove[0])
    if len(where) == 0:
        return False
    else:
        return where

while True:
    if len(output) == 8:
        break
    checked = check(cows[0])
    print(cows, output, checked)
    if checked == False:
        output.append(cows[0])
        cows.remove(cows[0])
    elif len(checked) == 1:
        output.append(cows[0])
        output.append(checked[0])
        cows.remove(cows[0])
        cows.remove(checked[0])
    else:
        if cows.index(sorted(checked)[0]) == 1:
            output.append(sorted(checked)[0])
            output.append(cows[0])
            output.append(sorted(checked)[1])
            cows.remove(sorted(checked)[0])
            cows.remove(cows[0])
            cows.remove(sorted(checked)[1])
        else:
            removed = []
            for i in range(1, cows.index(sorted(checked)[0])):
                output.append(cows[i])
                removed.append(cows[i])
            for i in removed:
                cows.remove(i)

with open("lineup.out", "w") as f:
    for i in output:
        f.write(i + "\n")