"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def dfs(self, v, grid, m, n, i, j, dirs):
        for x, y in dirs:
            if 0<=(i+x)<m and 0<=(y+j)<n and v[i+x][j+y] == 0 and grid[i+x][j+y] == "1":
                v[i+x][j+y] = 1
                self.dfs(v, grid, m, n, i+x, j+y, dirs)
                
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if v[i][j] == 0 and grid[i][j] == "1":
                    count += 1
                    v[i][j] = 1
                    self.dfs(v, grid, m, n, i, j, dirs)
        return count
