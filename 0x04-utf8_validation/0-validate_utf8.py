#!/usr/bin/python3
"""0-validate_utf8 module
"""


def validUTF8(data):
    """validUTF8 function
    
    Arguments:
        data {list} -- list of integers
    """
    for i in data:
        if i < 0 or i > 255:
            return False
    return True
