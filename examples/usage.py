from functions.dominance_algorithm import dominance_check
from main import matrix


def demo(n: int = 4) -> None:
    pairs = matrix(n, as_pairs=True)
    print("pairs matrix (shape", pairs.shape, "):\n", pairs)

    # Use the first coordinate (x) as a payoff matrix for demonstration
    payoff = pairs[:, :, 0]
    print("\nextracted payoff matrix (using x coordinate):\n", payoff)

    has_dom = dominance_check(payoff)
    print("\nDoes the payoff matrix contain any strictly dominated row/column?", has_dom)

    # Also show the scalar matrix mode
    scalars = matrix(n, as_pairs=False)
    print("\nscalar random matrix (shape", scalars.shape, "):\n", scalars)
    print("dominance on scalar matrix:", dominance_check(scalars))


if __name__ == "__main__":
    demo(4)
