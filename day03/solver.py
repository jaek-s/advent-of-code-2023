import re

match_digits = re.compile(r"\d+")  # match any amount of digits


def get_input_lines_with_next_and_prev(input: str):
    lines = input.strip().split("\n")

    for index in range(0, len(lines)):
        current_line = lines[index]
        prev_line = lines[index - 1] if index > 0 else ""
        next_line = lines[index + 1] if index < len(lines) - 1 else ""

        yield current_line, prev_line, next_line


# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #


match_symbols = re.compile(r"[^\d\.]")  # match anything other than a digit or a period


def puzzle1(input: str):
    sum = 0

    for current_line, prev_line, next_line in get_input_lines_with_next_and_prev(input):
        sum += get_part_num_sum_for_line(current_line, prev_line, next_line)

    return sum


def get_part_num_sum_for_line(current_line: str, prev_line: str, next_line: str):
    sum = 0

    for match in match_digits.finditer(current_line):
        match_start, match_end = match.span()

        search_start = match_start - 1 if match_start > 0 else 0
        search_end = (
            match_end + 1 if match_end < len(current_line) else len(current_line)
        )

        if (
            match_symbols.search(current_line[search_start])
            or match_symbols.search(current_line[search_end - 1])
            or (
                match_symbols.search(prev_line, search_start, search_end)
                if prev_line
                else False
            )
            or (
                match_symbols.search(next_line, search_start, search_end)
                if next_line
                else False
            )
        ):
            sum += int(match[0])

    return sum


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


match_gears = re.compile(r"\*")
match_part_number_at_end = re.compile(r"\d+$")
match_part_number_at_start = re.compile(r"^\d+")
match_non_digits = re.compile(r"[^\d]")


def puzzle2(input: str):
    sum = 0

    for current_line, prev_line, next_line in get_input_lines_with_next_and_prev(input):
        sum += get_gear_ratio_sum_for_line(current_line, prev_line, next_line)

    return sum


def get_gear_ratio_sum_for_line(current_line: str, prev_line: str, next_line: str):
    sum = 0

    for match in match_gears.finditer(current_line):
        match_start, match_end = match.span()
        part_nums = []

        left_of_match = current_line[:match_start]
        part_on_left = match_part_number_at_end.search(left_of_match)

        if part_on_left:
            part_nums.append(part_on_left[0])

        right_of_match = current_line[match_end:]
        part_on_right = match_part_number_at_start.search(right_of_match)

        if part_on_right:
            part_nums.append(part_on_right[0])

        part_nums += get_parts_above_or_below(prev_line, match_start)
        part_nums += get_parts_above_or_below(next_line, match_start)

        # two number matches need to be found or else continue
        if len(part_nums) != 2:
            continue

        sum += int(part_nums[0]) * int(part_nums[1])

    return sum


def get_parts_above_or_below(line: str, gear_position: int) -> list[str]:
    part_numbers_string = line[gear_position : gear_position + 1]

    left_half = line[:gear_position]
    left_match = match_part_number_at_end.search(left_half)

    if left_match:
        part_numbers_string = f"{left_match[0]}{part_numbers_string}"

    right_half = line[gear_position + 1 :]
    right_match = match_part_number_at_start.search(right_half)

    if right_match:
        part_numbers_string = f"{part_numbers_string}{right_match[0]}"

    return [part for part in match_non_digits.split(part_numbers_string) if part]
