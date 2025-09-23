"""
Convert a sequence of digits in one base, representing a number,
into a sequence of digits in another base, representing the same number.
"""


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """
    Convert a non-negative integer represented as digits in one base
    to digits in another base.

    :param int input_base: Base of the input digits; must be >= 2.
    :param list[int] digits: Sequence of digits where each d satisfies
                             0 <= d < input_base. Leading zeros are allowed;
                             an empty list denotes 0.
    :param int output_base: Base for the output digits; must be >= 2.
    :returns: Digits of the same number in ``output_base``, without leading
              zeros (except ``[0]`` for zero).
    :rtype: list[int]
    :raises ValueError: If ``input_base < 2``, if any digit violates
                        ``0 <= d < input_base``, or if ``output_base < 2``.
    """
    # Step 1: Validate the Inputs (Before Any Calculations)
    # Validate input_base >= 2
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # Validate each digit is 0 <= d < input_base
    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Validate output_base >= 2
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Step 2: Calculate the Intermediate Value Using input_base and digits
    # Start from the least significant number (from the right)
    # -> hence reverse the list
    intermediate_val: int = sum(
        digit * (input_base**i) for i, digit in enumerate(reversed(digits))
    )

    # Step 3: Convert the Intermediate Value to digits in output_base
    answer: list[int] = []
    while True:
        # Compute quotient (new intermediate_val)
        # and remainder (least significant digit)
        intermediate_val, remainder = (
            intermediate_val // output_base,
            intermediate_val % output_base,
        )
        # Add the least significant number into a new list of digits
        answer.append(remainder)
        # Break the loop since reach zero, no more calculation needed
        if intermediate_val == 0:
            break

    # Reverse the list to place the most significant digit first (leftmost).
    return answer[::-1]
