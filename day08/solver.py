import re

match_brackets = re.compile(r"[\()]")

def puzzle1(input: str):
    directions, locations_str = input.split("\n\n")

    locations = dict()
    for location in locations_str.splitlines():
        key, choices = location.split(" = ")
        locations[key] = tuple(match_brackets.sub("", choices).split(", "))

    step_count = 0
    direction_key = 0
    current_location = "AAA"
    while current_location != "ZZZ":
        direction = directions[direction_key]
        step_key = 0 if direction == "L" else 1

        current_location = locations[current_location][step_key]

        step_count += 1
        direction_key += 1

        if direction_key >= len(directions):
            direction_key = 0

    return step_count




