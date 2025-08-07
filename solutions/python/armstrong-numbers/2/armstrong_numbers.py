"""Armstrong Numbers."""


def is_armstrong_number(number: int) -> bool:
    """
    Test if "Armstrong Number".

    An Armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits.

    :param number: any integer number
    :type number: int
    :return: if "Armstrong Number"
    :rtype: bool

    Examples:
    >>> is_armstrong_number(153)
    True
    >>> is_armstrong_number(10)
    False
    """
    if number < 0:
        raise ValueError("Only non-negative integers are allowed")

    str_num: str = str(number)
    n: int = len(str_num)
    return number == sum(int(char) ** n for char in str_num)
