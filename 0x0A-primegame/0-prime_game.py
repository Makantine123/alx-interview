#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """Prime Numbers selection game"""

    def SieveOfEratosthenes(n):
        """Returns a list of prime numbers up to interger n"""
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p] is True):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        primelist = []
        for p in range(2, n + 1):
            if prime[p]:
                primelist.append(p)
        return primelist

    mariaWins = 0
    benWins = 0
    for k in range(x):
        n = nums[k]
        primelist = SieveOfEratosthenes(n)
        size = len(primelist)
        if (size % 2 == 0):
            benWins += 1
        else:
            mariaWins += 1

    if benWins > mariaWins:
        return "Ben"
    elif mariaWins > benWins:
        return "Maria"

    return None
