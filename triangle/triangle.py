"""Determine if a triangle is equilateral, isosceles, or scalene."""


def equilateral(sides: list) -> bool:
    """
    An equilateral triangle has all three sides the same length.
    """
    if all_sides_positive(sides) and no_inequality_violation(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides: list) -> bool:
    """
    An isosceles triangle has at least two sides the same length.
    (It is sometimes specified as having exactly two sides the same length,
    but for the purposes of this exercise we'll say at least two.)
    """
    if all_sides_positive(sides) and no_inequality_violation(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    return False


def scalene(sides: list) -> bool:
    """
    A scalene triangle has all sides of different lengths.
    """
    if all_sides_positive(sides) and no_inequality_violation(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
    return False


def no_inequality_violation(sides: list) -> bool:
    """
    Let a, b, and c be sides of the triangle.
    Then all three of the following expressions must be true:

    a + b ≥ c
    b + c ≥ a
    a + c ≥ b
    """
    return (sides[0] + sides[1] >= sides[2] and
            sides[0] + sides[2] >= sides[1] and
            sides[2] + sides[1] >= sides[0])


def all_sides_positive(sides: list) -> bool:
    """
    No zeroes or negative numbers allowed.
    All triangles should have 3 sides.
    """
    return all(side > 0 for side in sides) and len(sides) == 3
