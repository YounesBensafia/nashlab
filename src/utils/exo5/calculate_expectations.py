def calculate_expectations(matrix, strategy, axis):
    """Calculate expected utilities for each pure strategy."""
    expectations = []
    for i in range(matrix.shape[axis]):
        products = [matrix[i, j] * strategy[j] if axis == 0 else strategy[i] * matrix[i, j] for j in range(matrix.shape[1-axis])]
        expectations.append(sum(products))
    return expectations