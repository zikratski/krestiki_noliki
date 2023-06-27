import numpy as np

matr = np.zeros((3,3))
#print(matr)



def AI_get_solutions(matr):
    columns_len = len(matr[0])
    rows_len = len(matr)
    solutions = []
    state = matr[:] # копируем матрицу в state
    #win_lines - здесь будем хранить для каждого возможного решения(тройки) координаты
    win_lines = {f"c{i}":np.array([]) for i in range(rows_len)} | {f"r{i}":np.array([]) for i in range(columns_len)} | {f"d{i}":np.array([]) for i in range(2)}
    #print(win_lines)
    search_solutions(state,solutions)

    return solutions

def search_solutions(state,solutions):
    if check_state(state):
        pass
    else:
        candidates = get_candidates(state)
        for c_move in candidates:
            matr[c_move[0]][c_move[1]] = 1
            for p_move in candidates:
                if p_move != c_move:
                    matr[c_move[0]][c_move[1]] = 2
                    search_solutions(state,solutions)
                    matr[c_move[0]][c_move[1]] = 0
            matr[c_move[0]][c_move[1]] = 0

def check_state(state):
    ...

def get_candidates(state):
    candidates = np.array([])
    for i in matr:
        for j in matr[i]:
            if matr[i][j] == 0:
                candidates += [(i,j)]

    return candidates