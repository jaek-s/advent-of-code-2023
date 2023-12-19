from rich import print

from day11.solver import rotate_universe

def puzzle1(input: str):
    summary = 0
    for pattern in input.split("\n\n"):
        col_index = get_column_reflection_index(pattern)

        if col_index != None:
            summary += col_index + 1
            continue

        row_index = get_row_reflection_index(pattern)

        if row_index != None:
            summary += (row_index + 1) * 100

    return summary


def get_column_reflection_index(pattern: str) -> int | None:
    return get_row_reflection_index("\n".join(rotate_universe(pattern).splitlines()))


def get_row_reflection_index(pattern: str) -> int | None:
    found_index = None
    pattern_rows = pattern.splitlines()
    for i in range(0, len(pattern_rows)):
        if not check_reflectivity(pattern_rows, i):
            continue

        found_index = i
        break

    return found_index


def check_reflectivity(pattern_rows: list[str], index_to_check: int):
    left_ptr = index_to_check
    right_ptr = index_to_check + 1

    if not (left_ptr >= 0 and right_ptr < len(pattern_rows)):
        return False

    while left_ptr >= 0 and right_ptr < len(pattern_rows):
        if pattern_rows[left_ptr] == pattern_rows[right_ptr]:
            left_ptr -= 1
            right_ptr += 1
            continue

        return False


    return True
