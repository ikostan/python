"""
Anagram.

Given a target word and one or more candidate words,
your task is to find the candidates that are anagrams
of the target.
"""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Return the list of candidates that are anagrams of ``word``.

    Two words are considered anagrams if they consist of the same letters
    with the same multiplicities when case is ignored. The original casing of
    candidates is preserved in the returned list. Exact same word (case-insensitive)
    as the target is excluded.

    :param word: Target word to compare against.
    :param candidates: Sequence of candidate words to test.
    :returns: A list containing each candidate that is an anagram of ``word``.
    """
    word_ordered_lower_chars: list[str] = sorted(char.lower() for char in word)
    word_lower = word.lower()
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word_lower
        and sorted(char for char in candidate.lower()) == word_ordered_lower_chars
    ]
