from pprint import pprint

from rich import print

from helpers import open_input

# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #


def puzzle1():
    with open_input("05") as file:
        seeds, *almanac_categories = file.read().split("\n\n")

        seeds = list(map(int, seeds.split(":").pop().split()))

        categories = [
            parse_almanac_category(category) for category in almanac_categories
        ]

        locations = [get_seed_location(seed, categories) for seed in seeds]

    return min(locations)


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


# I could not for the life of me figure this one out.
# Credit goes to this youtube video: https://www.youtube.com/watch?v=NmxHw_bHhGM
def puzzle2():
    with open_input("05") as file:
        raw_seeds, *almanac_categories = file.read().split("\n\n")
        raw_seeds = list(map(int, raw_seeds.split(":")[1].split()))

        seeds = []

        for i in range(0, len(raw_seeds), 2):
            seeds.append((raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]))

        categories = [
            parse_almanac_category(category) for category in almanac_categories
        ]

        for category in categories:
            new_seeds = []

            while len(seeds) > 0:
                seeds_start, seeds_end = seeds.pop()

                for map_dest_start, map_input_start, map_len in category:
                    overlap_start = max(seeds_start, map_input_start)
                    overlap_end = min(seeds_end, map_input_start + map_len)

                    if overlap_start >= overlap_end:
                        continue

                    # I don't totally understand why we need to add map_input_start + map_dest_start
                    new_seeds.append(
                        (
                            overlap_start - map_input_start + map_dest_start,
                            overlap_end - map_input_start + map_dest_start,
                        )
                    )

                    if overlap_start > seeds_start:
                        seeds.append((seeds_start, overlap_start))

                    if seeds_end > overlap_end:
                        seeds.append((overlap_end, seeds_end))

                    break
                else:
                    new_seeds.append((seeds_start, seeds_end))
            seeds = new_seeds

        return min(seeds)[0]


# ---------------------------------------------------------------------------- #
#                                  Shared code                                 #
# ---------------------------------------------------------------------------- #


def parse_almanac_category(category: str):
    return [list(map(int, cat_map.split())) for cat_map in category.splitlines()[1:]]


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
