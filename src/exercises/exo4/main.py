from utils.exo3.opti import pareto_optimal_profiles
from typing import List, Tuple
from config.settings import GAME

from rich.console import Console
from rich.table import Table
from rich import box


def matrix_to_rich_table(matrix: List[List[Tuple[int, int]]], highlight: set) -> Table:
    cols = len(matrix[0])
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Row/Col", style="dim", no_wrap=True)
    for c in range(cols):
        table.add_column(f"C{c}", justify="center")

    for i, row in enumerate(matrix):
        cells = []
        for j, (a, b) in enumerate(row):
            text = f"({a},{b})"
            if (i, j) in highlight:
                cells.append(f"[bold green]{text}[/]")
            else:
                cells.append(text)
        table.add_row(f"R{i}", *cells)
    return table


def main() -> None:
    console = Console()
    nd = pareto_optimal_profiles(GAME)
    nd_set = {(i, j) for (i, j), _ in nd}

    console.rule("[bold cyan]Game matrix[/]")
    console.print(matrix_to_rich_table(GAME, nd_set))

    console.rule("[bold magenta]Pareto non-dominated profiles[/]")
    if not nd:
        console.print("No Pareto non-dominated profiles found.", style="yellow")
        return

    for (i, j), payoff in nd:
        console.print(f"Profile [bold]({i},{j})[/]: [green]{payoff}[/]")

    console.print()
    console.print(f"Found {len(nd)} Pareto non-dominated profile(s).", style="bold green")


if __name__ == "__main__":
    main()