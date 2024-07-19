class Tile:
    def __init__(self, x, y, state=False):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = False

    def get_neighbors(self):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                neighbors.append((self.x + i, self.y + j))
        return neighbors

    def change_state(self):
        self.state = self.next_state
