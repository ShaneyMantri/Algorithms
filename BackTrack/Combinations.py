"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
class Solution:
    res = [ ]
    def dfs(self, arr,i, n, k, temp):
        if k<0:
            return
        if (k)>(n-i):
            return
        if k==0:
            self.res.append(temp)
            return
                
        if i<n:        
            self.dfs(arr, i+1, n, k-1, temp+[arr[i]])
            self.dfs(arr, i+1, n, k, temp)
        
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        l = [i for i in range(1, (n+1))]
        self.dfs(l, 0, n, k, [])
        return self.res
