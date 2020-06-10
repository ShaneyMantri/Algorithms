"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    
    res = []
    def generate(self, s, lc, rc, n):
        if lc==n:
            if rc==n:
                self.res.append(s)
                return self.res
            else:
                self.generate(s+')', lc, rc+1, n)
                    
        if lc<n:
            if lc==rc:
                self.generate(s+'(', lc+1, rc, n)
            if lc>rc:
                self.generate(s+'(', lc+1, rc, n)
                self.generate(s+')', lc, rc+1, n)
                
                
            
    
    def generateParenthesis(self, n: int) -> List[str]:

        self.res[:] = []

        lc = 0
        rc = 0
        s = ''
        self.generate(s, lc, rc, n)
        return self.res
