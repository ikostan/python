"""
ISBN Verifier.

The ISBN-10 verification process is used to validate book identification
numbers. These normally contain dashes and look like: 3-598-21508-8

ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character
(either a digit or an X only). In the case the check character is an X,
this represents the value '10'. These may be communicated with or without
hyphens, and can be checked for their validity by the following formula:

(d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 +
d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0

If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
"""


def is_valid(isbn: str) -> bool:
    """
    Verify ISBN.

    :param isbn: 9 digits ISBN 10 format
    :return: Tru if isbn is valid, False otherwise
    """
    isbn_digits: list[int] = []
    for char in isbn:
        if char == "-":
            continue
        elif char.isdigit():
            isbn_digits.append(int(char))
        elif char.upper() == "X" and len(isbn_digits) == 9:
            isbn_digits.append(10)
        else:
            return False
    # ISBN total length should be = 10
    if len(isbn_digits) != 10:
        return False

    return (
        sum(digit * (10 - i) for i, digit in enumerate(isbn_digits)) % 11 == 0
    )
