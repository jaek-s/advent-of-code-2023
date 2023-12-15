from collections import namedtuple

from rich import print, reconfigure

Point = namedtuple("Point", ["x", "y"])

CHAR_TO_VALID_DIRECTIONS = {
    "S": (Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)),
    "-": (Point(1, 0), Point(-1, 0)),
    "|": (Point(0, 1), Point(0, -1)),
    "L": (Point(0, -1), Point(1, 0)),
    "J": (Point(0, -1), Point(-1, 0)),
    "7": (Point(0, 1), Point(-1, 0)),
    "F": (Point(1, 0), Point(0, 1)),
    ".": (),
}


def puzzle1(input: str):
    return find_the_loop(input)[0]


def puzzle2(input: str):
    """
    I used help from reddit to get a good direction for this puzzle.
    """
    _, loop_coords, _ = find_the_loop(input, print_loop=True)

    loop_area = calc_area(loop_coords)

    # Use Pick's theorem to calculate the number of interior sections
    return int(loop_area + 1 - (len(loop_coords)/2))

def calc_area(loop_coords: list[Point]):
    """
    Use the shoelace method to calculate the total area enclosed by the pipe
    """
    area_doubled = 0

    for i, coord in enumerate(loop_coords):
        try:
            next_coords = loop_coords[i + 1]
        except IndexError:
            next_coords = loop_coords[0]


        area_doubled += (coord.x * next_coords.y) - (coord.y * next_coords.x)

    return area_doubled/2

def find_the_loop(input: str, print_loop: bool = False):
    pipe_map, starting_coord = parse_input(input)

    max_steps = 1
    loop_coords = [starting_coord]

    prev_left_ptr = starting_coord
    left_ptr = find_next_coord(pipe_map, curr_coord=starting_coord)

    prev_right_ptr = starting_coord
    right_ptr = find_next_coord(
        pipe_map, curr_coord=starting_coord, prev_coord=left_ptr
    )

    while left_ptr != right_ptr:
        max_steps += 1

        loop_coords.insert(0, left_ptr)
        next_left_ptr = find_next_coord(
            pipe_map=pipe_map, curr_coord=left_ptr, prev_coord=prev_left_ptr
        )
        prev_left_ptr = left_ptr
        left_ptr = next_left_ptr

        loop_coords.append(right_ptr)
        next_right_ptr = find_next_coord(
            pipe_map=pipe_map, curr_coord=right_ptr, prev_coord=prev_right_ptr
        )
        prev_right_ptr = right_ptr
        right_ptr = next_right_ptr

    loop_coords.append(right_ptr)

    if print_loop:
        output = [""]*len(pipe_map)
        for x, col in enumerate(pipe_map):
            for y, cell in enumerate(col):
                this_cell = Point(x, y)
                if this_cell in loop_coords:
                    output[y] += f"[bold green]{cell}[/bold green]"
                    continue

                output[y] += cell

        reconfigure(highlight=False)
        for line in output:
            print(line)

    return max_steps, loop_coords, pipe_map


def parse_input(input: str):
    starting_coord = None

    lines = input.splitlines()
    pipe_map = [[] for _ in lines[0]]
    for y, line in enumerate(lines):
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
