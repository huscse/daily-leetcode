"""
    02 / 06 / 2026 - Count Elements Smaller Than the Current Number

Given an array nums, return a new array result such that:

result[i] = number of elements in nums that are smaller than nums[i]

Example

Input:
[8, 1, 2, 2, 3]

Output:
[4, 0, 1, 1, 3]

Explanation:

8 → four numbers smaller

1 → none smaller

2 → one number smaller (1)

2 → one number smaller

3 → three numbers smaller (1,2,2)
"""

""" 
Solution:
 - Create a result array filled with 0s
 - For each index i in nums:
     - Loop through nums again:
         - If nums[j] < nums[i]:
             - Increment result[i]
 - Return result
"""

def countElems(nums):
    n = len(nums)
    result = [0] * n

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                result[i] += 1

    return result

print(countElems([8, 1, 2, 2, 3]))