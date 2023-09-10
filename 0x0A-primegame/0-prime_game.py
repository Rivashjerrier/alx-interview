#!/usr/bin/python3
"""
0-prime_game.py module
"""


def isWinner(x, nums):
    """
    Returns name of the player that won the most rounds
    """
    maria = 0
    ben = 0
    for n in nums:
        if n % 2 == 0 or is_prime(n):
            ben += 1
        else:
            maria += 1

    if maria == ben:
        return None
    elif maria > ben:
        return "Maria"
    else:
        return "Ben"


def is_prime(num):
    """
    Checks if a number is a prime number
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True
