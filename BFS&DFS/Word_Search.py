"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from collections import deque
class Solution:
    res = 0
    def dfs(self, stind, i,j,m,n,grid, st, word, dirs, path):
        if self.res==1:
            return
        if word==st:
            self.res=1
            return
        if stind==len(word):
            return
        
        for x,y in dirs:
            if ((i+x),(j+y)) not in path:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]==word[stind+1]:
                    self.dfs(stind+1,i+x,j+y,m,n,grid,st+grid[i+x][j+y], word, dirs, path+[(i+x,j+y)] )
                    
                    
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(0,1), (-1,0), (0,-1)]
        
        for i in range(m):
            for j in range(n):
                if word[0]==board[i][j]:
                    self.dfs(0, i,j,m,n,board,str(board[i][j]), word,dirs,[(i,j)])
                    if self.res:
                        return True
        return False                    
