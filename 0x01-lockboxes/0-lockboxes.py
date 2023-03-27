#!/usr/bin/python3
"""0-lockboxes
"""


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (Array): Array of boxes

    Returns:
        Boolean: true if all boxes can be opened, else false
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
