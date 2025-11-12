import numpy as np

def find_sigma(A, B):
    """
    Find mixed strategy Nash equilibrium for two players.

    Args:
        A (np.ndarray): Payoff matrix for player 1.
        B (np.ndarray): Payoff matrix for player 2.

    Returns:
        tuple: Mixed strategies (sigma1, sigma2) for players 1 and 2.
    """
    # Number of strategies for each player
    num_strategies_1 = A.shape[0]
    num_strategies_2 = A.shape[1]

    # Correct the construction of A_eq_1 and A_eq_2 to ensure compatibility
    A_eq_1 = np.vstack([A.T, np.ones((1, num_strategies_1))])
    A_eq_2 = np.vstack([B, np.ones((1, num_strategies_2))])

    # Correct the construction of b_eq_1 and b_eq_2 to match the new dimensions
    b_eq_1 = np.append(np.zeros(num_strategies_1), 1)
    b_eq_2 = np.append(np.zeros(num_strategies_2), 1)

    # Solve for mixed strategies using linear programming
    sigma1 = np.linalg.lstsq(A_eq_1.T, b_eq_1, rcond=None)[0]
    sigma2 = np.linalg.lstsq(A_eq_2.T, b_eq_2, rcond=None)[0]

    # Ensure probabilities are non-negative
    sigma1 = np.maximum(sigma1, 0)
    sigma2 = np.maximum(sigma2, 0)

    return sigma1, sigma2

if __name__ == "__main__":
    A = np.array([[4, 5, 1], [2, 8, 3], [3, 9, 2]])
    B = np.array([[3, 1, 2], [1, 4, 6], [0, 6, 5]])

    sigma1, sigma2 = find_sigma(A, B)
    print("Mixed strategy for Player 1:", sigma1)
    print("Mixed strategy for Player 2:", sigma2)