"""
    01 / 29 / 2026 - Problem: Maximum Consecutive Ones

Write a function that takes a binary array (only 0s and 1s) and returns the maximum number of consecutive 1s in the array.

Rules

Input contains only 0 and 1

Consecutive means adjacent

Return the maximum streak of 1s

Examples

Input:
[1, 1, 0, 1, 1, 1]

Output: 3

Input:
[1, 0, 1, 1, 0, 1]

Output: 2

Input:
[0, 0, 0]

Output: 0
""" 

"""
Solution:
 - Initialize current_count = 0 and max_count = 0
 - Loop through the array:
     - If the number is 1:
         - Increment current_count
         - Update max_count if current_count is larger
     - If the number is 0:
         - Reset current_count to 0
 - Return max_count
"""

def MaxOnes(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        
        elif num == 0:
            count = 0

    return max_count

print(MaxOnes([1, 0, 1, 1, 0, 1]))
print(MaxOnes([1, 1, 0, 1, 1, 1]))