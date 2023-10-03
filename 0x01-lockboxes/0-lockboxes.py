#!/usr/bin/python3
"""
Unlock boxes Modules
"""


def canUnlockAll(boxes):
    """
    Function method that determines if all the boxes can be opened
    """
    num_of_boxes = len(boxes)
    unlocke_boxes = [False] * num_of_boxes
    unlocke_boxes[0] = True
    keys = boxes[0]

    for key in keys:
        if key < num_of_boxes and not unlocke_boxes[key]:
            unlocke_boxes[key] = True
            keys.extend(boxes[key])

    return all(unlocke_boxes)
