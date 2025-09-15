"""
Determine if a number is perfect, abundant, or deficient based on
Nicomachus' (60 - 120 CE) classification scheme for positive integers.
"""


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

    total_divisors: int = sum(i for i in range(1, number) if number % i == 0)

    if total_divisors == number:
        return "perfect"
    if number < total_divisors:
        return "abundant"

    return "deficient"
