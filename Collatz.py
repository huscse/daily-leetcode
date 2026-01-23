"""
    01 / 22 / 2026 - Collatz (3n + 1) Sequence

Write a function that takes a positive integer n and repeatedly applies the following rules until n becomes 1:

    - If n is even, replace n with n / 2

    - If n is odd, replace n with 3n + 1

Your function should return the number of steps it takes to reach 1.

Requirements

Input: an integer n where n >= 1

Output: an integer = number of operations needed to reach 1

If n is already 1, return 0

Example

Input: n = 6

Sequence: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Output: 8 (it took 8 steps)
"""

"""
Solution:
 - Start with the integer n
 - Repeat the process until n becomes 1
 - Keep a counter to track the number of operations
 - If n is even, replace it with n / 2
 - If n is odd, replace it with 3n + 1
 - Increment the counter after each operation
 - Return the counter once n reaches 1
"""

def collatz_sequence(n):
    count = 0
    while n != 1:
        if n % 2 == 0: # n is even -> n / 2
            n = n / 2
            count += 1
        else:          # n is odd -> 3(n) + 1
            n = 3*n + 1
            count += 1

    return count

print(collatz_sequence(6))

# Time: O(T(n)) -> where T(n) is the function
# space: O(1) -> constant, no extra memory used

