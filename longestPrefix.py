"""
    01 / 223/ 2026 - Longest Increasing Prefix

Write a function that takes a list of integers and returns the length of the longest strictly increasing prefix.

A prefix means the sequence must start from the first element and continue without skipping.

Rules

The prefix must start at index 0

Each next number must be greater than the previous one

Stop counting as soon as the sequence is no longer increasing

Examples

Input:
[1, 3, 5, 7, 6, 8]

Prefix:
[1, 3, 5, 7]

Output:
4

Input:
[5, 4, 3, 2]

Prefix:
[5]

Output:
1

Input:
[2, 2, 3, 4]

Prefix:
[2] (not strictly increasing)

Output:
1

Input:
[]

Output:
0

Requirements

Input: list of integers (may be empty)

Output: integer length of the longest increasing prefix
"""


"""
Solution:
 - If the array is empty, return 0
 - Initialize a count to 1 (the first element always counts)
 - Loop through the array starting from the second element
 - If the current element is greater than the previous element:
     - Increment the count
 - Otherwise:
     - Stop the loop and return the count
 - Return the count
"""
