# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://www.youtube.com/watch?v=YPTqKIgVk-k

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a dictionary (`map`) to store the frequency of each element in the array.
        map = defaultdict(int)
        # Step 2: Create buckets to store elements based on their frequency.
        freq = [[] for i in range(len(nums) + 1)]

        # Step 3: Iterate through the array to populate the `map` dictionary.
        for n in nums:
            map[n] += 1

        # Step 4: Iterate through the items in `map` and distribute elements into the corresponding buckets based on their frequency.
        # 0 1 2 3 ... 
        #   3 2 1 
        for key, val in map.items():
            freq[val].append(key)
        
        # Step 5: Iterate through the buckets from right to left (highest to lowest frequency) and append elements to the answer list until the desired k elements are collected.
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
