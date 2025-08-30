"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 2


# pylint: disable=R0801
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the bake time remaining.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calculate preparation time in minutes

    Takes the `number_of_layers` you want to add to the lasagna as an argument and
    returns how many minutes you would spend making them.

    Assume each layer takes 2 minutes to prepare.

    :param number_of_layers: Number of layers you want to add to the lasagna.
    :type number_of_layers: int
    :return: Preparation time in minutes
    :rtype: int
    """
    return int(PREPARATION_TIME * number_of_layers)


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate elapsed time in minutes.

    Return the total minutes you have been in the kitchen cooking — your preparation time layering +
    the time the lasagna has spent baking in the oven.

    :param number_of_layers: The number of layers added to the lasagna.
    :type number_of_layers: int
    :param elapsed_bake_time: The number of minutes the lasagna has
                              spent baking in the oven already.
    :type elapsed_bake_time: int
    :return: Elapsed time in minutes.
    :rtype: int
    """
    return preparation_time_in_minutes(number_of_layers=number_of_layers) + (
        EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time)
    )
