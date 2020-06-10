"""

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

"""


class Solution:
    res = []
    def dfs(self, target, candi, temp,n,k):
        if target<0:
            return
        if target==0:
            x = sorted(temp)
            if x not in self.res:
                self.res.append(x)
            
        for i in range(k,n):
            if target-candi[i]>=0:

                self.dfs(target-candi[i], candi, temp+[candi[i]], n, i)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        if len(candidates)==0:
            return []
        
        self.res = []
        self.temp = []
        n = len(candidates)
        candidates.sort(reverse=True)
        self.dfs(target, candidates, [],n, 0)
        return self.res
