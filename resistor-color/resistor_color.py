"""
Utilities for working with the 10-color resistor code.

Mnemonics map the colors to the numbers, that, when stored
as an array, happen to map to their index in the array:
Better Be Right Or Your Great Big Values Go Wrong.
"""

COLORS: tuple = (  # pylint: disable=R0801
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)


def color_code(color: str) -> int:
    """
    Return the numeric code (0-9) for a resistor color.

    :param color: Color name.
    :type color: str
    :returns: Index in the standard 10-color sequence
              (0 for 'black' through 9 for 'white').
    :rtype: int
    :raises ValueError: If color is not a valid resistor color.
    """
    return COLORS.index(color)


def colors() -> list:
    """
    Return all valid resistor colors in ascending code order.

    :returns: List of color names in order from 'black' (0) to 'white' (9).
    :rtype: list
    """
    return list(COLORS)
