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

import logging

LEFT: str = "[{("
RIGHT: str = "]})"
PAIRS: dict = {
    "[": "]",
    "{": "}",
    "(": ")",
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

    :param input_string:
    :return:
    """
    # Setup logging (console handler for visibility)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)
    logger.info("Processing text: %s", input_string)

    # Empty string
    if not input_string:
        logger.info("Empty string. Return True.")
        return True

    # Remove all non bracket items and convert a string to a list.
    brackets_list: list = [bracket for bracket in input_string if bracket in "(){}[]"]

    # Odd number of brackets
    if len(brackets_list) % 2 != 0:
        logger.info("Odd number of characters. Return False.")
        return False

    paired: bool = True
    while paired and brackets_list:
        logger.info("brackets_list: %s", brackets_list)
        for i, bracket in enumerate(brackets_list):
            if bracket in RIGHT:
                paired = False
                logger.info("Right side bracket found: %s. Return False.", bracket)
                break

            if i + 1 < len(brackets_list):
                if (
                    brackets_list[i + 1] != PAIRS[bracket]
                    and brackets_list[-1] != PAIRS[bracket]
                ):
                    paired = False
                    logger.info("No matching bracket found: %s. Return False.", bracket)
                    break

                if brackets_list[i + 1] == PAIRS[bracket]:
                    logger.info(
                        "Matching pair found: %s.",
                        brackets_list[:2],
                    )
                    del brackets_list[1]
                    del brackets_list[0]
                    break
                elif brackets_list[-1] == PAIRS[bracket]:
                    logger.info(
                        "Matching pair found: %s %s.",
                        brackets_list[0],
                        brackets_list[-1],
                    )
                    del brackets_list[0]
                    del brackets_list[-1]
                    break
            else:
                paired = False
                break

    logger.info("Is paired: %s", paired)
    return paired
