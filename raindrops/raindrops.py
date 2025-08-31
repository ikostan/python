"""
Introduction

Raindrops is a slightly more complex version of the FizzBuzz challenge,
a classic interview question.

Instructions

Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

is divisible by 3, add "Pling" to the result.
is divisible by 5, add "Plang" to the result.
is divisible by 7, add "Plong" to the result.
is not divisible by 3, 5, or 7, the result should be the number as a string.
"""


def convert(number: int) -> str:
    """
    Convert a number into its corresponding raindrop sounds.

    :param number:
    :return:
    """
    result: str = ""
    # is divisible by 3, add "Pling" to the result.
    if number % 3 == 0:
        result += "Pling"
    # is divisible by 5, add "Plang" to the result.
    if number % 5 == 0:
        result += "Plang"
    # is divisible by 7, add "Plong" to the result.
    if number % 7 == 0:
        result += "Plong"
    # is not divisible by 3, 5, or 7, the result should be the number as a string.
    return result if result else str(number)
