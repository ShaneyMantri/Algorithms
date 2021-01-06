"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        if len(set(s)) == 1:
            return 1
        
        d = {}
        st = 0
        en = 0
        ret = 0
        while en < len(s):
            if s[en] in d:
                new_st = d[s[en]] + 1
                while st < new_st:
                    del d[s[st]]
                    st += 1
            else:
                d[s[en]] = en
                ret = max(ret, en-st+1)
                en += 1
        return ret
