import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))

regex_get_first_digit = re.compile("^.*?(\\d)")

NUMBER_STRINGS = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}

def replace_letter_digits(input: str):
    for (letter_digit, real_digit) in NUMBER_STRINGS.items():
        input = input.replace(letter_digit, real_digit)
    return input

def get_input_lines():
    with open(current_dir + "/input.txt") as file:
        for line in file.readlines():
            yield line.strip()

def get_calibration_value(line: str) -> int:
    first_digit_match = regex_get_first_digit.match(line)
    last_digit_match = regex_get_first_digit.match(line[::-1])

    if not first_digit_match or not last_digit_match:
        return 0

    return int(f"{first_digit_match.group(1)}{last_digit_match.group(1)}")


def solve_first_puzzle():
    sum = 0

    for line in get_input_lines():
        sum += get_calibration_value(line)

    return sum

def solve_second_puzzle():
    sum = 0

    for line in get_input_lines():
        converted_line = replace_letter_digits(line)
        sum += get_calibration_value(converted_line)

    return sum



if __name__ == "__main__":
    print(f"first puzzle solution: {solve_first_puzzle()}")
    print(f"second puzzle solution: {solve_second_puzzle()}")
