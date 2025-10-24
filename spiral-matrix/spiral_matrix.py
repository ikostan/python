"""
Generate a square spiral matrix.

The matrix is filled with natural numbers starting at 1 in the top-left
corner and increasing in an inward, clockwise spiral order.

This module exposes a public function to build the spiral and some
internal helpers used to track direction and position.
"""

DIRECTIONS: dict = {
    "right": {"row": 0, "col": 1, "next_direction": "down"},
    "left": {"row": 0, "col": -1, "next_direction": "up"},
    "up": {"row": -1, "col": 0, "next_direction": "right"},
    "down": {"row": 1, "col": 0, "next_direction": "left"},
}


def spiral_matrix(size: int) -> list[list[int]]:
    """
    Build a square matrix filled in clockwise spiral order.

    :param size: The dimension of the square matrix to generate. Must be a
                 non-negative integer. A size of 0 returns an empty list.
    :return: A two-dimensional list representing the spiral matrix of shape
            ``size x size``. Each cell contains a natural number starting at
            1 and increasing as the spiral proceeds clockwise inward.
    """
    if size < 0:
        raise ValueError("Matrix size must be non-negative")
    # Set initial data
    result: list = [[0] * size for _ in range(size)]
    num: int = 1
    max_num: int = size * size
    direction: str = "right"
    x_y: list[int] = [0, 0]

    # Create a square matrix
    while num <= max_num:
        result[x_y[0]][x_y[1]] = num
        direction = _set_direction(direction, result, x_y, size)
        x_y[0] += DIRECTIONS[direction]["row"]
        x_y[1] += DIRECTIONS[direction]["col"]
        num += 1

    return result


def _set_direction(
    direction: str, result: list[list[int]], x_y: list[int], size: int
) -> str:
    """
    Determine the next movement direction based on bounds and visited cells.

    :param direction: next direction, one of {"right", "left", "up", "down"}.
    :param result: The current matrix being filled.
    :param x_y: Current coordinates as [row, col].
    :param size: Dimension of the square matrix.
    :return: The direction to move next so that the spiral proceeds without
             leaving bounds or revisiting filled cells.
    """
    row, col = x_y
    if direction == "right" and not (
        col + 1 < size and result[row][col + 1] == 0
    ):
        direction = DIRECTIONS[direction]["next_direction"]
    elif direction == "down" and not (
        row + 1 < size and result[row + 1][col] == 0
    ):
        direction = DIRECTIONS[direction]["next_direction"]
    elif direction == "up" and not (
        row - 1 >= 0 and result[row - 1][col] == 0
    ):
        direction = DIRECTIONS[direction]["next_direction"]
    elif direction == "left" and not (
        col - 1 >= 0 and result[row][col - 1] == 0
    ):
        direction = DIRECTIONS[direction]["next_direction"]

    return direction
