import importlib

import typer
from rich import print


def main(day: int):
    try:
        solvers = importlib.import_module(f"day{day:0>2}.solver")
    except ModuleNotFoundError:
        print(f"[bold red]No solvers found![/bold red] Please create a [blue]./day{day:0>2}/solvers.py[/blue] file.")
        return

    print(f"[bold]Day {day:0>2}[/bold]")

    if not solvers.solve_first_puzzle and not solvers.solve_first_puzzle:
        print(f"Please add a [blue]`solve_first_puzzle`[/blue] and/or [blue]solve_second_puzzle[/blue] function to [blue]./day{day:0>2}/solvers.py[/blue]")
        return

    if solvers.solve_first_puzzle:
        print(f"puzzle 1 solution: [bold green]{solvers.solve_first_puzzle()}[/bold green]")
    else:
        print(f"puzzle 1 solution: [bold red]No solver found![/bold red] Please create a [blue]solve_first_puzzle[/blue] function")

    if solvers.solve_first_puzzle:
        print(f"puzzle 2 solution: [bold green]{solvers.solve_second_puzzle()}[/bold green]")
    else:
        print(f"puzzle 1 solution: [bold red]No solver found![/bold red] Please create a [blue]solve_second_puzzle[/blue] function")


if __name__ == "__main__":
    typer.run(main)
