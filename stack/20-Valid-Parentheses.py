# https://leetcode.com/problems/valid-parentheses/description/
# https://www.youtube.com/watch?v=WTzjTskDFMg

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # If the character is an open bracket, add it to the stack
            if c in "([{":
                stack.append(c)
            # If the character is a closing bracket, check if the top of the stack is the corresponding open bracket
            elif len(stack) == 0 or stack[-1] != map[c]:
                return False
            # If the character is a closing bracket and the top of the stack is the corresponding open bracket, remove it from the stack
            else:
                stack.pop()

        return len(stack) == 0
