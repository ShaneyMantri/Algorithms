class Solution:
    def lcs(self, t1,t2, i, j):
        if i>=len(t1) or j>=len(t2):
            return 0
        if t1[i]==t2[j]:
            return 1+self.lcs(t1,t2,i+1, j+1)
        return max(self.lcs(t1,t2,i+1, j),
            self.lcs(t1,t2,i, j+1))
        
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)==0 or len(text2)==0:
            return 0
        res = self.lcs(text1, text2, 0,0)
        return res
        
