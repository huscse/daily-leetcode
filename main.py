"""
    01 / 18 / 2026 - 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false
"""

"""
SOLUTION:

- Use a stack and a hashmap
- Map closing brackets to their matching opening brackets
- Iterate through each character in the string:
  - If it's an opening bracket, push it onto the stack
  - If it's a closing bracket:
    - Check if the stack is empty or the top doesn't match → return false
    - Otherwise, pop the stack
- At the end, return true if the stack is empty

"""

