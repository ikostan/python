"""
The rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing
all the letters in the alphabet using an integer key between 0 and 26.
Using a key of 0 or 26 will always yield the same output due to modular
arithmetic. The letter is shifted for as many values as the value of the key.
"""

import string

LETTERS_LOWER: str = string.ascii_lowercase
LETTERS_UPPER: str = string.ascii_uppercase


def rotate(text: str, key: int) -> str:
    """
    Rotate each letter in the text by the specified key using Caesar cipher.

    Non-alphabetic characters remain unchanged. The rotation wraps around
    the alphabet (a->z, A->Z) using modular arithmetic.

    :param text: The input string to be rotated
    :param key: The number of positions to shift each letter (0-25)
    :return: The rotated string with letters shifted by key positions

    Examples:
        >>> rotate("abc", 1)
        "bcd"
        >>> rotate("Hello, World!", 13)
        "Uryyb, Jbeyq!"
    """
    new_str: list[str] = []
    for char in text:
        # Lower case
        if char in LETTERS_LOWER:
            new_str.append(
                LETTERS_LOWER[(LETTERS_LOWER.index(char) + key) % 26]
            )
        # Upper case
        elif char in LETTERS_UPPER:
            new_str.append(
                LETTERS_UPPER[(LETTERS_UPPER.index(char) + key) % 26]
            )
        # Not a letter
        else:
            new_str.append(char)
    # Convert to a string
    return "".join(new_str)
