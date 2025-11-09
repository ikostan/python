"""
Flower Field is a compassionate reimagining of the popular game Minesweeper.

This module provides helpers to validate and annotate a rectangular garden
representation, where each row is a string comprised of spaces and ``*``
characters. A ``*`` denotes a flower; a space denotes an empty square.

The goal is to compute numeric hints indicating how many flowers are
adjacent (horizontally, vertically, diagonally) to each square.
"""


def annotate(garden: list[str]) -> list[str]:
    """
    Annotate a garden with counts of adjacent flowers.

    Expects a rectangular list of strings containing only spaces and ``*``.
    Validation errors raise a :class:`ValueError`.

    :param list garden: A list of equal-length strings representing the garden.
        ``*`` marks a flower; space marks empty.
    :returns: An annotated garden of the same shape. Empty squares are
        replaced by digits (``"1"``–``"8"``) when adjacent to flowers;
        squares with zero adjacent flowers remain spaces. Flowers
        (``*``) are preserved.
    :rtype: list[str]
    :raises ValueError: If the garden is non-rectangular or contains
        invalid characters.
    """
    # empty list
    if not garden:
        return []

    # raise an error when the board receives malformed input
    _validate(garden)

    new_garden: list[str] = garden.copy()
    for i_row, row in enumerate(new_garden):
        for i_col, char in enumerate(row):
            if char == " ":
                flower_count = 0
                flower_count += _calc_surrounding_flowers(i_row, i_col, new_garden)

                if flower_count != 0:
                    new_garden[i_row] = (
                        new_garden[i_row][:i_col]
                        + str(flower_count)
                        + new_garden[i_row][i_col + 1 :]
                    )

    return new_garden

def _calc_surrounding_flowers(i_row: int, i_col: int, garden: list[str]) -> int:
    total: int = 0

    if i_col - 1 >= 0 and garden[i_row][i_col - 1] == "*":
        total += 1

    if i_col + 1 < len(garden[i_row]) and garden[i_row][i_col + 1] == "*":
        total += 1

    if i_row - 1 >= 0 and "*" in garden[i_row - 1]:
        if i_col > 0 and garden[i_row - 1][i_col - 1] == "*":
            total += 1
        if garden[i_row - 1][i_col] == "*":
            total += 1
        if i_col + 1 < len(garden[i_row]) and garden[i_row - 1][i_col + 1] == "*":
            total += 1

    if i_row + 1 < len(garden) and "*" in garden[i_row + 1]:
        if i_col > 0 and garden[i_row + 1][i_col - 1] == "*":
            total += 1
        if garden[i_row + 1][i_col] == "*":
            total += 1
        if i_col + 1 < len(garden[i_row]) and garden[i_row + 1][i_col + 1] == "*":
            total += 1

    return total


def _validate(garden: list[str]):
    """
    Validate the garden shape and contents.

    Ensures the input is rectangular and contains only spaces and ``*``.

    :param list garden: A list of equal-length strings to validate.
    :raises ValueError: If rows have differing lengths or contain characters
        other than space or ``*``.
    """
    garden_length = len(garden[0])
    for row in garden:
        # when the board receives malformed input
        # garden is not a rectangle due to inconsistent row length
        # or contains invalid chars inside the row
        if len(row) != garden_length or not all(char in " *" for char in row):
            raise ValueError("The board is invalid with current input.")
