import numpy as np
from utils.exo5.calculate_expectations import calculate_expectations
from utils.exo5.checking import is_nash_equilibrium

A = np.array([[4, 5, 1], [2, 8, 3], [3, 9, 2]])
B = np.array([[3, 1, 2], [1, 4, 6], [0, 6, 5]])

sigma1 = np.array([1/3, 1/3, 1/3])
sigma2 = np.array([1/2, 1/2, 0])


def main():
    if is_nash_equilibrium(A, B, sigma1, sigma2):
        print("✓ (sigma1, sigma2) est un équilibre de Nash!")
    else:
        print("✗ (sigma1, sigma2) n'est PAS un équilibre de Nash.")

if __name__ == "__main__":
    main()
