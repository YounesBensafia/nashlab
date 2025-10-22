from src.exercises.exo1.main import main as exo1
from src.exercises.exo2.main import main as exo2
import questionary
from rich.console import Console
from config.settings import choice_style
from config.settings import choice_question
console = Console()


def main() -> None:
    console.rule("[bold red]Select an exercise[/]")

    choice = questionary.select(
        "Select the exercise to run:",
        choices=choice_question,
        style=choice_style,
    ).ask()

    if choice is None:
        console.print("No selection made. Exiting.", style="bold red")
        return
    
    if choice == choice_question[0]:
        exo1()
    elif choice == choice_question[1]:
        exo2()

    console.print("Execution finished.", style="bold green")

if __name__ == "__main__":
    main()