"""
Convert a sequence of digits in one base, representing a number,
into a sequence of digits in another base, representing the same number.
"""


def rebase(input_base: int, digits: list[int], output_base: int):
    """
    Convert a non-negative integer represented as digits in one base to digits in another base.

    :param int input_base: Base of the input digits; must be >= 2.
    :param list[int] digits: Sequence of digits where each d satisfies 0 <= d < input_base.
                             Leading zeros are allowed; an empty list denotes 0.
    :param int output_base: Base for the output digits; must be >= 2.
    :returns: Digits of the same number in ``output_base``, without leading zeros
              (except ``[0]`` for zero).
    :rtype: list[int]
    :raises ValueError: If ``input_base < 2``, if any digit violates ``0 <= d < input_base``,
                        or if ``output_base < 2``.
    """

    # for input.
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # another example for input.
    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # or, for output.
    if output_base < 2:
        raise ValueError("output base must be >= 2")
