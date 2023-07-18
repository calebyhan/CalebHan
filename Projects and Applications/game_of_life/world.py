import tile
import random


class World:
    def __init__(self, x, y, custom_tiles=None):
        self.x = x
        self.y = y

        if custom_tiles:
            self.tiles = custom_tiles
        else:
            self.tiles = [[tile.Tile(i, j, random.choice([True, False])) for j in range(y)] for i in range(x)]

    def clear(self):
        self.tiles = [[tile.Tile(i, j, random.choice([True, False])) for j in range(self.y)] for i in range(self.x)]

    def run(self):
        for i in range(self.x):
            for j in range(self.y):
                neighbors = self.tiles[i][j].get_neighbors()
                count = 0
                for neighbor in neighbors:
                    try:
                        neighbor_tile = self.tiles[neighbor[0]][neighbor[1]]
                    except IndexError:
                        continue
                    if neighbor_tile.state:
                        count += 1

                if self.tiles[i][j].state:
                    if count < 2 or count > 3:
                        self.tiles[i][j].next_state = False
                    else:
                        self.tiles[i][j].next_state = True
                else:
                    if count == 3:
                        self.tiles[i][j].next_state = True

        for i in range(self.x):
            for j in range(self.y):
                self.tiles[i][j].change_state()

    def __str__(self):
        string = ""
        for i in range(self.x):
            for j in range(self.y):
                if self.tiles[i][j].state:
                    string += "X"
                else:
                    string += " "
            string += "\n"
        return string
