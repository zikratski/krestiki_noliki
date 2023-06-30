import numpy as np
import algo
#sum_score = 0
ai = 1
pers = 2
def best_move(state, mode='extreme'):
    inf = float('inf')
    score = None
    move = None
    if mode == 'extreme':
        best_score = -inf
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax(state, 0, False)
                    state[i][j] = 0
                    if score > 0:
                        return (i,j)
                    if score > best_score:
                        best_score = score
                        move = (i,j)
    if mode == 'easy':
        best_score = inf
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax_lose(state, 0, True)
                    state[i][j] = 0
                    if score < 0:
                        return (i,j)
                    if score < best_score:
                        best_score = score
                        move = (i,j)
    if mode == 'random':
        move = algo.random_sol(state)
    return move
def minimax(state, depth, isMaximazing):
    # if depth == 1:
    win_ai = algo.check_win(state)
    win_per = algo.check_lose(state)
    win_tie = algo.check_tie(state)
    #global sum_score
    if win_ai:
        #sum_score +=1
        return 1
    elif win_per:
        #sum_score += 1
        return -1
    elif win_tie:
        #sum_score += 1
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
                    if score > 0:
                        return score
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
                    if score < 0:
                        return score
                    best_score = min(score, best_score)
        return best_score

def minimax_lose(state, depth, isMaximazing):
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
        best_score = inf
        score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = pers
                    score = minimax_lose(state, depth+1, False)
                    state[i][j] = 0
                    if score < 0:
                        return score
                    best_score = min(score,best_score)
        return best_score
    else:
        inf = float('inf')
        best_score = inf
        score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax_lose(state, depth + 1, True)
                    state[i][j] = 0
                    if score < 0:
                        return score
                    best_score = min(score, best_score)
        return best_score

def get_stats(state, move='ai'):
    chances = {'ai': 0, 'person': 0, 'tie': 0}
    get_all_possibles(state, chances, move=move)
    chances_sum = sum(chances.values())
    print(f'sum:{chances_sum}')
    for key, value in chances.items():
        chances[key] = round((100 / chances_sum) * value, 2)
    print(f"chances in proc: \n"
          f"ai: {chances['ai']}%\n"
          f"person: {chances['person']}%\n"
          f"tie: {chances['tie']}%\n")

def get_all_possibles(state, chances, move):
    win_ai = algo.check_win(state)
    win_per = algo.check_lose(state)
    win_tie = algo.check_tie(state)
    if win_ai:
        chances['ai'] += 1
        return
    elif win_per:
        chances['person'] += 1
        return
    elif win_tie:
        chances['tie'] += 1
        return

    if move == 'ai':
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    get_all_possibles(state, chances, move='person')
                    state[i][j] = 0
        return
    else:
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = pers
                    get_all_possibles(state, chances, move='ai')
                    state[i][j] = 0
        return

if __name__ == '__main__':
    matr = np.array([[1,0,0],[2,0,1],[1,0,2]])
    #
    # # matr_ex = np.array([[2,1,2],[2,1,0],[1,0,0]])
    # # bestmove = best_move(matr_ex)
    # # print(bestmove)
    matr_zero = np.zeros_like(matr)
    print(best_move(matr_zero))




