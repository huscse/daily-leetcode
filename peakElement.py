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


"""
Solution:
 - Loop through the array
 - If the array has 1 element, that index (0) is a peak
-  Check the first element:
    - if nums[0] > nums[1], return 0
-  Check the middle elements (1 to n-2):
    - if nums[i] > nums[i-1] AND nums[i] > nums[i+1], return i
-  Check the last element:
    - if nums[n-1] > nums[n-2], return n-1
"""

def findPeakElement(nums):
    n = len(nums)

    # Case 1: only one element
    if n == 1:
        return 0

    # Case 2: first element is a peak
    if nums[0] > nums[1]:
        return 0

    # Case 3: last element is a peak
    if nums[n - 1] > nums[n - 2]:
        return n - 1

    # Case 4: check middle elements
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

