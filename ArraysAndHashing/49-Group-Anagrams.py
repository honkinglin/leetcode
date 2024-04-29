# https://leetcode.com/problems/group-anagrams/description/
# Solution: https://www.youtube.com/watch?v=vzdNOK2oB2E

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # store the sorted string in the map
            # such as:
            # eat ==> aet -> ['eat', 'tea', 'ate']
            # tan ==> atn -> ['nat', 'tan']
            # bat ==> abt -> ['bat']
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
