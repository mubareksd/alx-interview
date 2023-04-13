#!/usr/bin/python3
"""0-stats module
"""
import sys


cache = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
        }
size = 0
count = 0

if __name__ == "__main__":
    for line in sys.stdin:
        count += 1
        try:
            data = line.split()
            status = data[-2]
            size += int(data[-1])
            if status in cache:
                cache[status] += 1
        except Exception:
            pass
        if count % 10 == 0:
            print("File size: {}".format(size))
            for key, value in sorted(cache.items()):
                if value:
                    print("{}: {}".format(key, value))
