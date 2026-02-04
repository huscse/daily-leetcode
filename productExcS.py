"""
    02 / 03 / 2026 - Product of Array Except Self

Write a function that takes an array of integers nums and returns a new array output such that:

output[i] = product of all elements in nums except nums[i]

Rules

You cannot use division

The result array must be computed in O(n) time

Try to solve it using O(1) extra space (excluding the output array)

Examples

Input: [1, 2, 3, 4]

Output: [24, 12, 8, 6]

Input: [2, 3, 4, 5]

Output: [60, 40, 30, 24]
"""

"""
 Solution: 
  - Make output array
  - Set output[0] = 1
  - For i from 1 to n-1:
    output[i] = output[i-1] * nums[i-1]

  Pass 2: multiply by “right products”:
  - Set right = 1
  - For i from n-1 down to 0:
    output[i] = output[i] * right
    right = right * nums[i]
"""

def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    for i in range(1, len(nums)):
        output[i] = output[i - 1] * nums[i - 1]

    right = 1

    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output

print(productExceptSelf([2, 3, 4, 5]))
print(productExceptSelf([1, 2, 3, 4]))

# Time: O(n) —> two linear passes
# Space: O(1) -> extra space (output array excluded)