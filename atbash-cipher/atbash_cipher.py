"""
Atbash Cipher.

This is an implementation of the 'Atbash' cipher, an ancient
encryption system created in the Middle East.
"""

import string

alphabet: str = string.ascii_lowercase


def encode(plain_text: str) -> str:
    """
    Encode text using the Atbash cipher.

    Letters are mirrored in the lowercase Latin alphabet; digits are preserved.
    Punctuation characters '.,!?;:-' and spaces are removed. The result is
    grouped into 5-character blocks separated by spaces for readability.

    :param plain_text: Input text to encode.
    :type plain_text: str
    :returns: Encoded text (grouped in 5-character blocks when length >= 5).
    :rtype: str
    """
    temp_txt: str = "".join(
        _replace(char.lower()) for char in plain_text if char.isalnum()
    )
    return " ".join(
        "".join(temp_txt[i : i + 5]) for i in range(0, len(temp_txt), 5)
    )


def _replace(char: str) -> str:
    """
    Apply Atbash mapping to a single character.

    Alphabetic characters are lowercased and mirrored in the alphabet;
    non-letters are returned unchanged.

    :param char: Character to transform.
    :type char: str
    :returns: Transformed character.
    :rtype: str
    """
    if char.isalpha():
        return alphabet[-(alphabet.index(char) + 1)]
    return char


def decode(ciphered_text: str) -> str:
    """
    Decode an Atbash-encoded string.

    Atbash is symmetric; decoding reuses encoding and removes grouping spaces.

    :param ciphered_text: Encoded text, optionally grouped with spaces.
    :type ciphered_text: str
    :returns: Decoded text without grouping spaces.
    :rtype: str
    """
    return encode(ciphered_text).replace(" ", "")
