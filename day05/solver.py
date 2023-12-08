from pprint import pprint

from helpers import open_input

# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #


def puzzle1():
    with open_input("05") as file:
        almanac_categories = file.read().split("\n\n")

        categories = [
            parse_almanac_category(category)[1] for category in almanac_categories
        ]

        seeds = categories.pop(0)[0]

        locations = [get_seed_location(seed, categories) for seed in seeds]

    return min(locations)


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


def puzzle2():
    with open_input("05") as file:
        almanac_categories = file.read().split("\n\n")

        categories = [
            parse_almanac_category(category) for category in almanac_categories
        ]

        seeds = categories.pop(0)[1].pop()

        categories.reverse()

        starting_range = list(filter(lambda map: map[0] == 0, categories[0][1])).pop()
        pprint(
            find_destination_range_fit(
                [starting_range[0], starting_range[2]], categories[0]
            )
        )

        range_in_process = [starting_range[0], starting_range[2]]
        for category in categories:
            range_in_process = find_destination_range_fit(range_in_process, category)
            pprint(range_in_process)

        # This still needs to be run through `get_seed_location()`
        return get_lowest_available_seed_number_in_range(range_in_process, seeds)


def find_destination_range_fit(
    desired_range: list[int], category: tuple[str, list[list[int]]]
):
    desired_range_start, desired_range_length = desired_range

    for map in category[1]:
        map_dest_start, map_input_start, map_length = map

        if not desired_range_start in range(
            map_dest_start, map_dest_start + map_length
        ):
            continue

        return [
            desired_range_start + map_input_start - map_dest_start,
            desired_range_length if desired_range_length <= map_length else map_length,
        ]

    # This should actually output the desired map_dest_start
    # with a range that doesn't clip into existing ranges
    # raise Exception(f"Could not find destination range fit in {category[0]}. range {desired_range}")

    # This probably shouldn't work, but let's see what happens
    return desired_range


def get_lowest_available_seed_number_in_range(desired_range, seeds):
    desired_range_start, desired_range_len = desired_range
    desired_range_end = desired_range_start + desired_range_len

    for seed_range_start, seed_range_len in list(zip(seeds[::2], seeds[1::2])):
        seed_range_end = seed_range_start + seed_range_len
        if desired_range_start > seed_range_end:
            continue

        if desired_range_end < seed_range_start:
            continue

        if desired_range_start in range(seed_range_start, seed_range_end):
            return desired_range_start

        return seed_range_start


# ---------------------------------------------------------------------------- #
#                                  Shared code                                 #
# ---------------------------------------------------------------------------- #


def parse_almanac_category(category: str):
    category_name, category_content = category.split(":")
    return (
        category_name.strip(),
        [
            [int(map_part) for map_part in map.split()]
            for map in category_content.strip().split("\n")
        ],
    )


def get_seed_location(seed, categories: list[list[list[int]]]) -> int:
    input_val = int(seed)
    for category in categories:
        input_val = map_value_with_almanac_category(input_val, category)

    return input_val


def map_value_with_almanac_category(input_val: int, category: list[list[int]]) -> int:
    for map in category:
        dest_range_start, source_range_start, range_len = map

        value_in_range = (
            input_val >= source_range_start
            and input_val <= source_range_start + range_len
        )
        if not value_in_range:
            continue

        return input_val + dest_range_start - source_range_start

    return input_val
