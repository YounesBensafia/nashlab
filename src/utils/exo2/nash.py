import numpy as np

def find_pure_nash(matrix):
    """
    Find pure-strategy Nash equilibria for a 2-player game matrix.

    Args:
        matrix (np.ndarray): A 2D array where each entry is a tuple (a, b)
                             representing payoffs for players 1 and 2.

    Returns:
        list: A list of tuples (row, col) representing Nash equilibria.
    """
    nash_equilibria = []
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            player1_payoff = matrix[i, j][0]
            player2_payoff = matrix[i, j][1]

            # Check if player 1's strategy is the best response
            best_response_player1 = all(
                player1_payoff >= matrix[k, j][0] for k in range(rows)
            )

            # Check if player 2's strategy is the best response
            best_response_player2 = all(
                player2_payoff >= matrix[i, l][1] for l in range(cols)
            )

            if best_response_player1 and best_response_player2:
                nash_equilibria.append((i, j))

    return nash_equilibria