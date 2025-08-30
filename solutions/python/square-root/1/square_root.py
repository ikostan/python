"""Solution for Square Root."""

from math import sqrt


def square_root(number: float) -> int:
    """
    Calculate square root.

    :param number: any number
    :type number: float
    :return: square root of any number,
             only natural numbers (positive integers) as solutions.
    :rtype: int
    """
    return int(sqrt(number))
