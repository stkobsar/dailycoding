"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


array_integers = [3, 2, 1]
counter = 0
list_len = []
for (idx, value) in enumerate(array_integers):
    #for idx in array_integers:
    if idx == 0:
        list_idx = array_integers[idx]




