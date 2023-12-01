import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))

regex_get_first_digit = re.compile("^.*?(\\d)")

def solve_puzzle():
    sum = 0
    with open(current_dir + "/input.txt") as file:
        for line in file.readlines():
            stripped = line.strip()
            reversed = stripped[::-1]
            first_digit_match = regex_get_first_digit.match(stripped)
            last_digit_match = regex_get_first_digit.match(reversed)

            if not first_digit_match or not last_digit_match:
                continue

            line_digits = int(f"{first_digit_match.group(1)}{last_digit_match.group(1)}")
            sum += line_digits

    return sum

if __name__ == "__main__":
    print(solve_puzzle())
