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


def calc_formula(digits: str) -> int:
    """
    Calculate the weighted sum for ISBN-10 validation formula.

    :param digits: List of integer digits to calculate the formula for
    :return: The weighted sum result used in ISBN-10 validation
    """
    result: int = 0
    for i, digit in enumerate(digits):
        if digit.isdigit():
            result += int(digit) * (10 - i)
        elif digit.lower() == "x":
            result += 10 * 1
        else:
            # Invalid char, calc failed
            return 1
    return result


def is_valid(isbn: str) -> bool:
    """
    Verify ISBN.

    :param isbn: 9 digits ISBN 10 format
    :return: Tru if isbn is valid, False otherwise
    """
    formated_isbn: str = isbn.replace("-", "")
    if len(formated_isbn) != 10:
        return False

    return calc_formula(formated_isbn) % 11 == 0
