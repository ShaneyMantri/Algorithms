"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the character i in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
"""


# METHOD 1
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        res = [0]*n
        if n==1:
            return 0
        for i,letter in enumerate(s):
            res[i] = [letter, i]
        
        s = 0 
        i = 0
        while i<len(res)-1:
            if res[i][0] == res[i+1][0]:
                if cost[res[i][1]] < cost[res[i+1][1]]:
                    s+=cost[res[i][1]]
                    res[i] = res[i+1].copy()
                    res.pop(i+1)
                    continue
                else:
                    s+=cost[res[i+1][1]]
                    res.pop(i+1)
                    continue
            else:
                i+=1
        return s               

       
# METHOD 2

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        res = [0]*n
        if n==1:
            return 0
        st = 0
        en = 1
        res = 0
        while en<n:
            if s[st] == s[en]:
                if st != en:
                    en+=1
            else:
                res += sum(cost[st:en]) - max(cost[st:en])
                st = en
                en+=1
        if s[st] == s[en-1]:
            res += sum(cost[st:en]) - max(cost[st:en])
        return res
        
