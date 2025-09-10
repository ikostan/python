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
        # Not a letter
        if not char.isalpha():
            new_str.append(char)
        else:
            new_str.append(replace_char(char, key))
    # Convert to a string
    return "".join(new_str)


def replace_char(char: str, key: int) -> str:
    """
    Shifts the character by the specified key positions within its alphabet
    (uppercase or lowercase). Uses modular arithmetic to wrap around the
    alphabet.

    :param char: The alphabetic character to rotate
    :param key: The number of positions to shift the character
    :return: The rotated character in the same case as the input
    """
    if char in LETTERS_UPPER:
        new_index: int = LETTERS_UPPER.index(char) + key
        if new_index < 26:
            return LETTERS_UPPER[new_index]
        return LETTERS_UPPER[new_index - 26]

    new_index = LETTERS_LOWER.index(char) + key
    if new_index < 26:
        return LETTERS_LOWER[new_index]
    return LETTERS_LOWER[new_index - 26]
