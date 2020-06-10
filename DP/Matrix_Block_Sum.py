"""
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


"""

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        row = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                first = max(0, j-K)
                last = min(n-1, j+K)
                row[i][j] = sum(mat[i][first:last+1])
        ans = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                first = max(0, i-K)
                last = min(m-1, i+K)
                t = first
                while t<=last:
                    s+=row[t][j]
                    t+=1
                ans[i][j]=s
        return (ans)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
