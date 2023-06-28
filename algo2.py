import numpy as np
import algo

ai = 1
pers = 2
def best_move(state):
    inf = float('inf')
    best_score = -inf
    score = None
    move = None
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                state[i][j] = ai
                score = minimax(state, 0, False)
                state[i][j] = 0
                if (score > best_score):
                    best_score = score
                    move = (i,j)
    state[move[0]][move[1]] = ai
def minimax(state, depth, isMaximazing):
    win_ai = algo.check_win(state)
    win_per = algo.check_lose(state)
    win_tie = algo.check_tie(state)
    if win_ai:
        return 1
    elif win_per:
        return -1
    elif win_tie:
        return 0

    if isMaximazing:
        inf = float('inf')
        best_score = -inf
        score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax(state, depth+1, False)
                    state[i][j] = 0
                    best_score = max(score,best_score)
        return best_score
    else:
        inf = float('inf')
        best_score = inf
        score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = pers
                    score = minimax(state, depth + 1, True)
                    state[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

if __name__ == '__main__':
    matr = np.array([[1,0,0],[2,0,1],[1,0,2]])

    matr_ex = np.array([[1,2,1],[0,2,0],[2,0,0]])
    best_move(matr_ex)

    matr_zero = np.zeros_like(matr)
    while True:
        if algo.check_win(matr_zero) or algo.check_lose(matr_zero) or algo.check_tie(matr_zero):
            break
        inp = input('i,j')
        matr_zero[int(inp[0])][int(inp[-1])] = 2
        print(matr_zero)
        print()
        best_move(matr_zero)
        print(matr_zero)
        print()



