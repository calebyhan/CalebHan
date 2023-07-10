import maze

# example maze
ex = '''000000000000000
oxx0000xxx00000
00x0xxxx0xxxxx0
00xxx0000000xx0
0000000000000o0'''

m = maze.Maze(ex)

# prints solution
print(m.solution)

# prints maze
print(m)
