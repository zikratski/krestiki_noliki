import numpy as np

import algo, algo2

def play():
    matr = np.array([[1, 0, 0], [2, 0, 1], [1, 0, 2]])
    matr_zero = np.zeros_like(matr)
    print(matr_zero)
    while True:
        if algo.check_win(matr_zero) or algo.check_lose(matr_zero) or algo.check_tie(matr_zero):
            break
        #algo2.get_stats(state=matr_zero,move='person')
        ii = input('i: ')
        ij = input('j: ')
        matr_zero[int(ii)][int(ij)] = 2
        print(matr_zero)
        print()
        bm = algo2.best_move(matr_zero,mode='easy')
        matr_zero[bm[0]][bm[1]] = 1
        print(matr_zero)
        print()

def comp_move(matr,level='extreme',stats_show='False'):
    state = matr[:]
    move = None
    if stats_show:
        algo2.get_stats(state,move='ai')
    move = algo2.best_move(state,level)
    state[move[0]][move[1]] = 1
    return state


if __name__ == '__main__':
    play()