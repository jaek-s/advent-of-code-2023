import re

# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #

regex_get_first_digit = re.compile("^.*?(\\d)")


def get_calibration_value(line: str) -> int:
    first_digit_match = regex_get_first_digit.match(line)
    last_digit_match = regex_get_first_digit.match(line[::-1])

    if not first_digit_match or not last_digit_match:
        return 0

    return int(f"{first_digit_match.group(1)}{last_digit_match.group(1)}")


def puzzle1(input: str):
    sum = 0

    for line in input.splitlines():
        sum += get_calibration_value(line)

    return sum


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


NUMBER_STRINGS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

regex_match_first_digit_or_digit_string = re.compile(
    f"^.*?(\\d|{"|".join(NUMBER_STRINGS.keys())})"  # fmt: skip
)

regex_match_last_digit_or_digit_string = re.compile(
    f".*(\\d|{"|".join(NUMBER_STRINGS.keys())}).*?$"  # fmt: skip
)


def sanitize_digit(digit) -> int:
    if digit in NUMBER_STRINGS.keys():
        digit = NUMBER_STRINGS[digit]

    return int(digit)


def get_real_calibration_value(line: str) -> int:
    first_digit_match = regex_match_first_digit_or_digit_string.match(line)
    last_digit_match = regex_match_last_digit_or_digit_string.match(line)

    if not first_digit_match or not last_digit_match:
        return 0

    first_digit = sanitize_digit(first_digit_match.group(1))
    second_digit = sanitize_digit(last_digit_match.group(1))

    return int(f"{first_digit}{second_digit}")


def puzzle2(input: str):
    sum = 0
    for line in input.splitlines():
        sum += get_real_calibration_value(line)

    return sum
