"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

class Solution:
    def dfs(self, dirs, mat, m,n,i,j,memo):
        if memo[i][j]>0:
            return memo[i][j]
        memo[i][j]=1
        for x,y in dirs:
            if 0<=(i+x)<m and 0<=(y+j)<n and mat[i][j]>mat[i+x][j+y]:
                t = self.dfs(dirs, mat, m,n,i+x,y+j, memo)
                memo[i][j] = max(memo[i][j], t+1)
        return memo[i][j]
        
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m==0:
            return 0
        
        n = len(matrix[0])
        if n==0:
            return 0
            
        memo = [[0]*n for i in range(m)]
        dirs = [(1,0),(-1,0),(0,1), (0,-1)]
        
        for i in range(m):
            for j in range(n):
                self.dfs(dirs, matrix, m,n,i,j,memo)
                
        return max(max(j) for j in memo)
        
        
