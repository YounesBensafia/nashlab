from utils.exo3.nash import find_nash_from_pair_matrix
from rich.console import Console
from rich.table import Table
from rich import box
from config.settings import GAME
console = Console()
def matrix_to_table(matrix):
    cols = len(matrix[0])
    table = Table(show_header=False, box=box.SIMPLE_HEAVY)
    for i in range(cols):
        table.add_column(justify="center")

    for row in matrix:
        table.add_row(*[f"({a},{b})" for a, b in row])
    return table
def print_nash_equilibria() -> int:
    console.rule("Game Matrix")
    console.print(matrix_to_table(GAME))

    equilibria = find_nash_from_pair_matrix(GAME)

    if equilibria:
        console.rule("Nash Equilibria Found")
        eq_table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE_HEAVY)
        eq_table.add_column("A's Payoff", justify="center")
        eq_table.add_column("B's Payoff", justify="center")

        for a_payoff, b_payoff in equilibria:
            eq_table.add_row(str(a_payoff), str(b_payoff))

        console.print(eq_table)
    else:
        console.rule("No Nash Equilibria Found")

    return 0
def main() -> int:
    return print_nash_equilibria()
if __name__ == "__main__":
    main()