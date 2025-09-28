"""
This is an implementation of the 'Atbash' cipher, an ancient
encryption system created in the Middle East.
"""

import string

alphabet: str = string.ascii_lowercase


def encode(plain_text: str) -> str:
    """
    Encode text using the Atbash cipher.

    Letters are mirrored in the lowercase Latin alphabet; digits are preserved.
    Punctuation characters '.,!?' and spaces are removed. The result is grouped
    into 5-character blocks separated by spaces for readability.

    :param plain_text: Input text to encode.
    :type plain_text: str
    :returns: Encoded text (grouped in 5-character blocks when length >= 5).
    :rtype: str
    """
    temp_txt: list[str] = [
        _replace(char.lower()) for char in plain_text if char.isalnum()
    ]
    if len(temp_txt) > 4:
        step: int = 5
        i_start: int = 0
        i_end: int = i_start + step
        txt: list[str] = []
        while i_start <= len(temp_txt):
            tmp: str = "".join(temp_txt[i_start:i_end])
            if tmp:
                txt.append(tmp)
            i_start, i_end = i_end, i_end + step
        return " ".join(txt)
    return "".join(temp_txt)


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
