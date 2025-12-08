def winner(state):
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in win_patterns:
        if state[a] == state[b] == state[c] and state[a] != " ":
            return state[a]
    return None

def game_over(state):
    return winner(state) is not None or " " not in state

def get_possible_moves(state):
    return [i for i in range(9) if state[i] == " "]

def make_move(state, move, player):
    new_state = state.copy()
    new_state[move] = player
    return new_state


def evaluate(state):
    if winner(state) == "X":
        return 1
    elif winner(state) == "O":
        return -1
    else:
        return 0


def alpha_beta_pruning(state, depth, alpha, beta, player):
    if depth == 0 or game_over(state):
        return evaluate(state)

    if player == "X":  
        best_score = float('-inf')

        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "O")

            best_score = max(best_score, score)
            alpha = max(alpha, score)

            if beta <= alpha:
                break  

        return best_score

    else: 
        best_score = float('inf')

        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "X")

            best_score = min(best_score, score)
            beta = min(beta, score)

            if beta <= alpha:
                break  

        return best_score


board = ["X", "O", "X",
         " ", "O", " ",
         " ", " ", "X"]

print(alpha_beta_pruning(board, 5, float('-inf'), float('inf'), "X"))
