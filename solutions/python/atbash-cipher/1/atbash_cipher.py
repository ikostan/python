"""
This is an implementation of the 'Atbash' cipher, an ancient
encryption system created in the Middle East.
"""

import string

alphabet: str = string.ascii_lowercase


def encode(plain_text: str) -> str:
    temp_txt: [str] = [
        _replace(char) for char in plain_text if char not in ".,!? "
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
        print(f"{' '.join(txt)}")
        return " ".join(txt)
    return "".join(temp_txt)


def _replace(char: str) -> str:
    if char.lower().isalpha():
        new_indx: int = alphabet.index(char.lower()) + 1
        return alphabet[-new_indx]
    return char


def decode(ciphered_text: str) -> str:
    return encode(ciphered_text).replace(" ", "")
