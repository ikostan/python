"""
Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

- "Sure." This is his response if you ask him a question, such as "How are you?"
  The convention used for questions is that it ends with a question mark.
- "Whoa, chill out!" This is his answer if you YELL AT HIM.
  The convention used for yelling is ALL CAPITAL LETTERS.
- "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
- "Fine. Be that way!" This is how he responds to silence.
  The convention used for silence is nothing, or various combinations of whitespace characters.
- "Whatever." This is what he answers to anything else.
"""


def response(hey_bob: str) -> str:
    """
    Determine what Bob will reply to someone when they say something to him or ask him a question.

    :param hey_bob: str
    :return: str
    """
    # Empty string -> responds to silence.
    if not hey_bob.strip():
        return "Fine. Be that way!"

    # Yell at Bob
    if hey_bob == hey_bob.upper() and any(char.isalpha() for char in hey_bob):
        # Yell a question
        if is_question(hey_bob):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    # Ask question
    if is_question(hey_bob):
        return "Sure."

    # Anything else.
    return "Whatever."


def is_question(hey_bob: str) -> bool:
    """
    Determine if you ask/yell a question.

    :param hey_bob: str
    :return: bool
    """
    return "?" in hey_bob and hey_bob.strip()[-1] == '?'
