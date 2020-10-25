"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
Example 4:

Input: s = "cababc"
Output: false
Explanation: It is impossible to get "cababc" using the operation.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == 'c':
                if len(stack) < 2:
                    return False
                else:
                    if stack[-1] == 'b':
                        stack.pop()
                        if stack[-1] == 'a':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
            else:
                stack.append(s[i])
            i += 1
            # print(stack)
        return True if not stack else False
