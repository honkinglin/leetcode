# https://leetcode.com/problems/product-of-array-except-self/description/
# Solution: https://www.youtube.com/watch?v=bNvIQI2wAjk&themeRefresh=1

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)

        # calc the prefix product
        # 1 2 3 4
        # prefix: 1 1 2 6
        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]

        # The result is the prefix product of the current number multiplied by the suffix product of the current number.
        # 1 2 3 4
        # suffix: 24 12 4 1

        # prefix: 1 1 2 6
        # suffix: 24 12 4 1
        # product: 24 12 8 6
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] = ans[j] * suffix
            suffix *= nums[j]
        
        return ans
