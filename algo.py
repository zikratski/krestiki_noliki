import random
import numpy as np

# проверка матрицы на выигрыш
def check_win(state, ai=1):
    for column in state:
        if np.array_equal(column, np.array([ai,ai,ai])):
            return True
    for col_index in range(state.shape[1]):
        column = state[:, col_index]
        if np.array_equal(column, np.array([ai,ai,ai])):
            return True
    if state[0][0] == state[1][1] == state[2][2] == ai:
        return True
    elif state[0][2] == state[1][1] == state[2][0] == ai:
        return True
    else:
        return False

# проверка матрицы на проигрыш
def check_lose(state,pers=2):
    for column in state:
        if np.array_equal(column, np.array([pers,pers,pers])):
            return True
    for col_index in range(state.shape[1]):
        column = state[:, col_index]
        if np.array_equal(column, np.array([pers,pers,pers])):
            return True
    if state[0][0] == state[1][1] == state[2][2] == pers:
        return True
    elif state[0][2] == state[1][1] == state[2][0] == pers:
        return True
    else:
        return False

# проверка матрицы на ничью
def check_tie(state,ai=1,pers=2):
    if 0 not in state and not check_lose(state,pers) and not check_win(state,ai):
        return True
    else:
        return False

# выдает лучший ход на данный момент в зависимости от выбора режима сложности
def best_move(state, mode='extreme',pers=2,ai=1):
    inf = float('inf')
    #score = None
    move = None
    if mode == 'extreme':
        best_score = -inf
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax(state, 0, False,pers,ai)
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
                    score = minimax_lose(state, 0, True,pers,ai)
                    state[i][j] = 0
                    if score < 0:
                        return (i,j)
                    if score < best_score:
                        best_score = score
                        move = (i,j)
    if mode == 'random':
        move = random_sol(state)
    return move
# основной minimax алгоритм оптимального решения
def minimax(state, depth, isMaximazing, pers, ai):
    win_ai = check_win(state, ai=ai)
    win_per = check_lose(state,pers=pers)
    win_tie = check_tie(state,ai=ai,pers=pers)
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
        #score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = ai
                    score = minimax(state, depth+1, False, pers, ai)
                    state[i][j] = 0
                    if score > 0:
                        return score
                    best_score = max(score,best_score)
        return best_score
    else:
        inf = float('inf')
        best_score = inf
        #score = None
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = pers
                    score = minimax(state, depth + 1, True, pers, ai)
                    state[i][j] = 0
                    if score < 0:
                        return score
                    best_score = min(score, best_score)
        return best_score

# обратный minimax алгоритм проигрышного решения
def minimax_lose(state, depth, isMaximazing,pers,ai):
    win_ai = check_win(state,ai)
    win_per = check_lose(state,pers)
    win_tie = check_tie(state,ai,pers)
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
                    score = minimax_lose(state, depth+1, False,pers,ai)
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
                    score = minimax_lose(state, depth + 1, True,pers,ai)
                    state[i][j] = 0
                    if score < 0:
                        return score
                    best_score = min(score, best_score)
        return best_score
# выбор рандомного шага
def random_sol(state):
    sols = []
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                sols.append((i,j))
    return random.choice(sols)

# получение статистики
def get_stats(message,state, move='ai',pers=2,ai=1):
    chances = {'ai': 0, 'person': 0, 'tie': 0}
    get_all_possibles(state, chances, move=move,pers=pers,ai=ai)
    chances_sum = sum(chances.values())
    #print(f'sum:{chances_sum}')
    for key, value in chances.items():
        chances[key] = round((100 / chances_sum) * value, 2)
    return list(chances.values())
    # return (f"chances in proc: \n"
    #       f"ai: {chances['ai']}%\n"
    #       f"person: {chances['person']}%\n"
    #       f"tie: {chances['tie']}%\n")

# просчет всех ситуаций и учет выигрышей/проигрышей/ничей
def get_all_possibles(state, chances, move,pers,ai):
    win_ai = check_win(state,ai)
    win_per = check_lose(state,pers)
    win_tie = check_tie(state,ai,pers)
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
                    get_all_possibles(state, chances, move='person',pers=pers,ai=ai)
                    state[i][j] = 0
        return
    else:
        for i, column in enumerate(state):
            for j, elem in enumerate(column):
                if state[i][j] == 0:
                    state[i][j] = pers
                    get_all_possibles(state, chances, move='ai',pers=pers,ai=ai)
                    state[i][j] = 0
        return

