import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def open_input(day: str):
    return open(f"{current_dir}/day{day}/input.txt")


def get_input_lines(day: str):
    with open_input(day) as file:
        for line in file:
            yield line.strip()
