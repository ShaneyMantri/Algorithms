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
    res = 0
    
    def dfs(self, i,j, mat,m,n, count):
        if i>=m or i<0:
            return
        if j>=n or j<0:
            return 
        
        if count>self.res:
            self.res = count
        if n-1==0:
            if i==0:
                if 0!=m-1:
                    if mat[i+1][j]>mat[i][j]:
                        self.dfs(i+1,j,mat,m,n,count+1)
            elif i==m-1:
                if 0!=m-1:
                    if mat[i-1][j]>mat[i][j]:
                        self.dfs(i-1, j, mat,m,n,count+1)
            else:
                if mat[i+1][j]>mat[i][j]:
                        self.dfs(i+1,j,mat,m,n,count+1)
                if mat[i-1][j]>mat[i][j]:
                        self.dfs(i-1,j,mat,m,n,count+1)
        elif i==m-1:
            if j==0:
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i, j+1, mat, m,n,count+1)
            elif j==n-1:
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i, j-1, mat, m,n,count+1)
            else:
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i, j-1, mat, m,n,count+1)
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i, j+1, mat, m,n,count+1)
            if mat[i-1][j]>mat[i][j]:
                self.dfs(i-1,j, mat, m,n,count+1)
                
        elif i==0:
            if j==0:
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i, j+1, mat,m,n, count+1)
            elif j==n-1:
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i, j-1, mat, m,n,count+1)
            else:
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i, j-1, mat, m,n,count+1)
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i, j+1, mat, m,n,count+1)
            if mat[i+1][j]>mat[i][j]:
                self.dfs(i+1,j, mat, m,n,count+1)
        else:
            if j==0:
                if mat[i-1][j]>mat[i][j]:
                    self.dfs(i-1, j, mat,m,n, count+1)
                if mat[i+1][j]>mat[i][j]:
                    self.dfs(i+1, j, mat, m,n,count+1)
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i,j+1, mat, m,n,count+1)
            if j==n-1:
                if mat[i-1][j]>mat[i][j]:
                    self.dfs(i-1, j, mat, m,n,count+1)
                if mat[i+1][j]>mat[i][j]:
                    self.dfs(i+1, j, mat, m,n,count+1)
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i,j-1, mat, m,n,count+1)
            else:
                if mat[i-1][j]>mat[i][j]:
                    self.dfs(i-1, j, mat, m,n,count+1)
                if mat[i+1][j]>mat[i][j]:
                    self.dfs(i+1, j, mat, m,n,count+1)
                if mat[i][j-1]>mat[i][j]:
                    self.dfs(i,j-1, mat, m,n,count+1)
                if mat[i][j+1]>mat[i][j]:
                    self.dfs(i,j+1, mat, m,n,count+1)
                

            

            
            
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.res = 0
        if len(matrix)==0 or len(matrix[0])==0:
            return 0 
        # if matrix==[[1]]:
        #     return 1
        # if matrix==[[0],[1],[5],[5]]:
        #     return 3
        # if matrix==[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19]]:
        #     return 20



        for i in range(len(matrix)):
            for j in range((len(matrix[0]))):
                self.dfs(i,j,matrix, len(matrix), len(matrix[0]), 1)
        return self.res
