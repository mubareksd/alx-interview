#!/usr/bin/python3
"""0-making_change module
"""


def makeChange(coins, total):
    """makeChange function that determines the fewest
    number of coins needed to meet a given amount total.

    Args:
        coins (list): list of the values of the coins in your possession
        total (number): total to reach with coins

    Returns:
        number: number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
