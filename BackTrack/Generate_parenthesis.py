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
    res = 0
    def dfs(self, lp, rp, s, fin):
        if rp == lp:
            if lp < fin:
                self.dfs(lp+1, rp, s+"(", fin)
            else:
                self.res.append(s)
                return
        if rp < lp:
            if lp < fin:
                self.dfs( lp+1, rp, s+"(", fin)
            self.dfs( lp, rp+1, s+")", fin)
                
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(0,0,'', n)
        return self.res
