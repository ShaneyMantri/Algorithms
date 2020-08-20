"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
"""

from collections import deque 
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)==0:
            return s
        l = list(s)
        stack = deque([])
        q = deque([])
        vow = ['a','e','i', 'o', 'u']
        for i in range(len(l)):
            if l[i].lower() in vow:
                stack.append(l[i])
                q.append(i)
        for i in range(len(stack)):
            ch = stack.pop()
            ind = q.popleft()
            l[ind] = ch
        return ''.join(l)
