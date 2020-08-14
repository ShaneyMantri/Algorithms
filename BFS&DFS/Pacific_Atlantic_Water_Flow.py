"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

### 8136ms AC
from collections import deque
class Solution:
    def bfs(self, mat, start,end, dirs, v):
        d = deque([(start, end)])
        m = len(mat)
        n = len(mat[0])
        fx=fy=0
        while d:
            i,j = d.popleft()
            if i==0:
                fx=1
            if j==0:
                fx=1
            if j==n-1:
                fy=1
            if i==m-1:
                fy=1
                
            if fx==1 and fy==1:
                return fx,fy
            
            for x,y in dirs:
                if 0<=(i+x)<m and 0<=(j+y)<n and mat[i][j]>=mat[i+x][j+y] and v[i+x][j+y]==0:
                    d.append((i+x, j+y))
                    v[i+x][j+y]=1
                    
        return fx, fy
            
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])
        if n==0:
            return []
        status = [[0]*n for i in range(m)]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                v = [[0]*n for i in range(m)]
                v[i][j]=1
                x,y = self.bfs(matrix, i,j,dirs, v)
                status[i][j] = x+y
        res = []
        for i in range(m):
            for j in range(n):
                if status[i][j]==2:
                    res.append([i,j])
                    
        return res
                
        
        
