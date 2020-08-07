"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])
        
        if n==0:
            return []
        res = []
        up = True
        count=0
        total = m*n
        while count<total:
            if not up:
                while i<m and j>=0:
                    res.append(matrix[i][j])
                    count+=1
                    i+=1
                    j-=1
                up = True
                if i>=m:
                    if j<0:
                        j=1
                        i=m-1
                    else:
                        i=m-1
                        j+=2
                else:
                    j=0
            else:
                while i>=0 and j<n:
                    res.append(matrix[i][j])
                    i-=1
                    j+=1
                    count+=1
                up = False
                if j>=n:
                    if i<0:
                        i=1
                        j=n-1
                    else:
                        j=n-1
                        i+=2
                else:
                    i=0
                    
            if count==total:
                break
        return res
