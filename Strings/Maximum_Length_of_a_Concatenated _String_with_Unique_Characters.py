"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""

class Solution:
    s = 0
    def dfs(self, arr, i, temp, d, n):
        self.s = max(self.s, len(temp))
        if i >= n:
            return
        
        for j in range(i, n):
            if len(d[j].intersection(set(temp))) == 0:
                self.dfs(arr, j, temp + list(d[j]), d, n)
        
    def maxLength(self, arr: List[str]) -> int:
        i = 0
        while i < len(arr):
            if len(arr[i]) != len(set(list(arr[i]))):
                arr = arr[:i] + arr[i+1:]
                continue
            i += 1
        if len(arr) == 0:
            return 0
        d = {}
        for ind, ele in enumerate(arr):
            d[ind] = set(list(ele))
        self.s = 0
        self.dfs(arr, 0, [], d, len(arr))
        return self.s
