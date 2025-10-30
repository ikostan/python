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
                flower_count += _calc_flower_top(i_row, i_col, new_garden)
                flower_count += _calc_flower_bottom(i_row, i_col, new_garden)
                flower_count += _calc_flower_left(i_row, i_col, new_garden)
                flower_count += _calc_flower_right(i_row, i_col, new_garden)

                if flower_count != 0:
                    new_garden[i_row] = (
                        new_garden[i_row][:i_col]
                        + str(flower_count)
                        + new_garden[i_row][i_col + 1 :]
                    )

    return new_garden


def _calc_flower_left(i_row: int, i_col: int, garden: list[str]) -> int:
    """
    Check for a flower immediately to the left of the current position.

    This helper only inspects the single neighbor at ``(i_row, i_col - 1)``
    and returns 1 if it contains ``*``; otherwise returns 0.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: 1 if the left neighbor is a flower; otherwise 0.
    :rtype: int
    """
    if i_col - 1 >= 0 and garden[i_row][i_col - 1] == "*":
        return 1

    return 0


def _calc_flower_right(i_row: int, i_col: int, garden: list[str]) -> int:
    """
    Check for a flower immediately to the right of the current position.

    This helper only inspects the single neighbor at ``(i_row, i_col + 1)``
    and returns 1 if it contains ``*``; otherwise returns 0.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: 1 if the right neighbor is a flower; otherwise 0.
    :rtype: int
    """
    if i_col + 1 < len(garden[i_row]) and garden[i_row][i_col + 1] == "*":
        return 1

    return 0


def _calc_flower_top(i_row: int, i_col: int, garden: list[str]) -> int:
    """
    Count flowers in the three cells directly above the current position.

    Checks the top-left, top, and top-right neighbors when the row above
    exists and contains any flowers.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: Number of ``*`` cells among the three upper neighbors.
    :rtype: int
    """
    flower_count = 0

    if i_row - 1 >= 0 and "*" in garden[i_row - 1]:
        # top-left
        if i_col > 0 and garden[i_row - 1][i_col - 1] == "*":
            flower_count += 1
        # top
        if garden[i_row - 1][i_col] == "*":
            flower_count += 1
        # top-right
        if i_col + 1 < len(garden[i_row]) and garden[i_row - 1][i_col + 1] == "*":
            flower_count += 1
    return flower_count


def _calc_flower_bottom(i_row: int, i_col: int, garden: list[str]) -> int:
    """
    Count flowers in the three cells directly below the current position.

    Checks the bottom-left, bottom, and bottom-right neighbors when the row
    below exists and contains any flowers.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: Number of ``*`` cells among the three lower neighbors.
    :rtype: int
    """
    flower_count = 0

    if i_row + 1 < len(garden) and "*" in garden[i_row + 1]:
        # bottom-left
        if i_col > 0 and garden[i_row + 1][i_col - 1] == "*":
            flower_count += 1
        # bottom
        if garden[i_row + 1][i_col] == "*":
            flower_count += 1
        # bottom-right
        if i_col + 1 < len(garden[i_row]) and garden[i_row + 1][i_col + 1] == "*":
            flower_count += 1
    return flower_count


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
