"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. 
The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        
        
        row = [0]*m
        col = [0]*n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in row:
            if i > 1:
                res += i
        for j in col:
            if j > 1:
                res += j
                
                
        
        for i in range(m):
            for j in range(n):
                if row[i] > 1 and col[j] > 1:
                    if grid[i][j] == 1:
                        res -= 1
        return res
