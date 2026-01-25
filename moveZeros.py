"""
    01 / 25 / 2026 - Move Zeros to the End

Problem: Move Zeros to the End

Write a function that takes an array of integers and moves all zeros to the end of the array while preserving the order of non-zero elements.

You must do this in-place.

Rules

Maintain the relative order of non-zero elements

Modify the array directly (no extra arrays)

Return nothing (or return the array, depending on language)

Examples

Input:
[0, 1, 0, 3, 12]
 p  i
[1, 0, 0, 3, 12]
       p      i
[1, 3, 0, 0, 12]
       p      i
[1, 3, 12, 0, 0]


Output:
[1, 3, 12, 0, 0]

Input:
[0, 0, 0]

Output:
[0, 0, 0]

Input:
[1, 2, 3]

Output:
[1, 2, 3]
"""

"""
Solution:
 - Use a pointer (pos) to track where the next non-zero should go
 - Loop through the array from left to right
 - When you see a non-zero:
     - Place it at index pos
     - Increment pos
 - After the loop, fill the remaining positions (from pos to end) with zeros

"""

