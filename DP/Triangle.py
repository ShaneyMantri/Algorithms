"""
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[10**13]*len(i) for i in triangle]
        dp[0][0]=triangle[0][0]
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                if j-1>=0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j])
                if j < len(dp[i-1]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j])
                dp[i][j]+=triangle[i][j]
        return min(dp[-1])
                
                
                    
