#!/usr/bin/python3
"""
Module contains minOperations function
"""


def minOperations(n):
    """
    Minimum Operations function
    """
    if n <= 1:
        return n

    for i in range(2, n):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
