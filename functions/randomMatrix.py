import numpy as np
import random
def random_matrix(rows, cols):
    return np.array([[(random.randint(0, 7), random.randint(0, 7)) for _ in range(cols)] for _ in range(rows)])

