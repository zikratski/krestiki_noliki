import random

import numpy as np

matr = np.zeros((3,3))
#print(matr)



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
        solution = random.choice(solutions)[0]
    elif mode == 'random':
        solution = random_sol(state)
    elif mode == 'minmax':
        pass
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


# def check_state(state, solutions, win_lines):
#     for k,v in win_lines.items():
#         if v[0] == 3:
#             solutions.append(v[1:])
#             return True
#     return False


def check_win(state):
    for column in state:
        if np.array_equal(column, np.array([1,1,1])):
            return True
    for row in state[:,]:
        if np.array_equal(row, np.array([1,1,1])):
            return True
    if state[0][0] == state[1][1] == state[2][2] == 1:
        return True
    elif state[0][2] == state[1][1] == state[2][0] == 1:
        return True
    else:
        return False

def check_lose(state):
    for column in state:
        if np.array_equal(column, np.array([2,2,2])):
            return True
    for col_index in range(state.shape[1]):
        column = state[:, col_index]
        if np.array_equal(column, np.array([2,2,2])):
            return True
    if state[0][0] == state[1][1] == state[2][2] == 2:
        return True
    elif state[0][2] == state[1][1] == state[2][0] == 2:
        return True
    else:
        return False

def check_tie(state):
    if 0 not in state and not check_lose(state) and not check_win(state):
        return True
def get_candidates(state):
    candidates = []
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if elem == 0:
                candidates.append(tuple([i,j]))
    return candidates


#solution = AI_get_solutions(matr)
#print(solution)

matr_ex = np.array([[1,2,1],[1,2,0],[2,2,0]])
check_lose(matr_ex)