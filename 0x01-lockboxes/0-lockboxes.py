#!/usr/bin/python3
"""Module to determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    keys = [0]
    for key in keys:
        for box_with_key in boxes[key]:
            if box_with_key not in keys and box_with_key < len(boxes):
                keys.append(box_with_key)
    if len(keys) == len(boxes):
        return True
    return False
