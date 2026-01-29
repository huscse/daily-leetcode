"""
    01 / 28 / 2026 - Find the Majority Element

Write a function that takes an array of integers nums and returns the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.

You may assume that a majority element always exists.

Rules

Input: list of integers nums

Output: the majority element

Majority element appears more than half the time

Examples

Input:
[3, 2, 3]

Output: 3

Input:
[2, 2, 1, 1, 1, 2, 2]

Output: 2
"""

""" 
Solution:
 - Create a hashmap to store each number and its frequency
 - Loop through the array and update counts in the hashmap
 - Keep track of the element with the maximum count
 - Return the element whose count is greater than n // 2
"""


def majorityElement(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_count = 0
    maj = None

    for num, count in freq.items():
        if count > max_count:
            max_count = count
            maj = num

    return maj

