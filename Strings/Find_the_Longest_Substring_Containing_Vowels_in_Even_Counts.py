"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. 
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

 

Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
"""
### TLE 39/53 

class Solution:
    def checkEven(self, res, i, j):
        d1 = res[i]
        d2 = res[j]
        for k in d1.keys():
            if (d1[k]-d2[k])%2!=0:
                return -1
        return i-j
            
    def findTheLongestSubstring(self, s: str) -> int:
        d = {
            "a":0,
            "e":0,
            "i":0,
            "o":0,
            "u":0
        }
        
        if len(s)<=1:
            return 0
        
        res = [d.copy()]
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            res.append(d.copy())
        maxLength = -1
        for i in range(1,len(res)):
            for j in range(0, i):
                maxLength = max(maxLength, self.checkEven(res,i,j))
        return maxLength
                
        
        
