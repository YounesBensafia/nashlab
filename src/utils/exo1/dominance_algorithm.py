import numpy as np

def check_dominance(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    dominated_A = []
    dominated_B = []

    for i in range(n_rows):
        for j in range(n_rows):
            if i == j:
                continue

            greater_or_equal = True
            strictly_greater = False

            for c in range(n_cols):
                if matrix[i][c][0] < matrix[j][c][0]:
                    greater_or_equal = False
                    break
                elif matrix[i][c][0] > matrix[j][c][0]:
                    strictly_greater = True

            if greater_or_equal and strictly_greater:
                dominated_A.append((j, i)) 

    for i in range(n_cols):
        for j in range(n_cols):
            if i == j:
                continue

            greater_or_equal = True
            strictly_greater = False

            for r in range(n_rows):
                if matrix[r][i][1] < matrix[r][j][1]:
                    greater_or_equal = False
                    break
                elif matrix[r][i][1] > matrix[r][j][1]:
                    strictly_greater = True

            if greater_or_equal and strictly_greater:
                dominated_B.append((j, i)) 

    return dominated_A, dominated_B

def remove_dominated_strategies(matrix):
    is_numpy = isinstance(matrix, np.ndarray)
    if is_numpy:
        matrix = matrix.tolist()
    
    removed_rows = []
    removed_cols = []
    
    while True:
        A_dom, B_dom = check_dominance(matrix)
        
        if not A_dom and not B_dom:
            break
        
        rows_to_remove = set()
        cols_to_remove = set()
        
        for dominated, _ in A_dom:
            rows_to_remove.add(dominated)
        
        for dominated, dominating in B_dom:
            cols_to_remove.add(dominated)
        
        for row_idx in sorted(rows_to_remove, reverse=True):
            removed_rows.append(row_idx)
            matrix.pop(row_idx)
        
        for col_idx in sorted(cols_to_remove, reverse=True):
            removed_cols.append(col_idx)
            for row in matrix:
                row.pop(col_idx)
        
        if not matrix or not matrix[0]:
            break
    
    if is_numpy:
        matrix = np.array(matrix)
    
    return matrix, removed_rows, removed_cols
