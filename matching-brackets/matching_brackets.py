"""
Matching Brackets.

You're given the opportunity to write software for the Bracketeer™,
an ancient but powerful mainframe. The software that runs on it is
written in a proprietary language. Much of its syntax is familiar,
but you notice lots of brackets, braces and parentheses. Despite
the Bracketeer™ being powerful, it lacks flexibility. If the source
code has any unbalanced brackets, braces or parentheses, the Bracketeer™
crashes and must be rebooted. To avoid such a scenario, you start writing
code that can verify that brackets, braces, and parentheses are balanced
before attempting to run it on the Bracketeer™.
"""

PAIRS: dict = {
    "]": "[",
    "}": "{",
    ")": "(",
}


def is_paired(input_string: str) -> bool:
    """
    Verify that any and all pairs of brackets are matched.

    Given a string containing brackets [], braces {}, parentheses (),
    or any combination thereof, verify that any and all pairs are matched
    and nested correctly. Any other characters should be ignored. For example,
    "{what is (42)}?" is balanced and "[text}" is not.

    :param input_string: The string to check for balanced brackets
    :type input_string: str
    :returns: True if all brackets are properly paired and nested,
              False otherwise
    :rtype: bool
    """
    # Empty string
    if not input_string:
        return True

    # Remove all non bracket items and convert a string to a list.
    brackets_list: list[str] = [
        bracket for bracket in input_string if bracket in "(){}[]"
    ]

    # Odd number of brackets
    if len(brackets_list) % 2 != 0:
        return False

    stack: list[str] = []
    for bracket in brackets_list:
        if bracket in "({[":
            stack.append(bracket)
        elif bracket in PAIRS:
            if not stack or stack.pop() != PAIRS[bracket]:
                return False

    return not stack
