"""
    01 / 21 / 2026 - 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

"""
Solution:
 - Convert all characters in the string to lowercase
 - Use two pointers: left and right
 - left starts at the beginning, right starts at the end
 - While left is less than right:
     - If the left character is not alphanumeric, move left forward
     - Else if the right character is not alphanumeric, move right backward
     - Else if the characters at left and right are not equal, return False
     - Otherwise, move both pointers inward
 - If the loop completes, return True (the string is a palindrome)
"""