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

    def is_prime(num):
        """Check if num is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(num):
        """Returns array of primes"""
        primes = []
        for i in range(1, num + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """Plays game n times"""
        primes = get_primes(n)
        num_primes = len(primes)
        if num_primes % 2 == 0:
            return "Ben"
        return "Maria"

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        winner = play_game(nums[i])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
