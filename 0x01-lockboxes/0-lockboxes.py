#!/usr/bin/python3
"""Module to determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    keys = [0]
    for key in keys:
        for keyInBox in boxes[key]:
            if keyInBox not in keys and keyInBoxey < len(boxes):
                keys.append(keyInBox)
    if len(keys) == len(boxes):
        return True
    return False
