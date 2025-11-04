def find_nash_from_pair_matrix(payoff_matrix):
    """
    payoff_matrix: list[list[ (a_payoff, b_payoff) ]]
    returns: list of ((i,j), (a_payoff, b_payoff)) for each pure NE
    """
    # convert to list of lists (defensive)
    PM = [list(row) for row in payoff_matrix]
    n = len(PM)
    if n == 0:
        return []
    m = len(PM[0])
    for row in PM:
        if len(row) != m:
            raise ValueError("La matrice doit être rectangulaire (mêmes colonnes par ligne).")

    equilibria = []
    for i in range(n):
        for j in range(m):
            a_payoff, b_payoff = PM[i][j]
            best_A = True
            for k in range(n):
                other_a = PM[k][j][0]
                if other_a > a_payoff:
                    best_A = False
                    break
            best_B = True
            for l in range(m):
                other_b = PM[i][l][1]
                if other_b > b_payoff:
                    best_B = False
                    break

            if best_A and best_B:
                equilibria.append((a_payoff, b_payoff))

    return equilibria

