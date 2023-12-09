from functools import reduce

from rich import print

from helpers import open_input


def puzzle1():
    error_margins = []
    with open_input("06") as file:
        times, distances = file.read().splitlines()

        races = zip(
            list(map(int, times.split()[1:])), list(map(int, distances.split()[1:]))
        )

        for race in races:
            min_hold, max_hold = find_min_and_max_hold_times(race)
            error_margins.append(max_hold - min_hold + 1)

    return reduce(lambda x, y: x * y, error_margins)


def puzzle2():
    with open_input("06") as file:
        time, distance = file.read().splitlines()
        time = int(time.split(":")[1:].pop().replace(" ", ""))
        distance = int(distance.split(":")[1:].pop().replace(" ", ""))

        min_hold, max_hold = find_min_and_max_hold_times((time, distance))

        return max_hold - min_hold + 1


def find_min_and_max_hold_times(race: tuple[int, int]) -> tuple[int, int]:
    race_time, record = race

    min_hold = 0
    for hold_time in range(0, race_time + 1):
        travel_distance = hold_time * (race_time - hold_time)

        if travel_distance > record:
            min_hold = hold_time
            break

    max_hold = race_time
    for hold_time in reversed(range(0, race_time + 1)):
        travel_distance = hold_time * (race_time - hold_time)

        if travel_distance > record:
            max_hold = hold_time
            break

    return (min_hold, max_hold)
