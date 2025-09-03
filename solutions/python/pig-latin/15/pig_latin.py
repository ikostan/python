"""
The task is to translate text from English to Pig Latin.
The translation is defined using four rules, which look at the pattern
of vowels and consonants at the beginning of a word. These rules look
at each word's use of vowels and consonants:

vowels: the letters a, e, i, o, and u
consonants: the other 21 letters of the English alphabet
"""


def translate(text: str) -> str:
    """
    Translate English text to Pig Latin.

    :param text: The English text to translate
    :return: The text translated to Pig Latin
    """
    words: list[str] = text.split(" ")
    return " ".join(process_word(word) for word in words)


def process_word(text: str) -> str:
    """
    Process a single word and convert it to Pig Latin using
    the four translation rules.

    :param text: The English word to convert
    :return: The word converted to Pig Latin
    """
    if not text:
        return ""

    text_lower: str = text.lower()

    # Rule 1
    if is_vowel(text_lower[0]) or text_lower[:2] in ("xr", "yt"):
        # If a word begins with a vowel,
        # or starts with "xr" or "yt",
        # add an "ay" sound to the end of the word.
        return f"{text}ay"

    # Rule 3
    if is_rule_3(text_lower):
        # If a word starts with zero or more consonants followed by "qu",
        # first move those consonants (if any) and the "qu" part to the
        # end of the word, and then add an "ay" sound to the end of the word.
        i = text_lower.index("qu")
        return f"{text[i + 2 :]}{text[: i + 2]}ay"

    # Rule 4
    if is_rule_4(text_lower):
        # If a word starts with one or more consonants followed by "y",
        # first move the consonants preceding the "y" to the end of the
        # word, and then add an "ay" sound to the end of the word.
        i = text_lower.index("y")
        return f"{text[i:]}{text[:i]}ay"

    # Rule 2
    if not is_vowel(text_lower[0]):
        # If a word begins with one or more consonants, first move those
        # consonants to the end of the word and then add an "ay" sound
        # to the end of the word.
        i = get_consonant_cluster_index(text_lower)
        return f"{text[i + 1 :]}{text[: i + 1]}ay"

    raise ValueError(f"Unhandled word in Pig Latin translation: '{text}'")


def is_rule_3(text: str) -> bool:
    """
    Check if a word starts with zero or more consonants followed by "qu".

    :param text: The word to check
    :return: True if the word matches the pattern, False otherwise
    """
    if "qu" in text:
        if text[:2] == "qu":
            return True

        for char in text[: text.index("qu")]:
            if is_vowel(char):
                return False
        return True
    return False


def is_rule_4(text: str) -> bool:
    """
    Check if a word starts with one or more consonants followed by "y".

    :param text: The word to check
    :return: True if the word matches the pattern, False otherwise
    """
    if "y" in text and text[0] != "y":
        for char in text[: text.index("y")]:
            if is_vowel(char):
                return False
        return True
    return False


def is_vowel(char: str) -> bool:
    """
    Check if a character is a vowel (a, e, i, o, or u).

    :param char: The character to check
    :return: True if the character is a vowel, False otherwise
    """
    return char in "aeiou"


def get_consonant_cluster_index(text: str) -> int:
    """
    Find the index of the last consonant in the initial consonant cluster.

    :param text: The word to analyze
    :return: The index of the last consonant in the initial consonant cluster
    """
    index: int = 0
    for i, char in enumerate(text):
        if not is_vowel(char):
            index = i
        else:
            break

    return index
