"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        i = 1
        res = [[1]]
        while i<numRows:
            temp = [0]*(len(res[-1])+1)
            temp[0]=1
            temp[-1]=1
            for j in range(1,len(res[-1])):
                temp[j]=res[-1][j-1]+res[-1][j]
            res.append(temp)
            i+=1
        return res
                
        
