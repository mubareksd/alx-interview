#!/usr/bin/python3
"""0-prime_game module
"""


def isPrime(n):
    """determine if a number is prime

    Args:
        n (int): number to check

    Returns:
        bool: True if n is prime, False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 and i != n:
            return False
    return True


def primes(n):
    """return a list of prime numbers

    Args:
        n (int): number to check

    Returns:
        list: list of prime numbers
    """
    lss = []
    for i in range(n):
        if isPrime(i):
            lss.append(i)
    return lss


def isWinner(x, nums):
    """determine whoo the winner of each game is

    Args:
        x (int): number of rounds
        nums (list[int]): array of n

    Returns:
        str: name of the player that won the most rounds
    """
    if x < 1 or nums is None or len(nums) < 1:
        return None
    ben = 0
    maria = 0
    for i in range(x):

        if primes(nums[i]) == []:
            ben += 1
        elif len(primes(nums[i])) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None

    return "Maria" if maria > ben else "Ben"
