import numpy as np

import algo, algo2

def play(mode):
    matr = np.array([[1, 0, 0], [2, 0, 1], [1, 0, 2]])
    matr_zero = np.zeros_like(matr)
    which_move = 'person'
    state = matr_zero[:]
    print('Welcom to the tic tac toe game!')
    which_move = input('Who is moving first?\nPrint ai or person: ')
    while True:
        if algo.check_win(state) or algo.check_lose(state) or algo.check_tie(state):
            break
        print(state)
        show_stats = int(input('Print 1 to show stats else 0: '))
        if which_move == 'person':
            if show_stats:
                algo2.get_stats(state,'person')
            i = int(input('i: '))
            j = int(input('j: '))
            state[i][j] = 2
            which_move = 'ai'
        elif which_move == 'ai':
            if show_stats:
                algo2.get_stats(state,'ai')
            ij = algo2.best_move(state, mode)
            state[ij[0]][ij[1]] = 1
            which_move = 'person'




def comp_move(matr,level='extreme',stats_show='False'):
    state = matr[:]
    move = None
    move = algo2.best_move(state, level)
    if stats_show:
        algo2.get_stats(state,move='ai')
    state[move[0]][move[1]] = 1
    return state


if __name__ == '__main__':
    play('extreme')