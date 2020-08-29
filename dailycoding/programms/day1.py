"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

import itertools


def get_day1(k, list):
    for numbers in itertools.combinations(list, 2):
        suma = sum(numbers)
        if suma != k:
            pass
        if suma == k:
            return suma



