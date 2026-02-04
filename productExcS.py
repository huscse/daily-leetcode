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

Output: None

Input: [5, 1, 5, 3]

Output: 3
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