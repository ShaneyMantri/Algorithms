"""
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if len(grid)==0:
            return 0
        if len(grid[0])==0:
            return 0
        
        
        m = len(grid)
        n = len(grid[0])
        one = 0
        d = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    d.append((i,j, 0))
                elif grid[i][j]==1:
                    one+=1
        if len(d)==0:
            if one==0:
                return 0
            else:
                return -1
            
        days = 0
        while d and one>0:
            t = d.popleft()
            temp = one
            if 0<t[0] and t[0]<=(m-1):
                if grid[t[0]-1][t[1]]==1:
                    d.append((t[0]-1, t[1], t[2]+1))
                    grid[t[0]-1][t[1]]=2
                    one-=1
            
            if 0<=t[0] and t[0]<(m-1):
                if grid[t[0]+1][t[1]]==1:
                    d.append((t[0]+1,t[1], t[2]+1))
                    grid[t[0]+1][t[1]]=2
                    one-=1
                    
                    
            if 0<t[1] and t[1]<=(n-1):
                if grid[t[0]][t[1]-1]==1:
                    d.append((t[0],t[1]-1, t[2]+1))
                    one-=1
                    grid[t[0]][t[1]-1]=2
                    
            if 0<=t[1] and t[1]<(n-1):
                if grid[t[0]][t[1]+1]==1:
                    d.append((t[0],t[1]+1, t[2]+1))
                    one-=1
                    grid[t[0]][t[1]+1]=2
            days=t[2]+1
            
            
        if one==0:
            return days
        return -1
