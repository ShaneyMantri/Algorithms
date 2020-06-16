"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5

Example 2:

Input: [[1,2],[3,4]]
Output: 17

Example 3:

Input: [[1,0],[0,2]]
Output: 8

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21
"""
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        z = [[] for _ in range(len(grid[0]))]
        y = []
        x = 0
        for i in range(len(grid)):
            m=0
            for j in range(len(grid)):
                if grid[i][j]>0:
                    x+=1
                    z[j].append(grid[i][j])
                    if grid[i][j]>m:
                        m=grid[i][j]
                        
            y.append(m)
            
        z = [max(i) for i in z]
        return x+sum(y)+sum(z)
                    
                
        
