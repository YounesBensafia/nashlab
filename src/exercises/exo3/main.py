from utils.exo3.nash import find_nash_from_pair_matrix
from rich.console import Console
from rich.table import Table
from rich import box
from config.settings import GAME

console = Console()


def matrix_to_table(matrix, highlight: set):
    cols = len(matrix[0])
    table = Table(show_header=True, box=box.SIMPLE_HEAVY)
    table.add_column("", style="dim")
    for i in range(cols):
        table.add_column(f"C{i}", justify="center")

    for r_idx, row in enumerate(matrix):
        cells = []
        for c_idx, (a, b) in enumerate(row):
            text = f"({a},{b})"
            if (r_idx, c_idx) in highlight:
                cells.append(f"[bold yellow]{text}[/]")
            else:
                cells.append(text)
        table.add_row(f"R{r_idx}", *cells)
    return table


def print_nash_equilibria() -> int:
    console.rule("Game Matrix")

    equilibria = find_nash_from_pair_matrix(GAME)
    highlights = {(i, j) for (i, j, a, b) in equilibria}

    console.print(matrix_to_table(GAME, highlights))

    if equilibria:
        console.rule("Nash Equilibria Found")
        eq_table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE_HEAVY)
        eq_table.add_column("Row", justify="center")
        eq_table.add_column("Col", justify="center")
        eq_table.add_column("A payoff", justify="center")
        eq_table.add_column("B payoff", justify="center")

        for i, j, a_payoff, b_payoff in equilibria:
            eq_table.add_row(str(i), str(j), str(a_payoff), str(b_payoff))

        console.print(eq_table)
        console.print(f"Found {len(equilibria)} equilibrium(s).", style="bold green")
    else:
        console.rule("No Nash Equilibria Found")
        console.print("No pure-strategy Nash equilibria were found for this game.", style="yellow")

    return 0


def main() -> int:
    return print_nash_equilibria()


if __name__ == "__main__":
    main()