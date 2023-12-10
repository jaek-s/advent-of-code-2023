from rich import print


def puzzle1(input: str):
    return sum(
        [
            find_next_sequence_value(list(map(int, line.split())))
            for line in input.splitlines()
        ]
    )


def find_next_sequence_value(sequence: list[int]):
    next_val = 0
    difference_lists = list(reversed(build_sequence_difference_list(sequence)))

    for i in range(0, len(difference_lists)):
        current_list = difference_lists[i]

        try:
            next_list = difference_lists[i + 1]
        except IndexError:
            continue

        next_val = current_list[-1] + next_list[-1]
        next_list.append(next_val)

    return next_val


def build_sequence_difference_list(sequence: list[int]) -> list[list[int]]:
    sequence_differences = [sequence]
    current_sequence = sequence

    while not all([datum == 0 for datum in current_sequence]):
        current_sequence = calculate_differences(current_sequence)
        sequence_differences.append(current_sequence)

    return sequence_differences


def calculate_differences(sequence: list[int]) -> list[int]:
    differences = []

    for i, datum in enumerate(sequence):
        try:
            next_datum = sequence[i + 1]
        except IndexError:
            continue

        differences.append(next_datum - datum)

    return differences
