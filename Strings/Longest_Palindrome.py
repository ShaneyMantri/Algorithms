"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        even = 0
        res = []
        for k,v in d.items():
            if v%2==0:
                even+=v
            else:
                res.append(v)
        if len(res)>0:
            odd = sum(res)-len(res)+1
            return even+odd
        return even
        
