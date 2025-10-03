"""
Parse and evaluate simple math word problems
returning the answer as an integer.

Handle a set of operations, in sequence.

Since these are verbal word problems, evaluate
the expression from left-to-right, ignoring the
typical order of operations.
"""

STR_TO_OPERATOR: dict[str, str] = {
    "plus": "+",
    "minus": "-",
    "multiplied": "*",
    "divided": "/",
}

REPLACEABLE: tuple = ("What", "is", "by")


def answer(question: str) -> int:
    """
    Evaluate a simple word-based arithmetic question from left to right.

    :param question: The input question, e.g., "What is 5 plus 13?"
    :type question: str
    :returns: The evaluated integer result.
    :rtype: int
    :raises ValueError: If the operation is unknown or the syntax is invalid.
    """
    new_question: list[str] = [
        word
        for word in question.replace("?", "").split()
        if word not in REPLACEABLE
    ]
    # Reduce iteratively:
    # evaluate the first three-token slice and fold the result left-to-right.
    try:
        result, new_question = int(new_question[0]), new_question[1:]
        while new_question:
            result, new_question = _math_operation(result, new_question)
    except ValueError as exc:
        if exc.args[0] == "unknown operation":
            raise exc
        raise ValueError("syntax error") from exc
    except IndexError as exc:
        raise ValueError("syntax error") from exc

    return result


def _math_operation(result: int, question: list[str]) -> tuple[int, list[str]]:
    """
    Compute a single binary arithmetic step for the current operator.

    Expects the next tokens of the question to begin with the operator word
    (e.g. ``plus``, ``minus``, ``multiplied``, ``divided``) followed by the
    right-hand side operand. Division uses floor division (``//``) to comply
    with the exercise rules.

    :param result: Accumulated left-hand value computed so far.
    :type result: int
    :param question: Remaining tokens starting with the operator then rhs integer,
                     e.g. ``['plus', '4', ...]``.
    :type question: list[str]
    :returns: A tuple of the new accumulated result and the remaining tokens after
              consuming the operator and rhs.
    :rtype: tuple[int, list[str]]
    :raises ValueError: If the operator is unknown or the token sequence is malformed.
    """
    math_operator: str = question[0]
    # if the question contains an unknown operation.
    if (
        math_operator not in STR_TO_OPERATOR.keys()
        and not math_operator.isdigit()
    ):
        raise ValueError("unknown operation")
    # if the question is malformed or invalid.
    if math_operator.isdigit():
        raise ValueError("syntax error")
    # if the question is malformed or invalid.
    if math_operator in STR_TO_OPERATOR and len(question) == 1:
        raise ValueError("syntax error")

    if STR_TO_OPERATOR[math_operator] == "+":
        return result + int(question[1]), question[2:]

    if STR_TO_OPERATOR[math_operator] == "-":
        return result - int(question[1]), question[2:]

    if STR_TO_OPERATOR[math_operator] == "/":
        return result // int(question[1]), question[2:]

    if STR_TO_OPERATOR[math_operator] == "*":
        return result * int(question[1]), question[2:]
