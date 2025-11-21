"""
Resistor Color Trio.

In Resistor Color Duo you decoded the first two colors.
For instance: orange-orange got the main value 33.
The third color stands for how many zeros need to be added to the main value.
The main value plus the zeros gives us a value in ohms. For the exercise it
doesn't matter what ohms really are.
"""

# Mapping of resistor color names to their corresponding digit values.
COLOR_VALUES: dict[str, int] = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors: list[str]) -> str:
    """
    Return a human-readable label for a 3-band resistor value.

    The first two colors form the significant digits and the third color
    is the multiplier (number of trailing zeros). The resulting value is
    scaled to the largest whole unit among ohms, kiloohms, megaohms, or
    gigaohms.

    :param colors: Three resistor color names in order [band1, band2, multiplier].
                   band1 and band2 provide the significant digits; multiplier
                   adds zeros.
    :return: Formatted resistance value string using the largest whole unit
             (e.g., '47 kiloohms', '680 ohms').
    :raises KeyError: If a color name is not recognized.
    :raises IndexError: If fewer than three colors are provided.
    """
    prefix: str = f"{COLOR_VALUES[colors[0]]}{COLOR_VALUES[colors[1]]}"
    postfix: str = f"{'0' * COLOR_VALUES[colors[2]]}"
    int_val: int = int(prefix + postfix)

    # Scale to the largest whole unit
    # (ohms, kiloohms, megaohms, gigaohms) for readability
    if 1000 <= int_val < 1000000:
        return f"{int_val // 1000} kiloohms"

    if 1000000 <= int_val < 1000000000:
        return f"{int_val // 1000000} megaohms"

    if 1000000000 <= int_val:
        return f"{int_val // 1000000000} gigaohms"

    return f"{int_val} ohms"
