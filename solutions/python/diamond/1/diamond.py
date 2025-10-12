"""
The diamond kata takes as its input a letter, and outputs it in
a diamond shape. Given a letter, it prints a diamond starting
with 'A', with the supplied letter at the widest point.
"""

import string

CHARS: str = string.ascii_uppercase


def rows(letter: str) -> list:
    """
    Return the diamond rows from 'A' to ``letter``.

    Builds the upper half and mirrors it to form a symmetric diamond.

    :param str letter: Uppercase letter (``'A'``-``'Z'``) marking the widest row.
    :returns: The full diamond as a list of strings, one per row.
    :rtype: list
    :raises ValueError: If ``letter`` is not an ASCII uppercase character.
    """
    result: list = []
    letter_index: int = CHARS.index(letter)
    row_length: int = (letter_index * 2) + 1

    for i, char in enumerate(CHARS[: letter_index + 1]):
        # All rows have as many trailing spaces as leading spaces.
        spaces: str = " " * (letter_index - i)
        # The first/last row contains one 'A'.
        if i == 0:
            result.append(spaces + char + spaces)
        else:
            middle: str = " " * (row_length - 2 - (len(spaces) * 2))
            # All rows, except the first and last, have exactly two identical letters.
            result.append(spaces + char + middle + char + spaces)
    # Mirror the list: the bottom half has the letters in descending order.
    result = result + result[::-1][1:]
    return result
