from parameterized import parameterized
import unittest
import pytest

from black_jack import (
    value_of_card,
    higher_card,
    value_of_ace,
    is_blackjack,
    can_split_pairs,
    can_double_down
)


class BlackJackTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    @parameterized.expand([
        ('2', 2), ('5', 5), ('8', 8),
        ('A', 1), ('10', 10), ('J', 10),
        ('Q', 10), ('K', 10),
    ])
    def test_value_of_card(self, card, expected):
        actual_result = value_of_card(card)
        error_msg = (f'Called value_of_card({card}). '
                     f'The function returned {actual_result} '
                     f'as the value of '
                     f'the {card} card, '
                     f'but the test expected {expected} as the '
                     f'{card} card value.')
        self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=2)
    @parameterized.expand([
        ('A', 'A', ('A', 'A')),
        ('10', 'J', ('10', 'J')),
        ('3', 'A', '3'),
        ('3', '6', '6'),
        ('Q', '10', ('Q', '10')),
        ('4', '4', ('4', '4')),
        ('9', '10', '10'),
        ('6', '9', '9'),
        ('4', '8', '8'),
    ])
    def test_higher_card(self, card_one, card_two, expected):
        actual_result = higher_card(card_one, card_two)
        error_msg = (f'Called higher_card({card_one}, {card_two}). '
                     f'The function returned {actual_result}, '
                     f'but the test expected {expected} as the result for '
                     f'the cards {card_one, card_two}.')
        self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    @parameterized.expand([
        ('2', '3', 11), ('3', '6', 11), ('5', '2', 11),
        ('8', '2', 11), ('5', '5', 11), ('Q', 'A', 1),
        ('10', '2', 1), ('7', '8', 1), ('J', '9', 1),
        ('K', 'K', 1), ('2', 'A', 1), ('A', '2', 1),
    ])
    def test_value_of_ace(self, card_one, card_two, ace_value):
        actual_result = value_of_ace(card_one, card_two)
        error_msg = (f'Called value_of_ace({card_one}, {card_two}). '
                     f'The function returned {actual_result}, '
                     f'but the test expected {ace_value} '
                     f'as the value of an ace card '
                     f'when the hand includes {card_one, card_two}.')
        self.assertEqual(actual_result, ace_value, msg=error_msg)

    @pytest.mark.task(taskno=4)
    @parameterized.expand([
        (('A', 'K'), True), (('10', 'A'), True),
        (('10', '9'), False), (('A', 'A'), False),
        (('4', '7'), False), (('9', '2'), False),
        (('Q', 'K'), False),
    ])
    def test_is_blackjack(self, hand, expected):
        actual_result = is_blackjack(*hand)
        error_msg = (f'Called is_blackjack({hand[0]}, {hand[1]}). '
                     f'The function returned {actual_result}, '
                     f'but hand {hand} {"is" if expected else "is not"} '
                     f'a blackjack.')
        self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=5)
    @parameterized.expand([
        (('Q', 'K'), True), (('6', '6'), True),
        (('A', 'A'), True), (('10', 'A'), False),
        (('10', '9'), False),
    ])
    def test_can_split_pairs(self, hand, expected):
        actual_result = can_split_pairs(*hand)
        error_msg = (f'Called can_split_pairs({hand[0]}, {hand[1]}). '
                     f'The function returned {actual_result}, '
                     f'but hand {hand} '
                     f'{"can" if expected else "cannot"} '
                     f'be split into pairs.')
        self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=6)
    @parameterized.expand([
        (('A', '9'), True), (('K', 'A'), True),
        (('4', '5'), True), (('A', 'A'), False),
        (('10', '2'), False), (('10', '9'), False),
    ])
    def test_can_double_down(self, hand, expected):
        actual_result = can_double_down(*hand)
        error_msg = (f'Called can_double_down({hand[0]}, {hand[1]}). '
                     f'The function returned {actual_result}, '
                     f'but hand {hand} {"can" if expected else "cannot"} '
                     f'be doubled down.')
        self.assertEqual(actual_result, expected, msg=error_msg)