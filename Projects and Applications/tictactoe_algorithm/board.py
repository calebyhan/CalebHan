import random
import bot

class Board:
    '''
    Board key:
        -1: empty
        0: O
        1: X
    '''

    def __init__(self):
        '''
        Sets up the board with an empty board and variables
        '''

        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turn = random.choice(["X", "O"])
        self.assign = random.choice(["You", "Bot"])
    
    def __str__(self):
        '''
        Prints the board
        '''
        
        board = []
        for i in self.board:
            board.append(" {} | {} | {} \n".format(i[0], i[1], i[2]))
            board.append("-----------\n")
        board = "".join(board[:-1])
        board = board.replace("-1", " ")
        return board

    def switch(self):
        '''
        Switch turn
        '''
        
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        if self.assign == "You":
            self.assign = "Bot"
        else:
            self.assign = "You"

    def check_end(self):
        '''
        Check if the game is drawed or if one person has won.
        '''

        cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        if self.turn == "X":
            player = "O"
        else:
            player = "X"
        checking_0 = []
        checking_1 = []
        for j in range(len(self.board)):
            for i in range(len(self.board[j])):
                if self.board[j][i] == player:
                    checking_0.append(j * 3 + i)
                if self.board[j][i] == self.turn:
                    checking_1.append(j * 3 + i)
        for i in range(len(cases)):
            if len(list(set(cases[i]) & set(checking_0))) == 3:
                return 0
            if len(list(set(cases[i]) & set(checking_1))) == 3:
                return -1
        draw = True
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == -1:
                    draw = False
        if draw:
            return -1

    def place(self, pos):
        '''
        Places a piece at a position
        '''

        x = pos // 3
        y = pos % 3
        if self.board[x][y] == -1:
            self.board[x][y] = self.turn
        else:
            return False
        self.switch()

    def botMove(self):
        '''
        Calls on algorithm to get a move
        '''

        a = bot.move(self.board, self.turn)
        self.place(a)
