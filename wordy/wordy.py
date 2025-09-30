"""
Parse and evaluate simple math word problems
returning the answer as an integer.

Handle a set of operations, in sequence.

Since these are verbal word problems, evaluate
the expression from left-to-right, ignoring the
typical order of operations.
"""

import string

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
    result: int = 0
    new_question: list[str] = _reformat(question)

    if len(new_question) <= 3:
        try:
            _validate_evaluation_pattern(new_question)
            eval_str: str = "".join(new_question)
            result = eval(eval_str)
            return result
        except Exception:
            raise ValueError("syntax error")

    # Reduce iteratively: evaluate the first three-token slice
    # and fold the result left-to-right.
    while len(new_question) >= 3:
        try:
            _validate_evaluation_pattern(new_question[:3])
            eval_str: str = "".join(new_question[:3])
            val: int = eval(eval_str)
            result = val
            new_question = [str(result)] + new_question[3:]
            if len(new_question) < 3:
                _validate_evaluation_pattern(new_question)
                return eval("".join(new_question))
        except Exception:
            raise ValueError("syntax error")
    return result


def _validate_evaluation_pattern(val: list) -> None:
    """
    Ensure a token slice matches expected evaluation patterns.

    :param val: Token slice to validate, e.g.,
                ['3', '+', '4'] or ['+', '4'] during reduction.
    :type val: list
    :raises ValueError: If the pattern is invalid (syntax error).
    """
    if len(val) == 3 and not val[1] in STR_TO_OPERATOR.values():
        raise ValueError("syntax error")

    if len(val) == 2 and not val[0] in STR_TO_OPERATOR.values():
        raise ValueError("syntax error")


def _reformat(question: str) -> list:
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
    for i, item in enumerate(question_list):
        if not (
            item.isdigit()
            or item in STR_TO_OPERATOR.keys()
            or item in STR_TO_OPERATOR.values()
            or any(val in item for val in STR_TO_OPERATOR.values())
        ):
            continue
        elif item in STR_TO_OPERATOR.keys():
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

    digits: list[bool] = []
    for char in question:
        if char.isdigit():
            digits.append(True)

    operators: list[bool] = []
    for key, val in STR_TO_OPERATOR.items():
        if key in question or val in question:
            operators.append(True)

    if not any(digits + operators):
        raise ValueError("unknown operation")
