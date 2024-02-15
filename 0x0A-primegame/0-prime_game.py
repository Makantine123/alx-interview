#!/usr/bin/python3
"""Prime Game Module"""


def is_prime(num):
    """Check if number is a prime number"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Game between Maria and Ben"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(1 for i in range(1, n + 1) if is_prime(i))

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    if maria_wins > ben_wins:
        return "Maria"
    return "Ben"
