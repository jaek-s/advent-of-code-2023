import importlib
import os

import typer
from typing_extensions import Annotated
from rich import print

current_dir = os.path.dirname(os.path.abspath(__file__))


def main(
    day: int,
    use_test_input: Annotated[
        bool,
        typer.Option(
            "--test", "-t", help="Read input from `test.txt` instead of `input.txt`"
        ),
    ] = False,
):
    formatted_day = f"{day:02}"
    try:
        solvers = importlib.import_module(f"day{formatted_day}.solver")
    except ModuleNotFoundError:
        print(
            f"[bold red]No solvers found![/bold red] Please create a [blue]`./day{formatted_day}/solvers.py`[/blue] file."
        )
        return

    print(f"[bold]Day {formatted_day}[/bold]")

    file_name = "test" if use_test_input else "input"
    with open(f"{current_dir}/day{formatted_day}/{file_name}.txt") as file:
        input = file.read()

    if not hasattr(solvers, "puzzle1") and not hasattr(solvers, "puzzle2"):
        print(
            f"Please add a [blue]`puzzle1`[/blue] and/or [blue]`puzzle2`[/blue] function to [blue]`./day{formatted_day}/solvers.py`[/blue]"
        )
        return

    if hasattr(solvers, "puzzle1"):
        print(f"puzzle 1 solution: [bold green]{solvers.puzzle1(input)}[/bold green]")
    else:
        print(
            f"puzzle 1 solution: [bold red]No solver found![/bold red] Please create a [blue]`puzzle1`[/blue] function"
        )

    if hasattr(solvers, "puzzle2"):
        print(f"puzzle 2 solution: [bold green]{solvers.puzzle2(input)}[/bold green]")
    else:
        print(
            f"puzzle 2 solution: [bold red]No solver found![/bold red] Please create a [blue]`puzzle2`[/blue] function"
        )


if __name__ == "__main__":
    typer.run(main)
