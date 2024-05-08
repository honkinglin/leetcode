# https://leetcode.com/problems/container-with-most-water/description/
# https://www.youtube.com/watch?v=UuiTKBwPgAo

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            # find the area of the container
            area = min(height[l], height[r]) * (r - l)
            # update the maximum area if necessary
            ans = max(ans, area)

            # move the pointer with the smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ans
