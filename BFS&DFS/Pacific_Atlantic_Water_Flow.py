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
                
        
## Method 2
## 340ms

from collections import deque
class Solution:
    def bfs(self, mat, start,end, dirs, v):
        m = len(mat)
        n = len(mat[0])
        d = deque([(start, end)])
        while d:
            i, j = d.popleft()
            for x,y in dirs:
                if 0<=(i+x)<m and 0<=(y+j)<n and mat[i][j]<=mat[i+x][j+y] and v[i+x][j+y]==0:
                    d.append((i+x, y+j))
                    v[i+x][j+y] = 1
            
            
        
            
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])
        if n==0:
            return []
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        po = [[0]*n for _ in range(m)]
        ao = [[0]*n for _ in range(m)]
        for j in range(n):
            po[0][j]=1
            ao[m-1][j]=1
            
        for i in range(m):
            po[i][0]=1
            ao[i][n-1]=1
        
        stat_p = po.copy()
        stat_a = ao.copy()
        for i in range(m):
            for j in range(n):
                if po[i][j]==1:
                    self.bfs(matrix, i,j,dirs, stat_p)
                if ao[i][j]==1:
                    self.bfs(matrix,i,j,dirs,stat_a)
                    
        res = []        
        for i in range(m):
            for j in range(n):
                if stat_p[i][j]==1 and stat_a[i][j]==1:
                    res.append([i,j])
                    
        return res
        
        
