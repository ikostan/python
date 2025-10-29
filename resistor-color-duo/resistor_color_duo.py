"""
Resistor Color Duo.

In this exercise you are going to create a helpful program so that
you don't have to remember the values of the bands. The program will
take color names as input and output a two digit number, even if the
input is more than two colors!
"""

COLORS: tuple = (
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


def value(colors: list) -> int:
    """
    Take color names as input and output a two-digit number.

    :param colors: list of color names
    :return: two-digit number
    """
    return int("".join(str(COLORS.index(color)) for color in colors[:2]))
