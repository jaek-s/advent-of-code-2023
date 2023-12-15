from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

CHAR_TO_VALID_DIRECTIONS = {
    "S": (Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)),
    "-": (Point(1, 0), Point(-1, 0)),
    "|": (Point(0, 1), Point(0, -1)),
    "L": (Point(0, 1), Point(1, 0)),
    "J": (Point(0, 1), Point(-1, 0)),
    "7": (Point(0, -1), Point(-1, 0)),
    "F": (Point(1, 0), Point(0, -1)),
    ".": (),
}


def puzzle1(input: str):
    max_steps = 1
    pipe_map, starting_coord = parse_input(input)

    prev_left_ptr = starting_coord
    left_ptr = find_next_coord(pipe_map, curr_coord=starting_coord)

    prev_right_ptr = starting_coord
    right_ptr = find_next_coord(
        pipe_map, curr_coord=starting_coord, prev_coord=left_ptr
    )

    while left_ptr != right_ptr:
        max_steps += 1

        next_left_ptr = find_next_coord(
            pipe_map=pipe_map, curr_coord=left_ptr, prev_coord=prev_left_ptr
        )
        prev_left_ptr = left_ptr
        left_ptr = next_left_ptr

        next_right_ptr = find_next_coord(
            pipe_map=pipe_map, curr_coord=right_ptr, prev_coord=prev_right_ptr
        )
        prev_right_ptr = right_ptr
        right_ptr = next_right_ptr

    return max_steps


def parse_input(input: str):
    starting_coord = None

    lines = input.splitlines()
    pipe_map = [[] for _ in lines[0]]
    for y, line in enumerate(reversed(lines)):
        for x, char in enumerate(line):
            pipe_map[x].append(char)

            if char == "S":
                starting_coord = Point(x, y)

    if not starting_coord:
        raise ValueError("Input does not contain a starting point.")

    return pipe_map, starting_coord


def find_next_coord(
    pipe_map: list[list[int]], curr_coord: Point, prev_coord: Point | None = None
) -> Point:
    curr_char = get_map_char(pipe_map, curr_coord)
    valid_moves = CHAR_TO_VALID_DIRECTIONS[curr_char]

    for move in valid_moves:
        next_coord = Point(x=curr_coord.x + move.x, y=curr_coord.y + move.y)

        if next_coord == prev_coord or not is_valid_move(
            pipe_map, curr_coord, next_coord
        ):
            continue

        return next_coord

    raise Exception("Unable to compute the next coord")


def is_valid_move(
    pipe_map: list[list[int]], curr_coord: Point, next_coord: Point
) -> bool:
    try:
        next_char = get_map_char(pipe_map, next_coord)
    except IndexError:
        return False

    valid_moves = CHAR_TO_VALID_DIRECTIONS[next_char]

    for move in valid_moves:
        prev_coord = Point(x=next_coord.x + move.x, y=next_coord.y + move.y)
        if prev_coord == curr_coord:
            return True

    return False


def get_map_char(pipe_map: list[list[int]], coord: Point):
    return pipe_map[coord.x][coord.y]
