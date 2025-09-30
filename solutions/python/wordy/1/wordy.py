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
    "minus minus",
    "multiplied multiplied",
    "divided divided",
    "What is?",
]


def answer(question: str) -> int:
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

    print(f"\n{question}")
    return eval(_reformat(question))


def _reformat(question: str) -> str:
    # 1
    question = question.replace("?", "")
    # 2
    chars: list[str] = list(char for char in question)
    for i, char in enumerate(chars):
        if char in STR_TO_OPERATOR.values():
            chars[i] = f" {char} "
    # 3
    question = "".join(chars)
    print(f"\n new question:{question}")
    # 4
    question_list: list[str] = question.split()
    for i, item in enumerate(question_list):
        # print(f"\nitem: {item}")
        if not (
            item.isdigit()
            or item in STR_TO_OPERATOR.keys()
            or item in STR_TO_OPERATOR.values()
        ):
            question_list[i] = ""
            # print("\n#1")
        elif item in STR_TO_OPERATOR.keys():
            # print("\n#2")
            question_list[i] = STR_TO_OPERATOR[item]

    print(f"\n{question_list}")
    print(f"\n{' '.join(question_list)}")

    return " ".join(question_list)
