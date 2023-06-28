import numpy as np

matr = np.zeros((3,3))
#print(matr)



def AI_get_solutions(matr):
    columns_len = len(matr[0])
    rows_len = len(matr)
    solutions = []
    state = matr[:]
    plays = list()
    search_solutions(state,plays,solutions)

    return solutions

def search_solutions(state,plays,solutions):
    candidates = get_candidates(state)
    for c_move in candidates:
        matr[c_move[0]][c_move[1]] = 1
        plays.append(c_move)
        for p_move in candidates:
            if p_move != c_move:
                plays.append(p_move)
                matr[p_move[0]][p_move[1]] = 2
                if check_win(state):
                    solutions.append(plays)
                    plays = plays[:-2]
                    return True
                elif check_lose(state):
                    plays = plays[:-2]
                    return False
                else:
                    search_solutions(state,plays,solutions)
                    plays = plays[:-2]
                matr[p_move[0]][p_move[1]] = 0
        matr[c_move[0]][c_move[1]] = 0


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
    for row in state[:,]:
        if np.array_equal(row, np.array([2,2,2])):
            return True
    if state[0][0] == state[1][1] == state[2][2] == 2:
        return True
    elif state[0][2] == state[1][1] == state[2][0] == 2:
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


sols = AI_get_solutions(matr)


print('change for kiryll')