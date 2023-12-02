from helpers import get_input_lines


def get_games_from_input() -> dict[int, list[dict[str, int]]]:
    parsed_games = {}
    for line in get_input_lines("02"):
        game_id, game = line.split(": ")

        game_id = int(game_id.replace("Game ", ""))

        # I'd probably be rasing my eyebrows if I saw a combination of list and dict comprehensions like this in production code.
        # It does make the code below a _little_ bit cleaner, though.

        # This gives a list of dicts that looks like [{ red: 1, green: 2, blue: 3}]
        game = [
            {
                color: int(count)
                for (count, color) in [draw.split() for draw in round.split(", ")]
            }
            for round in game.split("; ")
        ]

        parsed_games[game_id] = game

    return parsed_games


# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def game_is_possible(game: list[dict[str, int]]):
    for round in game:
        if (
            round.get("red", 0) > MAX_RED
            or round.get("green", 0) > MAX_GREEN
            or round.get("blue", 0) > MAX_BLUE
        ):
            return False

    return True


def solve_first_puzzle(games: dict[int, list[dict[str, int]]]):
    sum = 0
    for game_id, game in games.items():
        if not game_is_possible(game):
            continue

        sum += game_id

    return sum


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #


def get_power_of_min_set_of_cubes(game):
    red = 0
    green = 0
    blue = 0

    for round in game:
        if round.get("red", 0) > red:
            red = round.get("red", 0)
        if round.get("green", 0) > green:
            green = round.get("green", 0)
        if round.get("blue", 0) > blue:
            blue = round.get("blue", 0)

    return red * green * blue


def solve_second_puzzle(games: dict[int, list[dict[str, int]]]):
    sum = 0

    for game in games.values():
        sum += get_power_of_min_set_of_cubes(game)

    return sum


if __name__ == "__main__":
    games = get_games_from_input()
    print(f"first puzzle solution: {solve_first_puzzle(games)}")
    print(f"second puzzle solution: {solve_second_puzzle(games)}")
