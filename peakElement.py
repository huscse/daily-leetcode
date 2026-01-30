"""
    01 / 30 / 2026 - Problem: Find the Peak Element
    
Write a function that takes an array of integers nums and returns the index of any peak element.

A peak element is an element that is strictly greater than its neighbors.

For the first element, only compare with the right neighbor

For the last element, only compare with the left neighbor

You may assume:

nums[i] != nums[i+1]

A peak always exists

Examples

Input:
[1, 2, 3, 1]

Output: 2 (because 3 is a peak)

Input:
[1, 2, 1, 3, 5, 6, 4]

Output: 1 or 5 (both are valid peaks)
""" 