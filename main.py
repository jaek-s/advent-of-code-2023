import importlib

import typer
from rich import print


def main(day: int):
    try:
        solvers = importlib.import_module(f"day{day:0>2}.solver")
    except ModuleNotFoundError:
        print(
            f"[bold red]No solvers found![/bold red] Please create a [blue]./day{day:0>2}/solvers.py[/blue] file."
        )
        return

    print(f"[bold]Day {day:0>2}[/bold]")

    if not hasattr(solvers, "puzzle1") and not hasattr(solvers, "puzzle2"):
        print(
            f"Please add a [blue]`puzzle1`[/blue] and/or [blue]puzzle2[/blue] function to [blue]./day{day:0>2}/solvers.py[/blue]"
        )
        return

    if hasattr(solvers, "puzzle1"):
        print(f"puzzle 1 solution: [bold green]{solvers.puzzle1()}[/bold green]")
    else:
        print(
            f"puzzle 1 solution: [bold red]No solver found![/bold red] Please create a [blue]puzzle1[/blue] function"
        )

    if hasattr(solvers, "puzzle2"):
        print(f"puzzle 2 solution: [bold green]{solvers.puzzle2()}[/bold green]")
    else:
        print(
            f"puzzle 2 solution: [bold red]No solver found![/bold red] Please create a [blue]puzzle2[/blue] function"
        )


if __name__ == "__main__":
    typer.run(main)
