"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        num = ["break"]
        st = []
        ret = ''
        for  i in s:
            if i.isnumeric():
                num.append(i)
            elif i.isalpha():
                st.append(i)
            else:
                if i=="]":
                    num.pop()
                    mult = ''
                    while num[-1]!="break":
                        mult = num.pop() + mult
                    temp = ''
                    while st[-1]!="[":
                        temp = st.pop()+temp
                        
                    st.pop()
                    temp = temp*int(mult)
                    st.append(temp)
                elif i=="[":
                    if num[-1].isnumeric():
                        num.append("break")
                    st.append(i)
        return ''.join(st)
