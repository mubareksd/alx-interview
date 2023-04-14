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


def print_stats():
    """print_stats function
    """
    print("File size: {}".format(total))
    for key, value in sorted(stats.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            data = line.split()
            status = data[-2]
            size = int(data[-1])
            if status in stats.keys():
                stats[status] += 1
            total += size
            count += 1
            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        raise
