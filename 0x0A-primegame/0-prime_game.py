#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Function is a game
    params:
        x: Number of rounds
        nums: Array of n (integers)
    returns:
        Name of the player that won most rounds
        None if a winner cannot be determined
    assumptions:
        n and x will not be larger than 10000
    """
    def sieve_of_eratosthenes(n):
        """Returns an array of prime numbers up to n."""
        sieve = [True] * (n+1)
        sieve[0], sieve[1] = False, False
        p = 2
        while p*p <= n:
            if sieve[p]:
                for i in range(p*p, n+1, p):
                    sieve[i] = False
            p += 1
        primes = [i for i in range(n+1) if sieve[i]]
        return primes

    primes = sieve_of_eratosthenes(max(nums))
    primes_count = len(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
