from rich.console import Console
from rich.table import Table
from rich import box

import copy
from utils.exo1.dominance_algorithm import remove_dominated_strategies
from config.settings import GAME


def matrix_to_table(matrix):
    cols = len(matrix[0])
    table = Table(show_header=False, box=box.SIMPLE_HEAVY)
    for i in range(cols):
        table.add_column(justify="center")

    for row in matrix:
        table.add_row(*[f"({a},{b})" for a, b in row])
    return table


def print_game_reduction() -> int:
    console = Console()
    game_copy = copy.deepcopy(GAME)
    reduced, removed_rows, removed_cols = remove_dominated_strategies(game_copy)

    console.rule("Original game")
    console.print(matrix_to_table(GAME))

    if removed_rows or removed_cols:
        console.rule("Reduced game")
        console.print(matrix_to_table(reduced))
        console.print(f"Removed rows: {removed_rows}")
        console.print(f"Removed columns: {removed_cols}")
    else:
        console.rule("No strictly dominated strategies found")

    return 0


def main() -> int:
    return print_game_reduction()


if __name__ == "__main__":
    main()