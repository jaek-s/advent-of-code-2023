from helpers import get_input_lines

def get_games_from_input():
    for line in get_input_lines("02"):
        game_id, game = line.split(": ")

        game_id = int(game_id.replace("Game ", ""))
        game = game.split("; ")

        yield game_id, game

# ---------------------------------------------------------------------------- #
#                                 first puzzle                                 #
# ---------------------------------------------------------------------------- #

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def game_is_possible(game: list[str]):
    for round in game:
        draws = round.split(", ")
        counts = {
            color: int(count) for (count, color) in [draw.split() for draw in draws]
        }

        if (
            counts.get("red", 0) > MAX_RED
            or counts.get("green", 0) > MAX_GREEN
            or counts.get("blue", 0) > MAX_BLUE
        ):
            return False

    return True


def solve_first_puzzle():
    sum = 0
    for (game_id, game) in get_games_from_input():

        if not game_is_possible(game):
            continue

        sum += game_id

    return sum


# ---------------------------------------------------------------------------- #
#                                 second puzzle                                #
# ---------------------------------------------------------------------------- #



if __name__ == "__main__":
    print(f"first puzzle solution: {solve_first_puzzle()}")
    # print(f"second puzzle solution: {solve_second_puzzle()}")
