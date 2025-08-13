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
    """
    str_num: str = str(number)
    n: int = len(str_num)
    return number == sum(int(char) ** n for char in str_num)
