"""
    02 / 03 / 2026 - Find the Second Largest Element

Write a function that takes an array of integers and returns the second largest distinct element.

If a second largest element does not exist, return None.

Rules

Elements may be unsorted

Values may repeat

The second largest must be distinct from the largest

Examples

Input: 10, 5, 20, 8]

Output: 10

Input: [3, 3, 3]

Output: None

Input: [1]

Output:
None

Input: [5, 1, 5, 3]

Output: 3
"""

""" 
Solution:
 - Use a hashmap to count the frequency of each number
 - Loop through the hashmap
 - Return the number whose frequency is exactly 1
"""


