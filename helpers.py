import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def get_input_lines(day: str):
    with open(f"{current_dir}/day{day}/input.txt") as file:
        for line in file.readlines():
            yield line.strip()
