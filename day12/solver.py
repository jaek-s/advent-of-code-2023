from functools import lru_cache


def puzzle1(input: str):
    sum = 0

    for line in input.splitlines():
        springs, notes = line.split()
        notes = tuple(map(int, notes.split(",")))
        sum += count(springs, notes)

    return sum


def puzzle2(input: str):
    sum = 0

    for line in input.splitlines():
        springs, notes = line.split()
        springs = "?".join([springs] * 5)
        notes = tuple(map(int, ",".join([notes] * 5).split(",")))
        sum += count(springs, notes)

    return sum


@lru_cache
def count(springs: str, notes: tuple):
    """
    This solution was borrowed from here: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day12p1.py
    """

    if springs == "":
        return 1 if notes == () else 0

    if notes == ():
        return 0 if "#" in springs else 1

    result = 0

    first_spring = springs[0]
    if first_spring in ".?":
        result += count(springs[1:], notes)

    if first_spring not in "#?":
        return result

    next_broken_run_len = notes[0]

    broken_spring_run_fits_remaining_springs = next_broken_run_len <= len(springs)
    if not broken_spring_run_fits_remaining_springs:
        return result

    next_spot_for_run_is_continuous = "." not in springs[:next_broken_run_len]
    run_actually_ends = (
        next_broken_run_len == len(springs) or springs[next_broken_run_len] != "#"
    )

    if next_spot_for_run_is_continuous and run_actually_ends:
        result += count(springs[next_broken_run_len + 1 :], notes[1:])

    return result
