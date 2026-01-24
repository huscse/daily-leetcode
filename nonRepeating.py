"""
    01 / 24 / 2026 - First Non-Repeating Character (Index)

Problem: First Non-Repeating Character (Index)

Write a function that takes a string s and returns the index of the first character that appears only once in the string.

If no such character exists, return -1.

Rules

Characters are case-sensitive ('a' ≠ 'A')

Return the index, not the character

The order of the string matters

Examples

Input:
s = "leetcode"

Output:
0
('l' appears once and is first)

Input:
s = "loveleetcode"

Output:
2
('v' is the first non-repeating character)

Input:
s = "aabb"

Output:
-1
"""

"""
Solution:
 - Use a hashmap to store each character and its frequency
 - Loop through the string and update counts in the hashmap
 - Loop through the string again in order:
     - If a character’s count is 1, return its index
 - If no such character exists, return -1
"""

def firstUniqChar(s):
    freq = {}

    # First pass: count character frequencies
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Second pass: find first character with count 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1


print(firstUniqChar("leetcode"))       
print(firstUniqChar("loveleetcode"))   
print(firstUniqChar("aabb"))           
