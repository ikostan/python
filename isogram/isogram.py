"""
Isogram.

Determine if a word or phrase is an isogram.

An isogram (also known as a "non-pattern word") is a word or phrase
without a repeating letter, however spaces and hyphens are allowed
to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old

The word isograms, however, is not an isogram, because the s repeats.
"""


def is_isogram(string: str) -> bool:
    """
    Determine if a word or phrase is an isogram.

    An isogram is a word or phrase without repeating letters. Spaces and
    hyphens are allowed to appear multiple times, but alphabetic
    characters must be unique (case-insensitive).

    :param string: The word or phrase to check
    :type string: str
    :returns: True if the string is an isogram, False otherwise
    :rtype: bool
    """
    # empty string
    if not string:
        return True

    letters: list[str] = [char for char in string.lower() if char.isalpha()]
    return len(letters) == len(set(letters))
