"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.


"""






class Solution:
    res= []
    def dfs(self, i, candi, target, temp,n):
        if target<0:
            return
        if target==0:
            x = sorted(temp)
            if x not in self.res:
                self.res.append(x)
        if i>=n:
            return

        self.dfs(i+1, candi, target-candi[i], temp+[candi[i]],n)
        self.dfs(i+1, candi, target, temp,n)
        
        
        
        
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return []
        
        self.res = []
        n = len(candidates)
        self.dfs(0, candidates, target, [],n)
        return self.res
        
