"""
    02 / 01 / 2026 - Find the Single Number

You are given a non-empty array of integers where every element appears twice except for one.

Find and return the element that appears only once.

Rules

Every number appears exactly twice, except one

You must find the single one

Order does not matter

Examples

Input:
[2, 2, 1]

Output: 1

Input:
[4, 1, 2, 1, 2]

Output: 4

Input: [1]

Output: 1
"""

""" 
Solution:
 - Use a hashmap to count the frequency of each number
 - Loop through the hashmap
 - Return the number whose frequency is exactly 1
"""

def singleNumber(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for item, value in freq.items():
        if value == 1:
            return item
        
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([2, 2, 1]))


