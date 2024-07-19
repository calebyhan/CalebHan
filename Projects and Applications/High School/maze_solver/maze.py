class Maze:
    def __init__(self, raw, exits="o", path='x', walls="0", enter=None):
        self.exits = exits
        self.path = path
        self.walls = walls
        self.raw = raw

        self.processed = None
        self.enter = enter if enter is not None else None

        self.process_input(self.raw)

        self.solution = self.solve_maze(self.enter[0], self.enter[1])

    def process_input(self, raw):
        self.processed = raw.split('\n')
        self.processed = [list(line) for line in self.processed]

        if self.enter is None:
            for y, line in enumerate(self.processed):
                for x, char in enumerate(line):
                    if char == self.exits:
                        self.enter = (x, y)
                        break
                else:
                    continue
                break

    def check_valid(self, x, y):
        if x < 0 or y < 0:
            return False
        try:
            if self.processed[y][x] == self.walls:
                return False
            else:
                return True
        except IndexError:
            return False

    def solve_maze(self, x, y):
        stack = [(x, y, [])]
        while stack:
            x, y, path = stack.pop()
            if self.processed[y][x] == self.exits and (x, y) != self.enter:
                path.append((x, y))
                return path
            elif self.processed[y][x] == self.walls:
                continue
            else:
                path.append((x, y))
                self.processed[y][x] = self.walls
                if self.check_valid(x + 1, y):
                    stack.append((x + 1, y, path.copy()))
                if self.check_valid(x, y + 1):
                    stack.append((x, y + 1, path.copy()))
                if self.check_valid(x - 1, y):
                    stack.append((x - 1, y, path.copy()))
                if self.check_valid(x, y - 1):
                    stack.append((x, y - 1, path.copy()))
        return None

    def __str__(self):
        return self.raw
