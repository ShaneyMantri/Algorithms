"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

"""

from collections import deque
import sys
class Solution:
    def bfs(self, d,mat,m,n,dirs):
        while d:
            i,j,step,px,py = d.popleft()
            for x,y in dirs:
                if px==(i+x) and py==(j+y):
                    continue
                if 0<=(i+x)<m and 0<=(j+y)<n:
                    if mat[i+x][j+y]==0:
                        return step+1
                    d.append((i+x,j+y,step+1, i,j))
        
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if (len(matrix))==0:
            return []
        if (len(matrix[0]))==0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    continue
                d = deque([(i,j,0,i,j)])
                matrix[i][j]=self.bfs(d,matrix,m,n,dirs)
        return matrix
                
        
        
