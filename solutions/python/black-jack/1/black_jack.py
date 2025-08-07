"""
Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card) -> int:
    """
    Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in 'JKQ':
        return 10
    elif card == 'A':
        return 1

    return int(card)


def higher_card(card_one, card_two) -> str | tuple[str, str]:
    """
    Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one

    return card_two


def value_of_ace(card_one, card_two) -> int:
    """
    Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    total: int = value_of_card(card_one) + value_of_card(card_two)
    # Hint: if we already have an ace in hand, then the value for the upcoming ace would be 1.
    if card_one == 'A' or card_two == 'A':
        return 1
    # The value of the hand with the ace needs to be as high as possible without going over 21.
    elif 21 - total >= 11:
        return 11

    return 1


def is_blackjack(card_one, card_two) -> bool:
    """
    Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    # If a player is dealt an ace (A) and a ten-card (10, K, Q, or J)
    # as their first two cards, then the player has a score of 21.
    if card_one == 'A' and card_two in ('J', 'Q', 'K', '10'):
        return True
    elif card_two == 'A' and card_one in ('J', 'Q', 'K', '10'):
        return True

    return False


def can_split_pairs(card_one, card_two) -> bool:
    """
    Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return True

    return False


def can_double_down(card_one, card_two) -> bool:
    """
    Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
