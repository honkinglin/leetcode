# https://leetcode.com/problems/contains-duplicate/description/
# Solution: https://www.youtube.com/watch?v=3OamzN90kPg

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums) -> bool:
        # Create a set to store the numbers that have been seen
        seen = set()

        for num in nums:
            if num in seen:
                # If the number is already in the set, return True
                return True
            # Otherwise, add the number to the set
            seen.add(num)

        # If the loop completes, return False
        return False
