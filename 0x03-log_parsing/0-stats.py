#!/usr/bin/python3
"""0-stats module
"""
import sys


stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
        }
total = 0
count = 0


def print_stats(stats, total):
    """print_stats function

    Args:
        stats (dict): stats
        total (int): total
    """
    print(f"File size: {total}")
    for key, value in sorted(stats.items()):
        if value:
            print(f"{key}: {value}")


try:
    for line in sys.stdin:
        ls = line.split()
        key, size = ls[-2], int(ls[-1])
        if key in stats.keys():
            stats[key] += 1
        total += size
        count += 1
        if count == 10:
            count = 0
            print_stats(stats, total)
except KeyboardInterrupt:
    print_stats(stats, total)
    raise
