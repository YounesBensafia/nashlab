import numpy as np
from utils.exo5.calculate_expectations import calculate_expectations
def check_support_equality(expectations, support):
    """Check if all strategies in the support have equal utility."""
    support_values = [expectations[k] for k in support]
    return all(abs(val - support_values[0]) < 1e-6 for val in support_values)

def check_no_strictly_better_outside_support(expectations, support):
    return all(expectations[k] <= max(expectations[s] for s in support) + 1e-6 for k in set(range(len(expectations))) - set(support))

def is_nash_equilibrium(A, B, sigma1, sigma2):
    support1 = np.where(sigma1 > 1e-8)[0]
    support2 = np.where(sigma2 > 1e-8)[0]

    U1 = calculate_expectations(A, sigma2, axis=0)
    U2 = calculate_expectations(B, sigma1, axis=1)

    equality1 = check_support_equality(U1, support1)
    no_better1 = check_no_strictly_better_outside_support(U1, support1)

    equality2 = check_support_equality(U2, support2)
    no_better2 = check_no_strictly_better_outside_support(U2, support2)

    return equality1 and no_better1 and equality2 and no_better2