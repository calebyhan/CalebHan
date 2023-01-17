import random

def check_first(board):
    '''
    Check if it is the first move
    '''
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                return False
    return True

def check_behind(board, bot):
    '''
    Check if the user went first
    '''
    
    turns = [0, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == bot:
                turns[0] += 1
            elif board[i][j] == list(set([1, 0]) - set([bot]))[0]:
                turns[1] += 1
    if turns[1] > turns[0]:
        return True
    return False

def check_iter(board, bot):
    '''
    Check how many turns in the game is
    '''
    
    ret_1 = 0
    ret_2 = 0
    player = 1
    if bot == 1:
        player = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == bot:
                ret_1 += 1
            elif board[i][j] == player:
                ret_2 += 1
    return max(ret_1, ret_2)

def ret_empty(board):
    '''
    Returns the empty positions
    '''
    
    ret_lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == -1:
                ret_lst.append([i, j])
    ret = []
    for i in ret_lst:
        ret.append(i[0] * 3 + i[1])
    return ret

def check_win_bot(board, bot):
    '''
    Check if the bot can win
    '''
    
    cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    bot_cases = []
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == bot:
                bot_cases.append(j * 3 + i)
    for i in range(len(cases)):
        if len(list(set(cases[i]) & set(bot_cases))) == 2:
            x = list(set(cases[i]) - set(bot_cases))[0] // 3
            y = list(set(cases[i]) - set(bot_cases))[0] % 3
            if board[x][y] == -1:
                return [True, list(set(cases[i]) - set(bot_cases))[0]]
    return [False]

def check_win_player(board, bot):
    '''
    Check if the player can win
    '''
    
    cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    if bot == 1:
        player = 0
    else:
        player = 1
    player_cases = []
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == player:
                player_cases.append(j * 3 + i)
    for i in range(len(cases)):
        if len(list(set(cases[i]) & set(player_cases))) == 2:
            x = list(set(cases[i]) - set(player_cases))[0] // 3
            y = list(set(cases[i]) - set(player_cases))[0] % 3
            if board[x][y] == -1:
                return [True, list(set(cases[i]) - set(player_cases))[0]]
    return [False]

def refit(board, bot):
    '''
    Refits the board from X/O to 1/0
    '''

    new_board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    if bot == "X":
        bots = 1
    else:
        bots = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == bot:
                new_board[i][j] = bots
            elif board[i][j] != -1:
                new_board[i][j] = list(set([0, 1]) - set([bots]))[0]
    return new_board

def solve_best(board, bot):
    '''
    Puts all functions together to find best move
    '''
    
    if check_behind(board, bot):
        if check_iter(board, bot) == 1:
            if board[1][1] == -1:
                return 4
            else:
                return random.choice([0, 2, 6, 8])
        else:
            return random.choice(ret_empty(board))
    else:
        if check_iter(board, bot) == 1:
            if board[0][0] == bot:
                if board[0][1] != -1:
                    return random.choice([6, 8])
                if board[1][0] != -1:
                    return random.choice([2, 8])
                return random.choice([2, 6, 8])
            if board[0][2] == bot:
                if board[0][1] != -1:
                    return random.choice([6, 8])
                if board[1][2] != -1:
                    return random.choice([0, 6])
                return random.choice([0, 6, 8])
            if board[2][0] == bot:
                if board[1][0] != -1:
                    return random.choice([2, 8])
                if board[2][1] != -1:
                    return random.choice([0, 2])
                return random.choice([0, 2, 8])
            else:
                if board[2][1] != -1:
                    return random.choice([0, 2])
                if board[1][2] != -1:
                    return random.choice([0, 6])
                return random.choice([0, 2, 6])
        elif check_iter(board, bot) == 2:
            if board[0][0] != -1 and board[0][2] != -1 and board[2][0] != -1:
                return 8
            if board[0][0] != -1 and board[0][2] != -1 and board[2][2] != -1:
                return 6
            if board[0][0] != -1 and board[2][2] != -1 and board[2][0] != -1:
                return 2
            if board[2][2] != -1 and board[0][2] != -1 and board[2][0] != -1:
                return 0
            if board[1][1] == -1:
                return 4
        elif check_iter(board, bot) == 3 or check_iter(board, bot):
            return random.choice(ret_empty(board))

def move(board, bot):
    '''
    If not a guaranteed win, check the best move
    '''
    
    board = refit(board, bot)
    if bot == "X":
        bot = 1
    else:
        bot = 0
    if check_first(board):
        return random.choice([0, 2, 6, 8])
    bot_win = check_win_bot(board, bot)
    if bot_win[0]:
        return bot_win[1]
    player_win = check_win_player(board, bot)
    if player_win[0]:
        return player_win[1]
    return solve_best(board, bot)