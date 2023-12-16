import re
from copy import copy
from collections import defaultdict, namedtuple

from rich import print

re_all_dots = re.compile(r"^\.+$")
Point = namedtuple("Point", ["x", "y"])


def puzzle1(input: str):
    universe = parse_input(input)

    galaxy_locations = []
    for y, line in enumerate(universe.splitlines()):
        for x, char in enumerate(line):
            if char != "#":
                continue

            galaxy_locations.append(Point(x, y))

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

            if dist == 0:
                continue

            distances[(location_idx, other_idx)] = dist

    return sum(distances.values())


def parse_input(input: str):
    partially_expanded_universe = expand_universe(input)

    return expand_universe(rotate_universe(partially_expanded_universe))


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


# def find_dist_to_closest_galaxy(location: Point, galaxy_locations: list[Point]):
#     """
#     I misunderstood the assignment and don't actually need this function.
#     Commenting out for now in case its useful in puzzle 2
#     """
#     lowest_dist = 999_999
#     for other_location in galaxy_locations:
#         dist = abs(location.x - other_location.x) + abs(location.y + other_location.y)

#         if dist == 0 or dist + 1 > lowest_dist:
#             continue

#         lowest_dist = dist + 1

#     return lowest_dist
