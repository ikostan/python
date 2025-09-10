"""Darts is a game where players throw darts at a target."""

from math import sqrt


def score(x: int, y: int) -> int:
    """
    Calculate the points scored in a single toss of a Darts game.

    Given the x and y coordinates where a dart lands, returns the score
    based on the distance from the center (0, 0):
    - Inner circle (distance <= 1): 10 points
    - Middle circle (distance <= 5): 5 points
    - Outer circle (distance <= 10): 1 point
    - Outside target (distance > 10): 0 points

    :param x: The x-coordinate where the dart landed
    :param y: The y-coordinate where the dart landed
    :return: The points scored (0, 1, 5, or 10)
    """
    # Calculate distance form the center of the circle (0, 0)
    distance: float = sqrt(pow(x, 2) + pow(y, 2))
    # Outside target
    if distance > 10:
        return 0
    # Outer circle
    if distance > 5:
        return 1
    # Middle circle
    if distance > 1:
        return 5
    # Inner circle
    return 10
