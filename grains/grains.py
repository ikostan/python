"""Grains."""


def square(number) -> int:
    """
    Calculate the number of grains on a given square.

    One grain on the first square of a chessboard, with the number
    of grains doubling on each successive square.

    :param number: A chessboard square
    :type number: int
    :return: number of grains on a given square.
    :rtype: int
    """
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total() -> int:
    """
    Calculate the total number of grains on the chessboard.

    A chessboard has 64 squares. Square 1 has one grain,
    square 2 has two grains, square 3 has four grains, and so on,
    doubling each time.

    :return: the total number of grains on the chessboard.
    :rtype: int
    """
    # return sum(square(sqr) for sqr in range(1, 65))
    return 2**64 - 1
