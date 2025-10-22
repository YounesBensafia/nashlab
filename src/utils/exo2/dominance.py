from typing import List, Tuple, Sequence


def _as_list_matrix(matrix: Sequence) -> List[List[Tuple[int, int]]]:
    # Accept numpy arrays or lists
    try:
        # defer import to avoid making numpy a hard dependency here
        import numpy as _np  # type: ignore
        if isinstance(matrix, _np.ndarray):
            return matrix.tolist()
    except Exception:
        pass
    return [list(row) for row in matrix]


def find_dominant_strategies(matrix: Sequence, kind: str = "strict"):
    if kind not in ("strict", "weak"):
        raise ValueError("kind must be 'strict' or 'weak'")

    M = _as_list_matrix(matrix)
    n_rows = len(M)
    n_cols = len(M[0]) if n_rows > 0 else 0


    dominant_rows = []
    for i in range(n_rows):
        is_dominant = True
        for j in range(n_rows):
            if i == j:
                continue
            better_all = True
            strictly_better_at_least_one = False
            for c in range(n_cols):
                ai = M[i][c][0]
                aj = M[j][c][0]
                if kind == "strict":
                    if ai <= aj:
                        better_all = False
                        break
                else:
                    if ai < aj:
                        better_all = False
                        break
                    if ai > aj:
                        strictly_better_at_least_one = True
            if not better_all or (kind == "weak" and not strictly_better_at_least_one):
                is_dominant = False
                break
        if is_dominant:
            dominant_rows.append(i)

    dominant_cols = []
    for i in range(n_cols):
        is_dominant = True
        for j in range(n_cols):
            if i == j:
                continue
            better_all = True
            strictly_better_at_least_one = False
            for r in range(n_rows):
                bi = M[r][i][1]
                bj = M[r][j][1]
                if kind == "strict":
                    if bi <= bj:
                        better_all = False
                        break
                else:
                    if bi < bj:
                        better_all = False
                        break
                    if bi > bj:
                        strictly_better_at_least_one = True
            if not better_all or (kind == "weak" and not strictly_better_at_least_one):
                is_dominant = False
                break
        if is_dominant:
            dominant_cols.append(i)

    return dominant_rows, dominant_cols
