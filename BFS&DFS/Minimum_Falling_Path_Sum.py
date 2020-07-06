"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  
The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:

    [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
    [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
    [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]

The falling path with the smallest sum is [1,4,7], so the answer is 12.
"""

### TLE 36/46
## CHECK DP

import sys
class Solution:
    tot =0 
    def dfs(self, i, j, m, n, a, c):
        if i==(m-1):
            self.tot=min(self.tot, c)
            return
               
        self.dfs(i+1, j, m,n,a,c+a[i+1][j])
        if j>0 and j<=(n-1):
            self.dfs(i+1,j-1,m,n,a,c+a[i+1][j-1])
        if j>=0 and j<(n-1):
            self.dfs(i+1,j+1,m,n,a,c+a[i+1][j+1])
            
        
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        self.tot=sys.maxsize
        for i in range(n):
            print("I",i)
            self.dfs(0,i,m,n,A,A[0][i])
            
        return self.tot
        
        
