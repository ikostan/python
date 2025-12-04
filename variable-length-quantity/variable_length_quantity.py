"""
Variable Length Quantity.

Implement variable length quantity encoding and decoding.
The goal of this exercise is to implement VLQ encoding/decoding.
"""

HEX_VALUES: str = "0123456789ABCDEF"


def encode(numbers: list[int]) -> list[int]:
    """

    :param numbers:
    :return:
    """
    results = []
    for number in numbers:
        chunks = []
        # Hex to Decimal -> Decimal to Binary
        n_bin = bin(int(number))
        # Split Binary into 7-Bit Chunks
        n_str: str = str(n_bin)[2:]  # represent binary value as a string, strip 'b0'
        # calculate number of 7 bit chunks
        n_chunks: int = len(n_str) // 7 if len(n_str) % 7 == 0 else (len(n_str) // 7) + 1
        # 7-Bit
        step: int = -7
        end = None
        start = -7
        step: int = -7
        for _ in range(n_chunks):
            chunk = n_str[start: end]
            if len(chunk) == 7:
                chunks.append(chunk)
            else:
                padding = "0" * (7 - len(chunk))
                chunks.append(padding + chunk)
            end = start
            start = (step + start) if (step + start) >= -len(n_str) else -len(n_str)
        chunks = chunks[::-1]
        # Add Continue Flag: since we have more than one member on the list
        # we have to add 1 in front of all member except the last one
        if len(chunks) > 1:
            for i, c in enumerate(chunks[:-1]):
                chunks[i] = "1" + chunks[i]
        # Convert to Decimal -> Convert Decimals to Hex
        for i, c in enumerate(chunks):
            chunks[i] = int(c, 2)
        results += chunks
    return results


def decode(bytes_: list):
    pass
