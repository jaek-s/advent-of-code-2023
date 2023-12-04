import re
from pprint import pprint

from helpers import open_input

# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #

match_part_numbers = re.compile(r"\d+")  # match any amount of digits
match_symbols = re.compile(r"[^\d\.]")  # match anything other than a digit or a period


def get_part_num_sum_for_line(index: int, lines: list[str]):
    sum = 0

    current_line = lines[index]
    prev_line = lines[index - 1] if index > 0 else ""
    next_line = lines[index + 1] if index < len(lines) - 1 else ""

    for match in match_part_numbers.finditer(current_line):
        match_start, match_end = match.span()

        search_start = match_start - 1 if match_start > 0 else 0
        search_end = (
            match_end + 1 if match_end < len(current_line) else len(current_line)
        )

        if (
            match_symbols.search(current_line[search_start])
            or match_symbols.search(current_line[search_end - 1])
            or (
                match_symbols.search(prev_line, search_start, search_end)
                if prev_line
                else False
            )
            or (
                match_symbols.search(next_line, search_start, search_end)
                if next_line
                else False
            )
        ):
            sum += int(match[0])

    return sum


def solve_first_puzzle():
    sum = 0

    with open_input("03") as file:
        lines = file.read().strip().split("\n")

        for index in range(0, len(lines)):
            sum += get_part_num_sum_for_line(index, lines)

    return sum


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


if __name__ == "__main__":
    print(f"first puzzle solution: {solve_first_puzzle()}")
    # print(f"second puzzle solution: {solve_second_puzzle()}")
