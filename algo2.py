import numpy as np
import algo

ai = 1
pers = 2
def best_move(state):
    chances = {'ai':0,'person':0,'tie':0}
    minimax(state, 0, True, chances)
    chances_sum = sum(chances.values())
    for key, value in chances.items():
        chances[key] = round((100 / chances_sum) * value, 2)
    print(f"chances in proc: {chances}")
    inf = float('inf')
    best_score = -inf
    score = None
    move = None
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                state[i][j] = ai
                score = minimax(state, 0, False, chances)
                state[i][j] = 0
                if (score > best_score):
                    best_score = score
                    move = (i,j)
    #state[move[0]][move[1]] = ai
    return move
def minimax(state, depth, isMaximazing, chances):
    win_ai = algo.check_win(state)
    win_per = algo.check_lose(state)
    win_tie = algo.check_tie(state)
    if win_ai:
        chances['ai'] += 1
        return 1
    elif win_per:
        chances['person'] += 1
        return -1
    elif win_tie:
        chances['tie'] += 1
        return 0

    if isMaximazing:
        inf = float('inf')
        best_score = -inf
        score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax(state, depth+1, False, chances)
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
                    score = minimax(state, depth + 1, True, chances)
                    state[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

if __name__ == '__main__':
    matr = np.array([[1,0,0],[2,0,1],[1,0,2]])

    matr_ex = np.array([[2,1,2],[2,1,0],[1,0,0]])
    bestmove = best_move(matr_ex)
    print(bestmove)
    # matr_zero = np.zeros_like(matr)
    # bestmove = best_move(matr_zero)
    # print(bestmove)

    # chances = {'ai': 0, 'person': 12, 'tie': 34}
    # chances_sum = sum(chances.values())
    # for key, value in chances.items():
    #     chances[key] = round((100 / chances_sum) * value, 2)
    # print(f"chances in proc: {chances}")

    # while True:
    #     if algo.check_win(matr_zero) or algo.check_lose(matr_zero) or algo.check_tie(matr_zero):
    #         break
    #     inp = input('i,j')
    #     matr_zero[int(inp[0])][int(inp[-1])] = 2
    #     print(matr_zero)
    #     print()
    #     best_move(matr_zero)
    #     print(matr_zero)
    #     print()



