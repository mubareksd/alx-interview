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


if __name__ == "__main__":
    for line in sys.stdin:
        data = line.split()
        status = data[-2]
        size = int(data[-1])
        if status in stats.keys():
            stats[status] += 1
        total += size
        count += 1
        if count == 10:
            print("File size: {}".format(total))
            for key, value in sorted(stats.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            count = 0
