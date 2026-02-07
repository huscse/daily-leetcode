"""
    02 / 07 / 2026 - Count leaf nodes

Given an array of integers nums, return the pivot index where:

The sum of all elements to the left of the index equals

The sum of all elements to the right of the index

If multiple pivot indices exist, return the leftmost one.
If none exist, return -1.

Examples

Input:
[1, 7, 3, 6, 5, 6]
Output: 3
Left sum = 1 + 7 + 3 = 11, right sum = 5 + 6 = 11

Input:
[1, 2, 3]
Output: -1

Input:
[2, 1, -1]
Output: 0
Left sum = 0, right sum = 1 + (-1) = 0
"""