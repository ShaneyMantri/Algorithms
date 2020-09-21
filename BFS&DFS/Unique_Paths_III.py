"""
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""

class Solution:
    res = 0
    def dfs(self, grid, i, j, m, n, dirs, count):
        for x, y  in dirs:
            if 0 <= (i + x) < m and 0 <= (j + y) < n and (grid[i + x][j + y] == 0 or grid[i + x][j + y] == 2):
                if grid[i + x][j + y] == 2:
                    if count == 0:
                        self.res += 1
                    continue
                grid[i+x][j+y] = -2
                self.dfs(grid, i + x, j + y, m, n, dirs, count - 1)
                grid[i+x][j+y] = 0
            
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = count = 0
        x = y = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    x = i
                    y = j
        self.dfs(grid, x, y, len(grid), len(grid[0]), dirs, count)
        return self.res
