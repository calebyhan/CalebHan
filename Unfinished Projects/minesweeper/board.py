import pygame
import random
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)


class Board:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.square_size = 50
        self.width = self.x * self.square_size
        self.height = self.y * self.square_size
        self.board = pygame.display.set_mode((self.width, self.height))
        self.squares = []

        self.flags = [[0 for j in range(self.y)] for i in range(self.x)]
        for i in range(self.n):
            while True:
                row = random.randint(0, x - 1)
                col = random.randint(0, y - 1)
                if self.flags[row][col] == -1:
                    continue
                self.flags[row][col] = -1
                break

        self._fill()

        for i in self.flags:
            print(i)

    def _draw(self):
        for x in range(self.width // self.square_size):
            row = []
            for y in range(self.height // self.square_size):
                rect = pygame.Rect(x * self.square_size, y * self.square_size, self.square_size, self.square_size)
                row.append(rect)
            self.squares.append(row)

        self.board.fill(WHITE)
        for row in self.squares:
            for square in row:
                pygame.draw.rect(self.board, GRAY, square, 1)

        pygame.display.update()

    def _fill(self):
        for r in range(self.x):
            for c in range(self.y):
                count = 0
                if self.flags[r][c] == -1:
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.x > r + i >= 0 and self.y > c + j >= 0:
                            if self.flags[r + i][c + j] == -1:
                                count += 1
                self.flags[r][c] = count

    def _clear0(self, x, y):
        if self.flags[x][y] == 0:
            self.flags[x][y] = -2
            for row in self.squares:
                for square in row:
                    if square.collidepoint((x * 50, y * 50)):
                        pygame.draw.rect(self.board, GRAY, square)
                        pygame.display.update(square)
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                if self.x > x + i >= 0 and self.y > y + j >= 0:
                                    self._clear0(x + i, y + j)
                                else:
                                    return

    def _failed(self):
        menu_width = 300
        menu_height = 200
        font = pygame.font.SysFont(None, 50)
        message = font.render("Game Over", True, (255, 0, 0))
        message_rect = message.get_rect(center=(self.width // 2, self.height // 2))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.board.blit(message, message_rect)
            pygame.draw.rect(self.board, (0, 0, 0), ((self.width - menu_width) // 2, (self.height - menu_height) // 2, menu_width, menu_height), 3)

            pygame.display.update()

    def run(self):
        self._draw()
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not keys[pygame.K_LCTRL]:
                    pos = pygame.mouse.get_pos()
                    for row in self.squares:
                        for square in row:
                            if square.collidepoint(pos):
                                if self.flags[square.topleft[1] // 50][square.topleft[0] // 50] == -1:
                                    self._failed()
                                else:
                                    if self.flags[square.topleft[1] // 50][square.topleft[0] // 50] != 0:
                                        font = pygame.font.SysFont(None, 50)
                                        message = font.render(str(self.flags[square.topleft[1] // 50][square.topleft[0] // 50]), True, (255, 0, 0))
                                        message_rect = message.get_rect(center=(square.center[0], square.center[1]))
                                        self.board.blit(message, message_rect)
                                        pygame.display.update()
                                    else:
                                        self._clear0(square.topleft[0] // 50, square.topleft[1] // 50)

                elif event.type == pygame.MOUSEBUTTONDOWN and keys[pygame.K_LCTRL]:
                    pos = pygame.mouse.get_pos()
                    for row in self.squares:
                        for square in row:
                            if square.collidepoint(pos):
                                pygame.draw.rect(self.board, RED, square)
                                pygame.display.update(square)
