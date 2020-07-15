"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 =list(t)
        s1.sort()
        t1.sort()
        if s1!=t1:
            return False
        return True
            
        
