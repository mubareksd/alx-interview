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
    prime = []
    for i in range(2, n + 1):
        if isPrime(i) and i ** 2 not in prime:
            prime.append(i)
    return prime


def isWinner(x, nums):
    """determine whoo the winner of each game is

    Args:
        x (int): number of rounds
        nums (list[int]): array of n

    Returns:
        str: name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria, ben = 0, 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None

    return "Maria" if maria > ben else "Ben"
