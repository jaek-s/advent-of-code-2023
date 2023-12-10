from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from functools import reduce


def puzzle1(input: str):
    rounds = []
    for hand_and_bid in input.splitlines():
        hand, bid = hand_and_bid.split()
        rounds.append(Round(hand=hand, bid=int(bid)))

    answer = 0
    for position, round in enumerate(sorted(rounds)):
        answer += round.bid * (position + 1)

    return answer

def puzzle2(input: str):
    rounds = []
    for hand_and_bid in input.splitlines():
        hand, bid = hand_and_bid.split()
        rounds.append(Part2Round(hand=hand, bid=int(bid)))

    answer = 0
    for position, round in enumerate(sorted(rounds)):
        answer += round.bid * (position + 1)

    return answer

ALPHA_CARD_VALUE = dict(
    T=10,
    J=11,
    Q=12,
    K=13,
    A=14,
)

@dataclass
class Round:
    hand: str
    bid: int

    @property
    def card_counts(self):
        hand_dict = defaultdict(lambda: 0)
        for char in self.hand:
            hand_dict[char] += 1

        return hand_dict

    @property
    def hand_value(self):
        counts = list(reversed(sorted(self.card_counts.values())))


        # 5 of a kind, highest of 7 possible hands
        if counts[0] == 5:
            return 7

        # 4 of a kind
        if counts[0] == 4:
            return 6

        # full house
        if counts[0] == 3 and counts[1] == 2:
            return 5

        # 3 of a kind
        if counts[0] == 3 and counts[1] == 1:
            return 4

        # 2 pair
        if counts[0] == 2 and counts[1] == 2:
            return 3

        # 1 pair
        if counts[0] == 2:
            return 2

        return 1

    @property
    def sort_key(self):
        key = [self.hand_value]

        for char in self.hand:
            if char not in ALPHA_CARD_VALUE.keys():
                key.append(int(char))
                continue

            key.append(ALPHA_CARD_VALUE[char])

        return key

    def __lt__(self, other):
        return self.sort_key < other.sort_key

class Part2Round(Round):
    @property
    def hand_value(self):
        joker_count = self.card_counts["J"]
        self.card_counts["J"] = 0

        card_counts = copy(self.card_counts)
        card_counts["J"] = 0


        counts = list(reversed(sorted(card_counts.values())))
        counts[0] += joker_count


        # 5 of a kind, highest of 7 possible hands
        if counts[0] == 5:
            return 7

        # 4 of a kind
        if counts[0] == 4:
            return 6

        # full house
        if counts[0] == 3 and counts[1] == 2:
            return 5

        # 3 of a kind
        if counts[0] == 3 and counts[1] == 1:
            return 4

        # 2 pair
        if counts[0] == 2 and counts[1] == 2:
            return 3

        # 1 pair
        if counts[0] == 2:
            return 2

        return 1

    @property
    def sort_key(self):
        key = [self.hand_value]

        for char in self.hand:
            if char not in ALPHA_CARD_VALUE.keys():
                key.append(int(char))
                continue

            if char == "J":
                key.append(1)
                continue

            key.append(ALPHA_CARD_VALUE[char])

        return key

    def __lt__(self, other):
        return self.sort_key < other.sort_key
