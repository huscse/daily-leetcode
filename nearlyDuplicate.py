"""
    02 / 06 / 2026 - Contains Nearby Duplicate

Given an array of integers nums and an integer k, return True if there are two different indices i and j such that:

nums[i] == nums[j]

|i - j| <= k

Otherwise, return False.

Examples

Input:
nums = [1,2,3,1], k = 3
Output: True
(duplicate 1 within distance 3)

Input:
nums = [1,0,1,1], k = 1
Output: True

Input:
nums = [1,2,3,1,2,3], k = 2
Output: False
"""

"""
Solution:
 - Create a hashmap to store:
     number → last index seen
 - Loop through the array with index i:
     - If number is already in the map:
         - Compute distance = i - last_seen_index
         - If distance <= k:
             - Return True
     - Update the map with current index
 - Return False if no valid pair found
"""

def nearlyDup(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k: # check distance, if <= k return True
                return True
        
        seen[num] = i # add num to map
        
    return False

print(nearlyDup([1,2,3,1,2,3], 2))
print(nearlyDup([1,0,1,1], 1))
print(nearlyDup([1,2,3,1], 3))