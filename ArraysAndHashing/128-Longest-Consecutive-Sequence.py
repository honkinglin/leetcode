# https://leetcode.com/problems/longest-consecutive-sequence/description/
# https://www.youtube.com/watch?v=P6RZZMu_maU

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestNum = 0
        numSet = set(nums)

        for n in nums:
            # check whether the current number is the start of the sequence
            # if there is a smaller consecutive number, then we will find it later and start counting again
            if (n - 1) not in numSet:
                length = 1
                # keep increasing the length to see if it exists in the array
                while (n + length) in numSet:
                    length += 1
                longestNum = max(length, longestNum)
        
        return longestNum
