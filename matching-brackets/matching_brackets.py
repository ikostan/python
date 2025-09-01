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

LEFT: str = "[{("
RIGHT: str = "]})"
PAIRS: dict = {
    "[": "]",
    "{": "}",
    "(": ")",
}


def is_paired(input_string: str) -> bool:
    """
    Verify that any and all pairs of brackets are matched.

    Given a string containing brackets [], braces {}, parentheses (),
    or any combination thereof, verify that any and all pairs are matched
    and nested correctly. Any other characters should be ignored. For example,
    "{what is (42)}?" is balanced and "[text}" is not.

    :param input_string:
    :return:
    """
    # Empty string
    if not input_string:
        return True

    # Remove all non bracket items and convert a string to a list.
    brackets_list: list = [bracket for bracket in input_string if bracket in "(){}[]"]

    # Odd number of brackets
    if len(brackets_list) % 2 != 0:
        return False

    paired: bool = True
    while paired and brackets_list:
        for i, bracket in enumerate(brackets_list):

            # Right side bracket found
            if bracket in RIGHT:
                paired = False
                break

            # No matching pair found
            if (
                brackets_list[i + 1] != PAIRS[bracket]
                and brackets_list[-1] != PAIRS[bracket]
            ):
                paired = False
                break

            # Matching pair found next to it
            if brackets_list[i + 1] == PAIRS[bracket]:
                del brackets_list[1]
                del brackets_list[0]
                break

            # Matching pair found at the end of the list
            if brackets_list[-1] == PAIRS[bracket]:
                del brackets_list[0]
                del brackets_list[-1]
                break

    return paired
