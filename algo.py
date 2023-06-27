import numpy as np

matr = np.zeros((3,3))
#print(matr)



def AI_get_solutions(matr):
    columns_len = len(matr[0])
    rows_len = len(matr)
    solutions = []
    #win_lines - здесь будем хранить для каждого возможного решения(тройки) координаты
    win_lines = {f"c{i}":tuple() for i in range(rows_len)} | {f"r{i}":tuple() for i in range(columns_len)} | {f"d{i}":tuple() for i in range(2)}
    #print(win_lines)


    return solutions

AI_get_solutions(matr)