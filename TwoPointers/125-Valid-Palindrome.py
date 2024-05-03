# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Check if the character is alphanumeric from the left
            while not s[left].isalnum() and left < right:
                left += 1
            
            # Check if the character is alphanumeric from the right
            while not s[right].isalnum() and left < right:
                right -= 1
            
            # If the characters are the same, move on to the next pair
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            # If the characters are different, return False
            else:
                return False

        return True
