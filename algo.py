import random
import numpy as np





def AI_get_solutions(matr, mode='standart'):
    columns_len = len(matr[0])
    rows_len = len(matr)
    solutions = []
    loses = []
    state = matr[:]
    solution = None
    if mode == 'standart':
        plays = list()
        search_solutions(state,plays,solutions, loses)
        print(f"len solutions: {len(solutions)}")
        solution = random.choice(solutions)[0]
    elif mode == 'random':
        solution = random_sol(state)
    elif mode == 'minmax':
        solution = best_move(state)
    return solution

def random_sol(state):
    sols = []
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                sols.append((i,j))
    return random.choice(sols)

def search_solutions(state,plays,solutions, loses):
    candidates = get_candidates(state)
    for c_move in candidates:
        state[c_move[0]][c_move[1]] = 1
        plays.append(c_move)
        for p_move in candidates:
            if p_move != c_move:
                plays.append(p_move)
                state[p_move[0]][p_move[1]] = 2
                if check_win(state):
                    solutions.append(plays)
                elif check_lose(state):
                    loses.append(plays)
                else:
                    plays = search_solutions(state,plays,solutions,loses)

                plays = plays[:-1]
                state[p_move[0]][p_move[1]] = 0
        state[c_move[0]][c_move[1]] = 0
        plays = plays[:-1]
    return plays


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

def check_tie(state,ai=1,pers=2):
    if 0 not in state and not check_lose(state,pers) and not check_win(state,ai):
        return True
    else:
        return False
def get_candidates(state):
    candidates = []
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if elem == 0:
                candidates.append(tuple([i,j]))
    return candidates


def best_move(state, mode='extreme',pers=2,ai=1):
    inf = float('inf')
    score = None
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
def minimax(state, depth, isMaximazing, pers, ai):
    # if depth == 1:
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
        score = None
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
        score = None
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
if __name__ == '__main__':
    matr = np.zeros((3, 3))
    #print(matr)
    solution = AI_get_solutions(matr, mode = 'minmax')
    print('i am here')
    print(solution)
