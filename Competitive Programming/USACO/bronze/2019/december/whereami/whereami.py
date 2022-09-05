'''
USACO 2019 December Contest, Bronze
Problem 2. Where Am I?

10/10

http://www.usaco.org/index.php?page=viewproblem2&cpid=964
'''

import re

with open("whereami.in", "r") as f:
    n = int(f.readline().strip())
    mailboxes = [*f.readline().strip()]

for i in range(n):
    j = 0
    output = True
    while j + i + 1 <= len(mailboxes):
        match = "".join(mailboxes[j:j + i + 1])
        for k in range(n - i):
            count = start = 0
            while True:
                if count > 1:
                    break
                start = "".join(mailboxes).find("".join(mailboxes[k:k + i + 1]), start) + 1
                if start > 0:
                    count += 1
                else:
                    break
            if count > 1:
                output = False
        j += 1
    if output:
        output = i + 1
        break

with open("whereami.out", "w") as f:
    f.write(str(output))