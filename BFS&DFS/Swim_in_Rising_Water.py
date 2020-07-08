"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
"""

class Solution:
    flag = False
    def dfs(self, grid, v,i,j,m,n, t):
    
        if self.flag==True:
            return
        
        if i==(m-1) and j==(n-1):
            self.flag=True
            return
        
        if i<0 or i>=m:
            return
        
        if j<0 and j>=n:
            return
        
        if 0<i<=(m-1):
            if grid[i-1][j]<=t:
                if v[i-1][j]==0:
                    v[i-1][j]=1
                    self.dfs(grid,v,i-1,j,m,n,t)
                    
        if 0<=i<(m-1):
            if grid[i+1][j]<=t:
                if v[i+1][j]==0:
                    v[i+1][j]=1
                    self.dfs(grid,v,i+1,j,m,n,t)
        
        if 0<=j<(n-1):
            if grid[i][j+1]<=t:
                if v[i][j+1]==0:
                    v[i][j+1]=1
                    self.dfs(grid,v,i,j+1,m,n,t)
                    
        if 0<j<=(n-1):
            if grid[i][j-1]<=t:
                if v[i][j-1]==0:
                    v[i][j-1]=1
                    self.dfs(grid,v,i,j-1,m,n,t)
        
        
        
    def swimInWater(self, grid: List[List[int]]) -> int:
    
        m = len(grid)
        n = len(grid[0])
        low = 0
        high = max(max(grid[v]) for v in range(m))+1
        res = []
        while low<high:
            mid = (low+high)//2
            self.flag=False
            if mid>=grid[0][0]: 
                v = [[0]*n for _ in range(m)]
                self.dfs(grid,v,0,0,m,n,mid)
            if self.flag==True:
                res.append(mid)
                high=mid
            else:
                low=mid+1
        return min(res)
            
