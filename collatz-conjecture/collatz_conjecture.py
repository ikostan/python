"""
Collatz Conjecture.

The rules were deceptively simple. Pick any positive integer.

If it's even, divide it by 2.
If it's odd, multiply it by 3 and add 1.
Then, repeat these steps with the result, continuing indefinitely.

Curious, you picked number 12 to test and began the journey:

12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
"""


# pylint: disable=R0801
def steps(number: int) -> int:
    """
    Return the number of steps it takes to reach 1 according to
    the rules of the Collatz Conjecture.

    :param number: any positive integer
    :type number: int
    :return: number of steps it takes to reach 1
    :rtype: int
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    n_steps: int = 0
    while number > 1:
        # If it's even, divide it by 2
        if number % 2 == 0:
            # Switch to integer division
            # keeps everything as int and avoids precision issues
            number = number // 2
        # If it's odd, multiply it by 3 and add 1
        else:
            number = (number * 3) + 1
        n_steps += 1

    return n_steps
