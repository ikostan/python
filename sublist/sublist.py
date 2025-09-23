"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.

It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: list, list_two: list) -> int:
    """
    Classify the relationship between two lists.

    Determines whether ``list_one`` and ``list_two`` are equal, or whether one
    is a contiguous sublist of the other, and returns the appropriate constant.

    :param list_one: First list to compare.
    :type list_one: list
    :param list_two: Second list to compare.
    :type list_two: list
    :returns: One of ``EQUAL``, ``SUBLIST``, ``SUPERLIST``, or ``UNEQUAL``.
    :rtype: int
    """

    len1: int = len(list_one)
    len2: int = len(list_two)

    if len1 == len2:
        if list_one == list_two:
            return EQUAL
        return UNEQUAL

    l1: str = ",".join(str(i) for i in list_one)
    l2: str = ",".join(str(i) for i in list_two)

    if l2 in l1:
        return SUPERLIST

    if l1 in l2:
        return SUBLIST

    return UNEQUAL
