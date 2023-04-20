#!/usr/bin/python3
"""UTF-8 Validation Module
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): list of integers

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xff
        if n_bytes == 0:
            mask1 = 1 << 7
            mask2 = 1 << 6
            while mask1 & byte:
                n_bytes += 1
                mask1 = mask1 >> 1
                mask2 = mask2 >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            mask1 = 1 << 7
            mask2 = 1 << 6
            if not (byte & mask1 and not (byte & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
