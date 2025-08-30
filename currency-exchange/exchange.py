"""
Functions for calculating steps in exchanging currency.

Python numbers documentation:
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling:
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    Return the value of the exchanged currency.

    Note: If your currency is USD and you want to exchange USD for EUR with
    an exchange rate of `1.20`, then `1.20 USD == 1 EUR`.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """
    Return the amount of money that "is left" from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value  # pylint: disable=R0801


def get_value_of_bills(denomination: float, number_of_bills: float) -> float:
    """
    Return only the total value of the bills (excluding fractional amounts)
    the booth would give back.

    The total you receive must be divisible by the value of one "bill" or unit,
    which can leave behind a fraction or remainder.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """
    Return the _number of currency bills_ that you can receive within the given _amount_.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """
    Return the _leftover amount_ that cannot be returned from your starting _amount_
    given the denomination of bills.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


# pylint: disable=R0801
def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """
    Return the maximum value of the new currency after calculating
    the *exchange rate* plus the *spread*.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    total_exchange_rate = exchange_rate + (exchange_rate * spread / 100)
    foreign_currency = exchange_money(budget, total_exchange_rate)
    bills = get_number_of_bills(foreign_currency, denomination)
    return int(get_value_of_bills(bills, denomination))
