"""
Resistor Color Expert.

In this exercise you will need to add tolerance to the mix.
Tolerance is the maximum amount that a value can be above or
below the main value. For example, if the last band is green,
the maximum tolerance will be ±0.5%.
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

# Mapping of tolerance band color names to their maximum tolerance suffix.
MAX_TOLERANCE: dict[str, str] = {
    "grey": " ±0.05%",
    "violet": " ±0.1%",
    "blue": " ±0.25%",
    "green": " ±0.5%",
    "brown": " ±1%",
    "red": " ±2%",
    "gold": " ±5%",
    "silver": " ±10%",
}


def resistor_label(colors: list[str]) -> str:
    """
    Return a human-readable resistor label from band colors.

    Scales to the largest whole unit (ohms, kiloohms, megaohms, gigaohms)
    and appends maximum tolerance if present.

    :param colors: Band colors in order. Lengths:
                   1 (value only);
                   4 (two digits, multiplier, tolerance);
                   5 (three digits, multiplier, tolerance).
    :type colors: list[str]
    :returns: Scaled value with units and optional tolerance (e.g., '4.7 kiloohms ±5%').
    :rtype: str
    :raises KeyError: If an unknown color is provided.
    """

    prefix: str = ""
    postfix: str = ""
    max_tolerance: str = ""

    if len(colors) == 1:
        prefix: str = f"{COLOR_VALUES[colors[0]]}"

    if len(colors) == 4:
        prefix: str = (f"{COLOR_VALUES[colors[0]]}"
                       f"{COLOR_VALUES[colors[1]]}")
        postfix = f"{'0' * COLOR_VALUES[colors[2]]}"
        max_tolerance = MAX_TOLERANCE[colors[3]]

    if len(colors) == 5:
        prefix = (f"{COLOR_VALUES[colors[0]]}"
                  f"{COLOR_VALUES[colors[1]]}"
                  f"{COLOR_VALUES[colors[2]]}")
        postfix = f"{'0' * COLOR_VALUES[colors[3]]}"
        max_tolerance = MAX_TOLERANCE[colors[4]]

    int_val: int = int(prefix + postfix)

    # Scale to the largest whole unit
    # (ohms, kiloohms, megaohms, gigaohms) for readability
    if 1000 <= int_val < 1000000:
        return f"{float(int_val / 1000)}".rstrip(".0") + f" kiloohms{max_tolerance}"

    if 1000000 <= int_val < 1000000000:
        return f"{int_val / 1000000} megaohms{max_tolerance}"

    if 1000000000 <= int_val:
        return f"{int_val / 1000000000} gigaohms{max_tolerance}"

    return f"{int_val} ohms{max_tolerance}"
