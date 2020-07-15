"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        for i in strs:
            t = list(i)
            t.sort()
            tj = ''.join(t)
            if tj in d:
                d[tj].append(i)
            else:
                d[tj]=[i]
        return d.values()
        
