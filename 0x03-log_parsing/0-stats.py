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


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            size = 0
            try:
                data = line.split()
                status = data[-2]
                size += int(data[-1])
                if status in stats:
                    stats[status] += 1
            except Exception:
                pass
            total += size
            if count % 10 == 0:
                print_stats(stats, total)
    except KeyboardInterrupt:
        print_stats(stats, total)
        raise
