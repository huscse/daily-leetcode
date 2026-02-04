"""
    02 / 03 / 2026 - Find the Second Largest Element

Write a function that takes an array of integers and returns the second largest distinct element.

If a second largest element does not exist, return None.

Rules

Elements may be unsorted

Values may repeat

The second largest must be distinct from the largest

Examples

Input: [10, 5, 20, 8]

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

""" 
Solution:
 - Initialize two variables:
     - largest = -infinity
     - second_largest = -infinity
 - Loop through the array:
     - If num > largest:
         - Set second_largest = largest
         - Set largest = num
     - Else if num < largest AND num > second_largest:
         - Set second_largest = num
 - If second_largest is still -infinity:
     - Return None
 - Otherwise, return second_largest
"""


def secondLargest(nums):
    largest = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num

        elif num < largest and num > second:
            second = num

    if second == float('-inf'):
        return None
            
    
    return second


print(secondLargest([5, 1, 5, 3]))
print(secondLargest([10, 5, 20, 8]))
print(secondLargest([3, 3, 3]))

# Time: O(n) -> we loop through the array once
# Space: O(1) -> You only use two variables (largest and second), no extra memory