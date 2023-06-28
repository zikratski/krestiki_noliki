import numpy as np

import algo, algo2

def play():
    matr = np.array([[1, 0, 0], [2, 0, 1], [1, 0, 2]])
    matr_zero = np.zeros_like(matr)
    while True:
        if algo.check_win(matr_zero) or algo.check_lose(matr_zero) or algo.check_tie(matr_zero):
            break
        inp = input('i,j')
        matr_zero[int(inp[0])][int(inp[-1])] = 2
        print(matr_zero)
        print()
        bm = algo2.best_move(matr_zero)
        matr_zero[bm[0]][bm[1]] = 1
        print(matr_zero)
        print()


play()