from typing import List, Sequence, Tuple
import numpy as _np

def pareto_optimal_profiles(matrix: Sequence) -> List[Tuple[Tuple[int, int], Tuple[float, float]]]:
    try:
         
        if isinstance(matrix, _np.ndarray):
            M = matrix.tolist()
        else:
            M = [list(row) for row in matrix]
    except Exception:
        M = [list(row) for row in matrix]

    profiles: List[Tuple[Tuple[int, int], Tuple[float, float]]] = []
    n_rows = len(M)
    if n_rows == 0:
        return []
    n_cols = len(M[0])

    for i in range(n_rows):
        for j in range(n_cols):
            profiles.append(((i, j), tuple(M[i][j])))

    dominated = [False] * len(profiles)

    for idx_p, (_, payoff_p) in enumerate(profiles):
        for idx_q, (_, payoff_q) in enumerate(profiles):
            if idx_p == idx_q:
                continue
            ge = all(q >= p for q, p in zip(payoff_q, payoff_p))
            gt = any(q > p for q, p in zip(payoff_q, payoff_p))
            if ge and gt:
                dominated[idx_p] = True
                break

    nondominated = [profiles[i] for i in range(len(profiles)) if not dominated[i]]
    return nondominated


