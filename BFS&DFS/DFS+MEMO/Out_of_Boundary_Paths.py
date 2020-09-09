"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
"""

class Solution:
    ans = 0
    def dfs(self, i,j,m,n,moves, dirs, memo, target):
        if (i == -1 or i == m) and moves <= target:
            return 1
        
        if (j == -1 or j == n) and moves <= target:
            return 1
        
        if moves == target:
            return 0
        
        if (i, j, moves) in memo:
            return memo[(i, j, moves)]
        
        
        memo[(i, j, moves)] = 0
        for x, y in dirs:
            memo[(i, j, moves)] += self.dfs(i+x, j+y, m, n, moves+1, dirs, memo, target)
            
        return memo[(i, j, moves)]
        
        
        
        
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        memo = {}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = self.dfs(i, j, m, n, 0, dirs, memo, N)
        return ans%((10**9)+7)
        
