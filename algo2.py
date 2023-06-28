def best_move(state):
    inf = float('inf')
    best_score = -inf
    score = None
    for i, column in enumerate(state):
        for j, elem in enumerate(column):
            if state[i][j] == 0:
                state[i][j] = ai
                score = minimax(state, 0, false);
            state[i][j] = 0
            if (score > best_score):
                best_score = score
                move = (i,j)
