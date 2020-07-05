"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""
class Solution:
    def dfs(self,sub, S, i, n):
        if sub not in self.res and i==(n):
            self.res.append(sub)
            return
        if i>=n:
            return
        
        if S[i].isalpha():
            if S[i].islower():
                self.dfs(sub+S[i].upper(),S, i+1, n)
                self.dfs(sub+S[i], S, i+1, n)
            
            elif S[i].isupper():
                self.dfs(sub+S[i].lower(), S, i+1, n)
                self.dfs(sub+S[i], S, i+1, n)
        else:
            self.dfs(sub+S[i], S, i+1, n)
            
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S)==1:
            if S[0].isalpha():
                return [S[0].lower(), S[0].upper()]
            return [S]
        self.res = []
        self.dfs('', S,0,len(S))
        return self.res
        
