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


game = [
    [(3,1), (2,2), (1,0)],
    [(1,1), (3,0), (2,3)],
    [(0,4), (1,2), (1,1)]
]

A_dom, B_dom = check_dominance(game)

print("Player A dominated strategies (row_j is dominated by row_i):", A_dom)
print("Player B dominated strategies (col_j is dominated by col_i):", B_dom)
