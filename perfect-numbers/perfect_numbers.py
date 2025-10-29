"""
Perfect Numbers.

Determine if a number is perfect, abundant, or deficient based on
Nicomachus' (60 - 120 CE) classification scheme for positive integers.
"""

import math


def classify(number: int) -> str:
    """
    A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError(
            "Classification is only possible for positive integers."
        )

    total_divisors: int = 1

    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            total_divisors += n
            if n != number // n:
                total_divisors += number // n

    if number == 1 or number > total_divisors:
        return "deficient"

    if total_divisors == number:
        return "perfect"

    return "abundant"
