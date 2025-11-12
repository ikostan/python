"""
Flower Field is a compassionate reimagining of the popular game Minesweeper.

This module provides helpers to validate and annotate a rectangular garden
representation, where each row is a string comprised of spaces and ``*``
characters. A ``*`` denotes a flower; a space denotes an empty square.

The goal is to compute numeric hints indicating how many flowers are
adjacent (horizontally, vertically, diagonally) to each square.
"""

# Relative offsets to the eight neighboring cells around a given position
COORDINATES: tuple[tuple[int, int]] = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


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
    return [
        "".join(
            str(count)
            if (count := _calc_surrounding_flowers(i_row, i_col, garden)) != 0
            else char
            for i_col, char in enumerate(row)
        )
        for i_row, row in enumerate(garden)
    ]


def _calc_surrounding_flowers(i_row: int, i_col: int, garden: list[str]) -> int:
    """
    Count flowers adjacent to the given cell.

    Counts the eight neighboring positions around ``(i_row, i_col)`` when the
    current cell is empty (space). If the cell itself is a flower (``*``), the
    count remains zero as the caller preserves flowers unchanged.

    :param int i_row: Row index of the target cell.
    :param int i_col: Column index of the target cell.
    :param list garden: The rectangular garden representation.
    :returns: Number of adjacent flowers (0–8).
    :rtype: int
    """
    total: list[int] = [0]
    # Only compute neighbors for empty squares; flowers are preserved by caller.
    if garden[i_row][i_col] == " ":
        # Count flowers all around current position
        total = [
            _process_cell(i_row, offset_row, i_col, offset_col, garden)
            for offset_row, offset_col in COORDINATES
        ]

    return sum(total)


def _process_cell(i_row, offset_row, i_col, offset_col, garden) -> int:
    """
    Return 1 if the neighbor at the given relative offset contains a flower.

    Computes the absolute coordinates from ``(i_row, i_col)`` and the provided
    offsets, performs bounds checking to avoid ``IndexError``, and returns ``1``
    only when the cell is within the garden and equals ``"*"``.

    :param int i_row: Row index of the reference cell.
    :param int offset_row: Row delta to apply to ``i_row``.
    :param int i_col: Column index of the reference cell.
    :param int offset_col: Column delta to apply to ``i_col``.
    :param list garden: The rectangular garden representation.
    :returns: ``1`` when the computed neighbor cell contains a flower, otherwise ``0``.
    :rtype: int
    """
    row: int = i_row + offset_row
    col: int = i_col + offset_col

    if (
        0 <= row < len(garden)  # ROW: Avoid IndexError
        and 0 <= col < len(garden[0])  # COL: Avoid IndexError
        and garden[row][col] == "*"  # Detect/count flower
    ):
        return 1
    return 0


def _validate(garden: list[str]) -> None:
    """
    Validate the garden shape and contents.

    Ensures the input is rectangular and contains only spaces and ``*``.
    Raise ValueError when the board receives malformed input garden is not
    a rectangle due to inconsistent row length or contains invalid chars
    inside the row.

    :param list garden: A list of equal-length strings to validate.
    :raises ValueError: If rows have differing lengths or contain characters
        other than space or ``*``.
    """
    garden_length = len(garden[0])
    if any(
        (len(row) != garden_length or not all(char in " *" for char in row))
        for row in garden
    ):
        raise ValueError("The board is invalid with current input.")
