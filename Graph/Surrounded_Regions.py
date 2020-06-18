"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        d = deque([])
        m = len(board)
        n = len(board[0])
        a = board
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1) and a[i][j]=="O":
                    d.append((i,j))
                elif (j==0 or j==n-1) and a[i][j]=="O":
                    d.append((i,j))

        while d:
            t = d.popleft()
            if (0<=t[0]<=(m-1)) and (0<=t[1]<=(n-1)):
                if a[t[0]][t[1]]=="O":
                    a[t[0]][t[1]]="N"
                    d.append((t[0], t[1]+1))
                    d.append((t[0], t[1]-1))
                    d.append((t[0]-1, t[1]))
                    d.append((t[0]+1, t[1]))
        
        for i in range(m):
            for j in range(n):
                if a[i][j]=="N":
                    a[i][j]="O"
                else:
                    a[i][j]="X"
