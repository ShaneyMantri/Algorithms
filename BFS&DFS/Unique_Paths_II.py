"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""

## DFS TLE 27/41
## CHECK DP

class Solution:
    res = []
    def dfs(self, i, j, v, o, m, n, p):
        if i>=m:
            return
        if j>=n:
            return
        if i==(m-1) and j==(n-1):
            if p not in self.res:
                self.res.append(p)
            return
        
        if j==(n-1):
            if v[i+1][j]==0:
                if o[i+1][j]!=1:
                    v[i+1][j]=1
                    self.dfs(i+1, j, v,o,m,n,p+'d')
                    v[i+1][j]=0
                    
        elif i==(m-1):
            if v[i][j+1]==0:
                if o[i][j+1]!=1:
                    v[i][j+1]=1
                    self.dfs(i,j+1,v,o,m,n,p+'r')
                    v[i][j+1]=0
        else:
            if v[i+1][j]==0:
                if o[i+1][j]!=1:
                    v[i+1][j]=1
                    self.dfs(i+1, j, v,o,m,n,p+'d')
                    v[i+1][j]=0
                    
            if v[i][j+1]==0:
                if o[i][j+1]!=1:
                    v[i][j+1]=1
                    self.dfs(i,j+1,v,o,m,n,p+'r')
                    v[i][j+1]=0

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.res = []
        if len(obstacleGrid)==0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        v = [[0]*n for _ in range(m)]
        self.dfs(0,0, v, obstacleGrid, m, n, '')
        
        return len(self.res)
