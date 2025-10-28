"""
Flower Field is a compassionate reimagining of the popular game Minesweeper.

This module provides helpers to validate and annotate a rectangular garden
representation, where each row is a string comprised of spaces and ``*``
characters. A ``*`` denotes a flower; a space denotes an empty square.

The goal is to compute numeric hints indicating how many flowers are
directly adjacent (horizontally, vertically, diagonally) to each square.
"""


def annotate(garden: list) -> list:
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
    :rtype: list
    :raises ValueError: If the garden is non-rectangular or contains
                        invalid characters.
    """
    # empty list
    if not garden:
        return []

    # when the board receives malformed input
    if not _is_garden_valid(garden):
        raise ValueError("The board is invalid with current input.")

    for i_row, row in enumerate(garden):
        for i_col, char in enumerate(row):
            if char == " ":
                flower_count: int = 0
                flower_count += _calc_flower_top(i_row, i_col, garden)
                flower_count += _calc_flower_bottom(i_row, i_col, garden)
                flower_count += _calc_flower_left(i_row, i_col, garden)
                flower_count += _calc_flower_right(i_row, i_col, garden)

                if flower_count != 0:
                    garden[i_row] = (
                        garden[i_row][:i_col]
                        + str(flower_count)
                        + garden[i_row][i_col + 1:]
                    )
    return garden


def _calc_flower_left(i_row: int, i_col: int, garden: list) -> int:
    """
    Count contiguous flowers to the left of the current position.

    Scans leftward from ``(i_row, i_col - 1)`` until a non-flower character is
    found or the row boundary is reached.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: Number of adjacent ``*`` cells to the left.
    :rtype: int
    """
    flower_count: int = 0

    if i_col - 1 >= 0:
        for char in garden[i_row][:i_col][::-1]:
            if char == "*":
                flower_count += 1
            else:
                break
    return flower_count


def _calc_flower_right(i_row: int, i_col: int, garden: list) -> int:
    """
    Count contiguous flowers to the right of the current position.

    Scans rightward from ``(i_row, i_col + 1)`` until a non-flower character is
    found or the row boundary is reached.

    :param int i_row: Current row index.
    :param int i_col: Current column index.
    :param list garden: The garden as a list of strings.
    :returns: Number of adjacent ``*`` cells to the right.
    :rtype: int
    """
    flower_count: int = 0

    if i_col + 1 < len(garden[i_row]):
        for char in garden[i_row][i_col + 1:]:
            if char == "*":
                flower_count += 1
            else:
                break
    return flower_count


def _calc_flower_top(i_row: int, i_col: int, garden: list) -> int:
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

    flower_count: int = 0

    if i_row - 1 >= 0 and "*" in garden[i_row - 1]:
        # top-left
        if i_col > 0 and garden[i_row - 1][i_col - 1] == "*":
            flower_count += 1
        # top
        if garden[i_row - 1][i_col] == "*":
            flower_count += 1
        # top-right
        if (
            i_col + 1 < len(garden[i_row])
            and garden[i_row - 1][i_col + 1] == "*"
        ):
            flower_count += 1
    return flower_count


def _calc_flower_bottom(i_row: int, i_col: int, garden: list) -> int:
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

    flower_count: int = 0

    if i_row + 1 < len(garden) and "*" in garden[i_row + 1]:
        # bottom-left
        if i_col > 0 and garden[i_row + 1][i_col - 1] == "*":
            flower_count += 1
        # bottom
        if garden[i_row + 1][i_col] == "*":
            flower_count += 1
        # bottom-right
        if (
            i_col + 1 < len(garden[i_row])
            and garden[i_row + 1][i_col + 1] == "*"
        ):
            flower_count += 1
    return flower_count


def _is_garden_valid(garden: list) -> bool:
    """
    Check whether the garden input is a valid rectangular board.

    A garden is considered valid when all rows have the same length and only
    contain spaces or ``*`` characters.

    :param list garden: Candidate garden as a list of strings.
    :returns: ``True`` if the input is rectangular and uses only valid
              characters; otherwise ``False``.
    :rtype: bool
    """

    garden_length: int = len(garden[0])
    # when the board receives malformed input
    for row in garden:
        # garden is not a rectangle due to inconsistent row length
        if len(row) != garden_length:
            return False
        # contains invalid chars inside row
        valid_chars: bool = all(char in " *" for char in row)
        if not valid_chars:
            return False
    return True
