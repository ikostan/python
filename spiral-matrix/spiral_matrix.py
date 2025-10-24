"""
Generate a square spiral matrix.

The matrix is filled with natural numbers starting at 1 in the top-left
corner and increasing in an inward, clockwise spiral order.

This module exposes a public function to build the spiral and some
internal helpers used to track direction and position.
"""

DIRECTIONS: dict = {
    "right": {"row": 0, "col": 1},
    "left": {"row": 0, "col": -1},
    "up": {"row": -1, "col": 0},
    "down": {"row": 1, "col": 0},
}


def spiral_matrix(size: int) -> list:
    """
    Build a square matrix filled in clockwise spiral order.

    :param size: The dimension of the square matrix to generate. Must be a
                 non-negative integer. A size of 0 returns an empty list.
    :return: A two-dimensional list representing the spiral matrix of shape
            ``size x size``. Each cell contains a natural number starting at
            1 and increasing as the spiral proceeds clockwise inward.
    """
    # Set initial data
    result: list = [[0] * size for i in range(size)]
    num: int = 1
    max_num: int = size * size
    direction: str = "right"
    x_y: list = [0, 0]

    # Create a square matrix
    while num <= max_num:
        result[x_y[0]][x_y[1]] = num
        direction = _set_direction(direction, result, x_y, size)
        x_y[0] += DIRECTIONS[direction]["row"]
        x_y[1] += DIRECTIONS[direction]["col"]
        num += 1

    return result


def _set_direction(direction: str, result: list, x_y: list, size: int) -> str:
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
    if direction == "right":
        if col + 1 < size and result[row][col + 1] == 0:
            direction = "right"
        else:
            direction = "down"
    elif direction == "down":
        if row + 1 < size and result[row + 1][col] == 0:
            direction = "down"
        else:
            direction = "left"
    elif direction == "up":
        if row - 1 >= 0 and result[row - 1][col] == 0:
            direction = "up"
        else:
            direction = "right"
    elif direction == "left":
        if col - 1 >= 0 and result[row][col - 1] == 0:
            direction = "left"
        else:
            direction = "up"

    return direction
