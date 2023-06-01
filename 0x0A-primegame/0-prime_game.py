#!/usr/bin/python3
"""0-prime_game module
"""


def isWinner(x, nums):
    """determine whoo the winner of each game is

    Args:
        x (int): number of rounds
        nums (list[int]): array of n

    Returns:
        str: name of the player that won the most rounds
    """
    maria, ben = 0, 0
    if not nums or x < 1:
        return None
    for i in range(x):
        if nums[i] % 2 == 0:
            maria += 1
        if nums[i] % 2 != 0:
            ben += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
