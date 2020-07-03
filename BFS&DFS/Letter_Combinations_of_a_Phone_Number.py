"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from collections import deque
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        d1 = deque([])
        for i in dic[digits[0]]:
            d1.append(i)
        d2 = deque([])
        for i in range(1,len(digits)):
            while d1:
                t = d1.popleft()
                for j in dic[digits[i]]:
                    d2.append(str(t)+str(j))
            temp = d2.copy()
            d2 = deque([])
            d1 = temp.copy()
            
        return d1v
