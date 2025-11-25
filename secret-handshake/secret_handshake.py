"""
Secret Handshake.

Convert a number's binary representation (up to five bits) to a
sequence of actions in the secret handshake.

The sequence of actions is determined by inspecting the rightmost five
binary digits (least-significant bit on the right):

- 1 (..00001): "wink"
- 2 (..00010): "double blink"
- 4 (..00100): "close your eyes"
- 8 (..01000): "jump"
- 16(..10000): reverse the order of the operations selected above

Only the presence of a bit matters; higher bits beyond the five listed
are ignored. The reverse bit (16) inverses the final list of actions.
"""

ACTIONS: tuple[str, str, str, str] = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list[str]:
    """
    Return the list of secret-handshake actions for the given binary string.

    The input should be a binary string whose rightmost character is the
    least-significant bit. Up to five bits are considered, mapping to the
    actions defined by the classic Exercism "Secret Handshake" exercise.
    If the fifth bit is set, the final list of actions is reversed.

    :param binary_str: Binary string (e.g. "10101"). Rightmost char is LSB.
    :returns: A list of action strings in the computed order.
    """
    results: list[str] = []
    # Iterate from least- to most-significant bit by reversing the string.
    for i, char in enumerate(binary_str[::-1]):
        # Check if the corresponding bit position matches the expected "1".
        if char == "1" and i < 4:
            results.append(ACTIONS[i])
        elif char == "1" and i == 4:
            # Fifth bit indicates the final list should be reversed.
            results = results[::-1]
    return results
