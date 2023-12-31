from dataclasses import dataclass
from functools import cached_property


@dataclass
class ParsedCard:
    index: int
    winning_numbers: list[int]
    numbers_you_have: list[int]

    @cached_property
    def match_count(self) -> int:
        match_count = 0

        for winning_number in self.winning_numbers:
            match_count += 1 if winning_number in self.numbers_you_have else 0

        return match_count

    @classmethod
    def parse(cls, card: str):
        index, numbers = card.split(": ")

        index = int(index.replace("Card", "").strip())

        winning_numbers, numbers_you_have = numbers.split("|")

        winning_numbers = parse_number_str(winning_numbers)
        numbers_you_have = parse_number_str(numbers_you_have)

        return cls(index, winning_numbers, numbers_you_have)


def parse_number_str(number_str: str) -> list[int]:
    return [int(number.strip()) for number in number_str.split(" ") if number != ""]


# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #


def puzzle1(input: str):
    sum = 0

    for line in input.splitlines():
        sum += get_card_value(line)

    return sum


def get_card_value(card: str) -> int:
    parsed_card = ParsedCard.parse(card)

    match_count = parsed_card.match_count

    if match_count == 0:
        return 0

    return 2 ** (match_count - 1)


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


def puzzle2(input: str):
    cards = build_card_list(input)
    return calculate_winnings(cards, 0, len(cards))


def build_card_list(input: str):
    card_list = []

    for line in input.splitlines():
        card_list.append(ParsedCard.parse(line))

    return card_list


def calculate_winnings(cards: list[ParsedCard], start: int, end: int):
    sum = 0
    for card in cards[start:end]:
        sum += 1
        match_count = card.match_count

        if not match_count:
            continue

        sum += calculate_winnings(cards, card.index, card.index + match_count)

    return sum
