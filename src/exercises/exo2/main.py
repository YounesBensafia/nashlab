from utils.exo2.dominance import find_dominant_strategies
from config.settings import GAME
import copy


def main() -> None:
    GAME_matrix = copy.deepcopy(GAME)
    print("Game matrix:")
    print(GAME_matrix)
    dominant_rows, dominant_cols = find_dominant_strategies(GAME_matrix, kind="strict")
    print("Dominant strategies for Player A (rows):", dominant_rows)
    print("Dominant strategies for Player B (columns):", dominant_cols)

if __name__ == "__main__":
    main()