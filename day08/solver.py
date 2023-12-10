from math import lcm
import re

match_brackets = re.compile(r"[\()]")


def puzzle1(input: str):
    directions, locations = parse_input(input)

    return get_step_count(directions, locations, "AAA")


def puzzle2(input: str):
    directions, locations = parse_input(input)

    current_locations = list(
        filter(lambda location: location.endswith("A"), locations.keys())
    )

    steps_to_destination = [
        get_step_count(directions, locations, current_location)
        for current_location in current_locations
    ]

    return lcm(*steps_to_destination)


def parse_input(input: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    directions, locations_str = input.split("\n\n")

    locations = dict()
    for location in locations_str.splitlines():
        key, choices = location.split(" = ")
        locations[key] = tuple(match_brackets.sub("", choices).split(", "))

    return [0 if direction == "L" else 1 for direction in directions], locations


def get_step_count(
    directions: list[int], locations: dict[str, tuple[str, str]], start_key: str
) -> int:
    step_count = 0
    current_location = start_key
    while not current_location.endswith("Z"):
        current_location = locations[current_location][
            get_next_direction(directions, step_count)
        ]

        step_count += 1

    return step_count


def get_next_direction(directions: list[int], step_count: int) -> int:
    direction_key = step_count

    while direction_key - len(directions) >= 0:
        direction_key = direction_key - len(directions)

    return directions[direction_key]
