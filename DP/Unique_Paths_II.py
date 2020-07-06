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

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid)==0:
            return 0
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
         
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else:
                break
        
        for i in range(n):
            if obstacleGrid[0][i]==0:
                dp[0][i]=1
            else:
                break
                
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    if obstacleGrid[i-1][j]==0:
                        dp[i][j]+=dp[i-1][j]
                    if obstacleGrid[i][j-1]==0:
                        dp[i][j]+=dp[i][j-1]
                        
        return dp[-1][-1]
                    
