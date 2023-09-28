#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """
    Returns a lists of intergers representing the Pascal Triangle
    """
    mylist = []

    if n <= 0:
        return mylist

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j in [0, i]:
                row.append(1)
            else:
                row.append(mylist[i - 1][j - 1] + mylist[i - 1][j])
        mylist.append(row)
    return mylist
