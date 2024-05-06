# https://leetcode.com/problems/3sum/description/
# https://www.youtube.com/watch?v=jzZsG8n2R9A

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the array
        nums.sort()

        ans, n = [], len(nums)

        for i in range(n - 2):
            x = nums[i]

            # filter duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # when the sum of the two smallest numbers is greater than 0, there is no solution for the rest of the values
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            # if the current value and the sum of the two largest numbers are less than 0, there is no solution for this loop
            if x + nums[-1] + nums[-2] < 0:
                continue

            # define two pointers
            j, k = i + 1, n - 1
            while j < k:
                # sum of three values
                s = x + nums[j] + nums[k]

                if s < 0:
                    j += 1

                if s > 0:
                    k -= 1

                if s == 0:
                    ans.append([x, nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # filter duplicate values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # filter duplicate values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
