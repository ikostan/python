"""
Bottle Song
===========

Recite verses from the children's song "Ten Green Bottles".

This module exposes the precomputed lyrics and a helper to
extract slices of the song by verse.
"""

Ten_Green_Bottles: list[str] = [
    "Ten green bottles hanging on the wall,",
    "Ten green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be nine green bottles hanging on the wall.",
    "",
    "Nine green bottles hanging on the wall,",
    "Nine green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be eight green bottles hanging on the wall.",
    "",
    "Eight green bottles hanging on the wall,",
    "Eight green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be seven green bottles hanging on the wall.",
    "",
    "Seven green bottles hanging on the wall,",
    "Seven green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be six green bottles hanging on the wall.",
    "",
    "Six green bottles hanging on the wall,",
    "Six green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be five green bottles hanging on the wall.",
    "",
    "Five green bottles hanging on the wall,",
    "Five green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be four green bottles hanging on the wall.",
    "",
    "Four green bottles hanging on the wall,",
    "Four green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be three green bottles hanging on the wall.",
    "",
    "Three green bottles hanging on the wall,",
    "Three green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be two green bottles hanging on the wall.",
    "",
    "Two green bottles hanging on the wall,",
    "Two green bottles hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be one green bottle hanging on the wall.",
    "",
    "One green bottle hanging on the wall,",
    "One green bottle hanging on the wall,",
    "And if one green bottle should accidentally fall,",
    "There'll be no green bottles hanging on the wall.",
]


def recite(start: int, take: int = 1) -> list[str]:
    """
    Return a slice of the song lyrics corresponding to ``take`` consecutive
    verses starting from the verse that begins with ``start`` green bottles.

    The lyrics are stored as a flat list where each verse occupies five lines
    (four lyric lines plus a trailing blank line). This function computes the
    appropriate slice boundaries to return the requested verses in order.

    :param start: The number of green bottles to start from (e.g., 10 for
                  "Ten green bottles"). Must be between 1 and 10.
    :param take: Number of consecutive verses to include starting at ``start``.
                 Defaults to 1.
    :returns: A list of lyric lines forming the requested verses.
    """
    start: int = -(start * 5)
    end: int = len(Ten_Green_Bottles) + start + (take * 5)
    return Ten_Green_Bottles[start + 1: end]
