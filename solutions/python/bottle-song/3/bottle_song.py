"""
Bottle Song.

Recite verses from the children's song "Ten Green Bottles".

This module exposes the precomputed lyrics and a helper to
extract slices of the song by verse.
"""

NUMBERS: tuple = (
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
)


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
    result: list[str] = []
    for i in range(start, start - take, -1):
        if i == 1:
            verse = [
                f"{NUMBERS[i - 1]} green bottle hanging on the wall,",
                f"{NUMBERS[i - 1]} green bottle hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                "There'll be no green bottles hanging on the wall.",
            ]
        elif i != start - take + 1:
            verse = [
                f"{NUMBERS[i - 1]} green bottles hanging on the wall,",
                f"{NUMBERS[i - 1]} green bottles hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {NUMBERS[i - 2].lower()} green "
                f"{'bottles' if NUMBERS[i - 2] != 'One' else 'bottle'} hanging on"
                f" the wall.",
                "",
            ]
        else:
            verse = [
                f"{NUMBERS[i - 1]} green bottles hanging on the wall,",
                f"{NUMBERS[i - 1]} green bottles hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {NUMBERS[i - 2].lower()} green "
                f"{'bottles' if NUMBERS[i - 2] != 'One' else 'bottle'} hanging on"
                f" the wall.",
            ]
        result += verse
    return result
