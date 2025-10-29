"""
Parse and evaluate simple math word problems returning the answer as an integer.

Handle a set of operations, in sequence.

Since these are verbal word problems, evaluate
the expression from left-to-right, ignoring the
typical order of operations.
"""

OPERATORS: tuple = ("plus", "minus", "multiplied", "divided")
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
    # evaluate the first two-token slice and fold the result left-to-right.
    try:
        result, new_question = int(new_question[0]), new_question[1:]
        while new_question:
            _err_check(new_question)
            result, new_question = (
                _math_operation(result, new_question),
                new_question[2:],
            )
    except ValueError as exc:
        if exc.args[0] == "unknown operation":
            raise exc
        raise ValueError("syntax error") from exc
    except IndexError as exc:
        raise ValueError("syntax error") from exc

    return result


def _math_operation(result: int, question: list[str]) -> int:
    """
    Compute a single binary arithmetic step for the current operator.

    Expects the next tokens of the question to begin with the operator word
    (e.g. ``plus``, ``minus``, ``multiplied``, ``divided``) followed by the
    right-hand side operand. Division uses floor division (``//``) to comply
    with the exercise rules.

    :param result: Accumulated left-hand value computed so far.
    :type result: int
    :param question: Remaining tokens starting with the operator then rhs
                     integer, e.g. ``['plus', '4', ...]``.
    :type question: list[str]
    :returns: Accumulated result after consuming the operator and rhs.
    :rtype: int
    """
    math_operator: str = question[0]
    operand: int = int(question[1])

    match math_operator:
        case "plus":
            result += operand
        case "minus":
            result -= operand
        case "divided":
            result //= operand
        case "multiplied":
            result *= operand

    return result


def _err_check(question: list[str]) -> None:
    """
    Validate the upcoming operator/operand tokens and raise appropriate errors.

    :param question: Remaining tokens starting at the operator; used to detect
                     malformed sequences (e.g., missing rhs integer).
    :type question: list[str]
    :raises ValueError: If an unknown operation is encountered or the token
                        sequence is syntactically invalid.
    """
    math_operator: str = question[0]
    # if the question contains an unknown operation.
    if math_operator not in OPERATORS and not math_operator.isdigit():
        raise ValueError("unknown operation")
    # if the question is malformed or invalid.
    if math_operator.isdigit():
        raise ValueError("syntax error")
    # if the question is malformed or invalid.
    if math_operator in OPERATORS and len(question) == 1:
        raise ValueError("syntax error")
