#!/usr/bin/python3
"""0-minoperations module
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): Number of H characters

    Returns:
        int: Minimum number of operations needed
    """
    if n <= 1:
        return 0

    min_ops = 0
    i = 2
    while i <= n:
        if n % i == 0:
            min_ops += i
            n = n / i
        else:
            i += 1
    return min_ops
