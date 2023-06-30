import numpy as np

import algo, algo2
import graphic


def play(mode,pers=2,ai=1):
    matr = np.array([[1, 0, 0], [2, 0, 1], [1, 0, 2]])
    matr_zero = np.zeros_like(matr)
    which_move = 'person'
    state = matr_zero[:]
    print('Welcom to the tic tac toe game!')
    which_move = input('Who is moving first?\nPrint ai or person: ')
    while True:
        if algo.check_win(state,ai=ai) or algo.check_lose(state,pers=pers) or algo.check_tie(state,ai=ai,pers=pers):
            break
        #print(state)
        graphic.graph(state)

        if which_move == 'person':
            show_stats = int(input('Print 1 to show stats else 0: '))
            if show_stats:
                algo2.get_stats(state,'person')
            i = int(input('i: '))
            j = int(input('j: '))
            state[i][j] = pers
            which_move = 'ai'
        elif which_move == 'ai':
            ij = algo2.best_move(state, mode,pers=pers,ai=ai)
            state[ij[0]][ij[1]] = ai
            which_move = 'person'
    graphic.graph(state)




def comp_move(matr,level='extreme',stats_show='False',ai=1):
    state = matr[:]
    move = None
    move = algo2.best_move(state, level)
    if stats_show:
        algo2.get_stats(state,move='ai')
    state[move[0]][move[1]] = ai
    return state


if __name__ == '__main__':
    # mode = 'easy'
    mode = 'easy'
    play(mode,pers=1,ai=2)