"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""

## DFS 

class Solution:
    count = 0
    def dfs(self, g,m,n,i,j):
        for x,y in [(1,0),(-1,0),(0,-1),(0,1)]:
            if 0<=(i+x)<m and 0<=(j+y)<n and g[i+x][j+y]==0:
                g[i+x][j+y]=1
                self.dfs(g,m,n,i+x,j+y)
        
        
                
    def closedIsland(self, grid: List[List[int]]) -> int:
        v = [[0]*len(grid[0]) for _ in range(len(grid))]
        self.count=0
        n = len(grid[0])
        m = len(grid)

        for i in range(n):
            if grid[0][i]==0:
                grid[0][i]=1
                self.dfs(grid,m,n,0,i)
                
        for i in range(n):
            if grid[m-1][i]==0:
                grid[m-1][i]=1
                self.dfs(grid,m,n,m-1,i)
                
        for i in range(m):
            if grid[i][0]==0:
                grid[i][0]=1
                self.dfs(grid,m,n,i,0)
                
        for i in range(m):
            if grid[i][n-1]==0:
                grid[i][n-1]=1
                self.dfs(grid,m,n,i,n-1)
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==0:
                    self.dfs(grid,m,n,i,j)
                    self.count+=1
                    
        return self.count
