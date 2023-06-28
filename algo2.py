import numpy as np
def best_move(state):
    inf = float('inf')
    best_score = -inf
    score = None
    move = None
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                state[i][j] = 1
                score = minimax(state, 0, False)
                state[i][j] = 0
                if (score > best_score):
                    best_score = score
                    move = (i,j)
    state[move[0]][move[1]] = 1
def minimax(state, smth = 0, b = False):
    return 1

matr = np.array([[1,0,0],[2,0,1],[1,0,2]])

print(matr)
for _ in range(4):
    best_move(matr)
    print()
    print(matr)


