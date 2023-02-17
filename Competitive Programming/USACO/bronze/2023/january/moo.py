q = int(input().strip())
cases = []
for i in range(q):
    cases.append([*input().strip()])

for case in cases:
    if len(case) < 3:
        print(-1)
    elif "".join(case) == "MOO":
        print(0)
    elif len(case) == 3:
        if case[1] != "O":
            print(-1)
        else:
            if (case[0] == "M" and case[2] == "M") or (case[0] == "O" and case[2] == "O"):
                print(1)
            else:
                print(2)
    else:
        if "MOO" in "".join(case):
            print(len(case) - 3)
        elif "MOM" in "".join(case) or "OOO" in "".join(case):
            print(len(case) - 2)
        elif "OOM" in "".join(case):
            print(len(case) - 1)
        else:
            print(-1)