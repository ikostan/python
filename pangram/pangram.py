"""
Pangram.

You work for a company that sells fonts through their website. They'd like to
show a different sentence each time someone views a font on their website.
To give a  comprehensive sense of the font, the random sentences should use
all the letters in the English alphabet.

They're running a competition to get suggestions for sentences that they can
use. You're in charge of checking the submissions to see if they are valid.
"""


def is_pangram(sentence: str) -> bool:
    """
    Verify that the random sentences uses all the letters in the English.

    :param sentence: The sentence to check for pangram validity
    :type sentence: str
    :return: True if the sentence contains all 26 letters of the English,
             False otherwise
    :rtype: bool
    """
    # Empty string
    if not sentence:
        return False
    # Convert sentence to lowercase and extract unique alphabetic characters
    unique_letters: set = set(char for char in sentence.lower() if char.isalpha())
    return len(unique_letters) == 26
