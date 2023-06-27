import numpy as np

matr = np.zeros((3,3))
#print(matr)



def AI_get_solutions(matr):
    columns_len = len(matr[0])
    rows_len = len(matr)
    solutions = []
    state = matr[:] # копируем матрицу в state
    #win_lines - здесь будем хранить для каждого возможного решения(тройки) координаты
    win_lines = {f"c{i}":np.array([0,set(),0]) for i in range(rows_len)} \
                | {f"r{i}":np.array([0,set(),0]) for i in range(columns_len)} \
                | {f"d{i}":np.array([0,set(),0]) for i in range(2)}
    #print(win_lines)
    search_solutions(state,solutions,win_lines)

    return solutions

def search_solutions(state,solutions,win_lines):
    if check_state(state, solutions, win_lines):
        return
    else:
        candidates = get_candidates(state)
        for c_move in candidates:
            matr[c_move[0]][c_move[1]] = win_lines[f"c{c_move[0]}"][2] = win_lines[f"r{c_move[1]}"][2] = 1
            win_lines[f"c{c_move[0]}"][0] += 1
            win_lines[f"c{c_move[0]}"][1].add(c_move)
            win_lines[f"r{c_move[1]}"][0] += 1
            win_lines[f"r{c_move[1]}"][1].add(c_move)

            for p_move in candidates:
                if p_move != c_move:
                    matr[p_move[0]][p_move[1]] = win_lines[f"c{p_move[0]}"][2] = win_lines[f"r{p_move[1]}"][2] = 2
                    win_lines[f"c{p_move[0]}"][0] += 1
                    win_lines[f"c{p_move[0]}"][1].add(p_move)
                    win_lines[f"r{p_move[1]}"][0] += 1
                    win_lines[f"r{p_move[1]}"][1].add(p_move)

                    search_solutions(state,solutions,win_lines)

                    matr[p_move[0]][p_move[1]] = win_lines[f"c{p_move[0]}"][2] = win_lines[f"r{p_move[1]}"][2] = 0
                    win_lines[f"c{p_move[0]}"][0] -= 1
                    win_lines[f"c{p_move[0]}"][1].remove(p_move)
                    win_lines[f"r{p_move[1]}"][0] -= 1
                    win_lines[f"r{p_move[1]}"][1].remove(p_move)

            matr[c_move[0]][c_move[1]] = win_lines[f"c{c_move[0]}"][2] = win_lines[f"r{c_move[1]}"][2] = 0
            win_lines[f"c{c_move[0]}"][0] -= 1
            win_lines[f"c{c_move[0]}"][1].remove(c_move)
            win_lines[f"r{c_move[1]}"][0] -= 1
            win_lines[f"r{c_move[1]}"][1].remove(c_move)

def check_state(state, solutions, win_lines):
    for k,v in win_lines.items():
        if v[0] == 3:
            solutions.append(v[1:])
            return True
    return False

def get_candidates(state):
    candidates = []
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if elem == 0:
                candidates.append(tuple([i,j]))
    return candidates


sols = AI_get_solutions(matr)