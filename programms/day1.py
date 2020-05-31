"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

import itertools

integer_list = [10, 15, 3, 7]
k = 17
for numbers in itertools.combinations(integer_list, 2):
    suma = sum(numbers)
    if suma != k:
        pass
    if suma == k:
        print(suma)
