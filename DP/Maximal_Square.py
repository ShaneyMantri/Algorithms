"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:
            return 0
        
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        for i in range(len(dp)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    dp[i][j]= 1  

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j]=="1":
                    if matrix[i-1][j]=="1" and matrix[i][j-1]=="1" and matrix[i-1][j-1]=="1":
                        dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    else:
                        dp[i][j]=1
                        
        return max(max(x) for x in dp)**2
