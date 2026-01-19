"""
    01 / 19 / 2026 - 217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""

"""
SOLUTION:

- Use a set - a set does not contain any duplicates
- Loop through the array and see if the num exists in the set
- If yes then the current value is a duplicate - return True
- If no, we add the num to the set 
- Return False and in the end

"""