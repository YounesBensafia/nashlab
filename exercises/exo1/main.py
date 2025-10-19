import copy
from src.dominance_algorithm import remove_dominated_strategies
from config.exo1_config import GAME 

def main() -> None:
    game_copy = copy.deepcopy(GAME)
    reduced, _, _ = remove_dominated_strategies(game_copy)
    print(reduced)
    

if __name__ == "__main__":
    main()