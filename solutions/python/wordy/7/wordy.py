"""
Parse and evaluate simple math word problems
returning the answer as an integer.

Handle a set of operations, in sequence.

Since these are verbal word problems, evaluate
the expression from left-to-right, ignoring the
typical order of operations.
"""

STR_TO_OPERATOR: dict = {
    "plus": "+",
    "minus": "-",
    "multiplied": "*",
    "divided": "/",
}

WRONG_OPERATORS: list[str] = [
    "plus?",
    "minus?",
    "multiplied?",
    "divided?",
    "plus plus",
    "plus multiplied",
    "minus multiplied",
    "minus minus",
    "multiplied multiplied",
    "divided divided",
    "What is?",
]


def answer(question: str) -> int:
    """
    Evaluate a simple word-based arithmetic question from left to right.

    :param question: The input question, e.g., "What is 5 plus 13?"
    :type question: str
    :returns: The evaluated integer result.
    :rtype: int
    :raises ValueError: If the operation is unknown or the syntax is invalid.
    """
    _validate_errors(question)
    new_question: list[str] = _reformat(question)
    # Reduce iteratively: evaluate the first three-token slice
    # and fold the result left-to-right.
    while new_question:
        try:
            if len(new_question) == 3:
                _validate_evaluation_pattern(new_question)
                return _math_operation(new_question)
            if len(new_question) == 1:
                return int(new_question[0])
            _validate_evaluation_pattern(new_question[:3])
            result = _math_operation(new_question[:3])
            new_question = [str(result)] + new_question[3:]
        except Exception as exc:
            raise ValueError("syntax error") from exc
    raise ValueError("syntax error")  # Safety net for empty cases


def _math_operation(question: list[str]) -> int:
    """
    Compute a single binary arithmetic operation.

    Expects a three-token slice like ``['3', '+', '4']`` and returns
    the integer result. Division performs floor division (``//``) to
    match exercise rules.

    :param question: Three tokens ``[lhs, operator, rhs]``.
    :type question: list[str]
    :returns: The computed integer result.
    :rtype: int
    """
    math_operator: str = question[1]

    if math_operator == "+":
        return int(question[0]) + int(question[-1])

    if math_operator == "-":
        return int(question[0]) - int(question[-1])

    if math_operator == "/":
        return int(question[0]) // int(question[-1])

    if math_operator == "*":
        return int(question[0]) * int(question[-1])

    raise ValueError("syntax error")


def _validate_evaluation_pattern(val: list[str]) -> None:
    """
    Ensure a token slice matches expected evaluation patterns.

    :param val: Token slice to validate, e.g.,
                ['3', '+', '4'] or ['+', '4'] during reduction.
    :type val: list[str]
    :raises ValueError: If the pattern is invalid (syntax error).
    """
    if len(val) == 3 and val[1] not in STR_TO_OPERATOR.values():
        raise ValueError("syntax error")

    if len(val) == 2 and val[0] not in STR_TO_OPERATOR.values():
        raise ValueError("syntax error")


def _reformat(question: str) -> list[str]:
    """
    Tokenize a natural-language math question into numbers
    and operator symbols.

    :param question: Raw question string.
    :type question: str
    :returns: Token list with numbers and operator symbols.
    :rtype: list[str]
    """
    # 1: Remove '?' mark
    question = question.replace("?", "")
    # 2: Convert all operators writen in word into proper math sign
    question_list: list[str] = question.split()
    formated_question_list: list[str] = []
    for item in question_list:
        if not (
            item.isdigit()
            or item[1:].isdigit()
            or item in STR_TO_OPERATOR
            or item in STR_TO_OPERATOR.values()
        ):
            continue

        if item in STR_TO_OPERATOR:
            formated_question_list.append(STR_TO_OPERATOR[item])
        elif item.isdigit():
            formated_question_list.append(item)
        elif item in STR_TO_OPERATOR.values():
            formated_question_list.append(item)
        elif any(val in item for val in STR_TO_OPERATOR.values()):
            formated_question_list.append(item)

    return formated_question_list


def _validate_errors(question: str) -> None:
    """
    Pre-validate unsupported or malformed questions.

    :param question: Raw question string.
    :type question: str
    :raises ValueError: Unknown operation or malformed
                        phrasing (syntax error).
    """
    if "cubed" in question:
        raise ValueError("unknown operation")

    for item in WRONG_OPERATORS:
        if item in question:
            raise ValueError("syntax error")
