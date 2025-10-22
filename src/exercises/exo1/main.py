import copy
from utils.exo1.dominance_algorithm import remove_dominated_strategies
from config.exo1_config import GAME 

def main() -> int:
    return print_game_reduction()

def print_game_reduction():
    game_copy = copy.deepcopy(GAME)
    reduced, _, _ = remove_dominated_strategies(game_copy)
    print("original game:")
    print(GAME)
    print("reduced game:")
    print(reduced)
    return 0
    
if __name__ == "__main__":
    main()