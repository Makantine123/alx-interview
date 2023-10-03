#!/usr/bin/python3
"""
Unlock boxes Modules
"""


def canUnlockAll(boxes):
    """
    Function method that determines if all the boxes can be opened
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
