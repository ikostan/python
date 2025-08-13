"""
Armstrong Numbers Test Suite Documentation

## Overview

This test suite validates the `is_armstrong_number` function,
ensuring its correct behavior for various types of numbers:

- Single-digit and multi-digit numbers
- Known Armstrong numbers and non-Armstrong numbers

Tests are auto-generated based on canonical data from
[Exercism problem specifications](https://github.com/exercism/problem-specifications/tree/main/exercises/armstrong-numbers/canonical-data.json).

## Structure

- **Framework:** Uses Python's built-in `unittest`.
- **Target Function:** `is_armstrong_number` (imported from `armstrong_numbers` module).

## Test Cases

| Test Description                                        | Input    | Expected Output |
|---------------------------------------------------------|----------|-----------------|
| Zero is an Armstrong number                             | 0        | `True`          |
| Single-digit numbers are Armstrong numbers              | 5        | `True`          |
| No two-digit numbers (e.g. 10) are Armstrong numbers    | 10       | `False`         |
| 153 is an Armstrong number                              | 153      | `True`          |
| 100 is not an Armstrong number                          | 100      | `False`         |
| 9474 is an Armstrong number                             | 9474     | `True`          |
| 9475 is not an Armstrong number                         | 9475     | `False`         |
| 9926315 is an Armstrong number                          | 9926315  | `True`          |
| 9926314 is not an Armstrong number                      | 9926314  | `False`         |

## Usage

To run the tests, ensure `is_armstrong_number` is implemented and run:

```bash
python -m unittest armstrong_numbers_test.py

"""

# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/armstrong-numbers/canonical-data.json
# File last updated on 2023-07-20

import unittest

from armstrong_numbers import (
    is_armstrong_number,
)


class ArmstrongNumbersTest(unittest.TestCase):
    """Armstrong Numbers Test."""

    def test_zero_is_an_armstrong_number(self):
        """
        Test that zero is correctly identified as an Armstrong number.

        This test verifies that the function correctly determines that 0
        is an Armstrong number, as 0^1 == 0.

        :returns: None
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(0), True)

    def test_single_digit_numbers_are_armstrong_numbers(self):
        """
        Test that all single digit numbers are Armstrong numbers.

        :returns: None. Asserts that a single digit number (e.g., 5) is an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(5), True)

    def test_there_are_no_two_digit_armstrong_numbers(self):
        """
        Test that no two-digit numbers are Armstrong numbers.

        :returns: None. Asserts that a two-digit number (e.g., 10) is not an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(10), False)

    def test_three_digit_number_that_is_an_armstrong_number(self):
        """
        Test that 153 is correctly identified as an Armstrong number.

        :returns: None. Asserts that 153 is an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(153), True)

    def test_three_digit_number_that_is_not_an_armstrong_number(self):
        """
        Test that 100 is not identified as an Armstrong number.

        :returns: None. Asserts that 100 is not an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(100), False)

    def test_four_digit_number_that_is_an_armstrong_number(self):
        """
        Test that 9474 is correctly identified as an Armstrong number.

        :returns: None. Asserts that 9474 is an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(9474), True)

    def test_four_digit_number_that_is_not_an_armstrong_number(self):
        """
        Test that 9475 is not identified as an Armstrong number.

        :returns: None. Asserts that 9475 is not an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(9475), False)

    def test_seven_digit_number_that_is_an_armstrong_number(self):
        """
        Test that 9926315 is correctly identified as an Armstrong number.

        :returns: None. Asserts that 9926315 is an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(9926315), True)

    def test_seven_digit_number_that_is_not_an_armstrong_number(self):
        """
        Test that 9926314 is not identified as an Armstrong number.

        :returns: None. Asserts that 9926314 is not an Armstrong number.
        :rtype: NoneType
        """
        self.assertIs(is_armstrong_number(9926314), False)
