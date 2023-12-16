import re
from copy import copy
from collections import defaultdict, namedtuple

re_all_dots = re.compile(r"^\.+$")
Point = namedtuple("Point", ["x", "y"])

EXPANSION_FACTOR = 1_000_000


def puzzle1(input: str):
    universe = parse_input(input)
    galaxy_locations = get_galaxy_locations(universe)

    distances = {}
    for location_idx, location in enumerate(galaxy_locations):
        for other_idx, other_location in enumerate(galaxy_locations):
            if distances.get((location_idx, other_idx)) or distances.get(
                (other_idx, location_idx)
            ):
                continue

            dist = abs(location.x - other_location.x) + abs(
                location.y - other_location.y
            )

            distances[(location_idx, other_idx)] = dist

    return sum(distances.values())


def puzzle2(input: str):
    empty_rows = get_empty_row_indices(input)
    empty_cols = get_empty_col_indices(input)
    galaxy_locations = get_galaxy_locations(input)

    distances = {}

    for location_idx, location in enumerate(galaxy_locations):
        for other_idx, other_location in enumerate(galaxy_locations):
            if distances.get((location_idx, other_idx)) or distances.get(
                (other_idx, location_idx)
            ):
                continue

            count_empty_cols_traversed = get_empties_traversed_count(
                location.x, other_location.x, empty_cols
            )
            x_expansion_accounting = (
                count_empty_cols_traversed * EXPANSION_FACTOR
                - count_empty_cols_traversed
            )
            x_dist = abs(location.x - other_location.x) + x_expansion_accounting

            count_empty_rows_traversed = get_empties_traversed_count(
                location.y, other_location.y, empty_rows
            )
            y_expansion_accounting = (
                count_empty_rows_traversed * EXPANSION_FACTOR
                - count_empty_rows_traversed
            )
            y_dist = abs(location.y - other_location.y) + y_expansion_accounting

            distances[(location_idx, other_idx)] = x_dist + y_dist

    return sum(distances.values())


def parse_input(input: str):
    partially_expanded_universe = expand_universe(input)

    return expand_universe(rotate_universe(partially_expanded_universe))


def get_galaxy_locations(universe: str):
    galaxy_locations = []
    for y, line in enumerate(universe.splitlines()):
        for x, char in enumerate(line):
            if char != "#":
                continue

            galaxy_locations.append(Point(x, y))

    return galaxy_locations


def expand_universe(universe: str):
    lines = universe.splitlines()
    lines_copy = copy(lines)
    insert_offset = 0

    for i, line in enumerate(lines):
        if not re_all_dots.match(line):
            continue

        # This would probably fuck up if the first line or column was all dots
        # but our inputs don't have that, so hurray!
        lines_copy.insert(i + insert_offset, line)
        insert_offset += 1

    return "\n".join(lines_copy)


def rotate_universe(universe: str):
    lines = universe.splitlines()
    rotated_lines = defaultdict(str)

    for line in lines:
        for i, char in enumerate(line):
            rotated_lines[i] = char + rotated_lines[i]

    return "\n".join(rotated_lines.values())


def get_empty_row_indices(input: str):
    empty_rows = []

    for i, line in enumerate(input.splitlines()):
        if not re_all_dots.match(line):
            continue

        empty_rows.append(i)

    return empty_rows


def get_empty_col_indices(input: str):
    return get_empty_row_indices(rotate_universe(input))


def get_empties_traversed_count(
    galaxy_1_coordinate: int, galaxy_2_coordinate: int, empties: list[int]
):
    count = 0

    for empty in empties:
        if (galaxy_1_coordinate > empty and galaxy_2_coordinate > empty) or (
            galaxy_1_coordinate < empty and galaxy_2_coordinate < empty
        ):
            continue

        count += 1

    return count
