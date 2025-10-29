"""Your task is to determine the RNA complement of a given DNA sequence."""

DNA = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand: str) -> str:
    """
    Determine the RNA complement for a DNA strand.

    :param dna_strand: DNA sequence containing only
           'G', 'C', 'T', or 'A' (case-insensitive).
    :return: RNA complement string using 'C', 'G', 'A',
             and 'U' (uppercase).
    :raises KeyError: If dna_strand contains any character
                      other than 'G', 'C', 'T', or 'A'.
    """
    return "".join(DNA[char] for char in dna_strand.upper())
