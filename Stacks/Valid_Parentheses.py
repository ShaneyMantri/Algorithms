"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        st = []
        o=list("([{")
        c=list("})]")
        if s[0] in c:
            return False
        st.append(s[0])
        i=1
        n = len(s)
        while i<n:
            if s[i] in c:
                if not st:
                    return False
                if s[i]==")" and st[-1]!="(":
                    return False
                elif s[i]=="]" and st[-1]!="[":
                    return False
                elif s[i]=="}" and st[-1]!="{":
                    return False

                else:
                    st.pop()
            else:
                st.append(s[i])
            i+=1
                
        
        if st:
            return False
        return True
