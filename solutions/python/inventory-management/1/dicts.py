"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    """
    Create a dict that tracks the amount (count) of each element
    on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory: dict = {}
    for item in items:
        inventory[item] = items.count(item)
    return inventory


def add_items(inventory: dict, items: list) -> dict:
    """
    Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in set(items):
        count: int = items.count(item)
        if item in inventory:
            inventory[item] += count
        else:
            inventory[item] = count
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """
    Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in set(items):
        if item in inventory:
            quantity: int = items.count(item)
            if inventory[item] >= quantity:
                inventory[item] -= quantity
            else:
                inventory[item] = 0
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """
    Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed.
             Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory: dict) -> list:
    """
    Create a list containing only available
    (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the
             inventory dictionary.
    """
    return [(key, inventory[key]) for key in inventory if inventory[key] != 0]
