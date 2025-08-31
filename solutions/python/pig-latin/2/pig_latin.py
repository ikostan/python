"""
The task is to translate text from English to Pig Latin.
The translation is defined using four rules, which look at the pattern of vowels
and consonants at the beginning of a word. These rules look at each word's use
of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
"""


def translate(text: str) -> str:
    """
    Translate text from English to Pig Latin.

    :param text:
    :return:
    """
    words: list = text.split(' ')
    return " ".join(process_text(word) for word in words)


def process_text(text: str) -> str:
    # Rule 1
    # If a word begins with a vowel,
    # or starts with "xr" or "yt",
    # add an "ay" sound to the end of the word.
    if is_rule_1(text):
        return text + 'ay'

    # Rule 2
    # If a word begins with one or more consonants, first move those consonants
    # to the end of the word and then add an "ay" sound to the end of the word.
    if is_rule_2(text):
        i = get_last_consonant_indx(text)
        return text[i + 1:] + text[: i + 1] + 'ay'

    # Rule 3
    # If a word starts with zero or more consonants followed by "qu", first move
    # those consonants (if any) and the "qu" part to the end of the word, and then
    # add an "ay" sound to the end of the word.
    if is_rule_3(text):
        i = text.index('qu')
        return text[i + 2:] + text[:i + 2] + 'ay'

    # Rule 4
    # If a word starts with one or more consonants followed by "y", first move the
    # consonants preceding the "y" to the end of the word, and then add an "ay" sound
    # to the end of the word.
    if is_rule_4(text):
        i = text.index('y')
        return text[i:] + text[:i] + 'ay'


def is_rule_1(text: str) -> bool:
    """
    Check if a word begins with a vowel, or starts with "xr" or "yt".

    :param text:
    :return:
    """
    if is_vowel(text[0]):
        return True
    if text[:2] in ("xr", "yt"):
        return True
    return False


def is_rule_2(text: str) -> bool:
    """
    Check ff a word begins with one or more consonants.
    No 'qu' or 'y' in it.

    :param text:
    :return:
    """
    return is_consonant(text[0]) and not is_rule_3(text) and not is_rule_4(text)


def is_rule_3(text: str) -> bool:
    """
    Check if a word starts with zero or more consonants followed by "qu".

    :param text:
    :return:
    """
    if 'qu' in text:
        if text[:2] == 'qu':
            return True

        for char in text[:text.index('qu')]:
            if is_vowel(char):
                return False
        return True
    return False


def is_rule_4(text: str) -> bool:
    """
    Check if a word starts with one or more consonants followed by "y".

    :param text:
    :return:
    """
    if 'y' in text and text[0] != 'y':
        for char in text[:text.index('y')]:
            if is_vowel(char):
                return False
        return True
    return False


def is_vowel(char: str) -> bool:
    """
    Test that char in vowels: the letters a, e, i, o, and u.

    :param char:
    :return:
    """
    return char in "aeiou"


def is_consonant(char: str) -> bool:
    """
    Check that char is consonant (the other 21 letters of the English alphabet).

    :param char:
    :return:
    """
    return char.isalpha() and not is_vowel(char)


def get_last_consonant_indx(text: str) -> int:
    """

    :param text:
    :return:
    """
    i = 0
    for i, char in enumerate(text):
        if is_consonant(char):
            i += 1
        else:
            break

    return i - 1
