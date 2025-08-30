# pylint: disable=C0301
"""
Unit tests for the steps function implementing the Collatz Conjecture.

Tests include validation for zero, negative, even, odd values, and large numbers.
Ensures ValueError is raised for invalid input according to Collatz rules.
"""

# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/collatz-conjecture/canonical-data.json
# File last updated on 2023-07-20

import unittest

from collatz_conjecture import (
    steps,
)


# pylint: disable=C0116
class CollatzConjectureTest(unittest.TestCase):
    """Unit tests for the functions related to the Collatz conjecture."""

    def test_zero_steps_for_one(self):
        self.assertEqual(steps(1), 0)

    def test_divide_if_even(self):
        self.assertEqual(steps(16), 4)

    def test_even_and_odd_steps(self):
        self.assertEqual(steps(12), 9)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(steps(1000000), 152)

    def test_zero_is_an_error(self):
        with self.assertRaises(ValueError) as err:
            steps(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],
                         "Only positive integers are allowed")

    def test_negative_value_is_an_error(self):
        with self.assertRaises(ValueError) as err:
            steps(-15)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],
                         "Only positive integers are allowed")
