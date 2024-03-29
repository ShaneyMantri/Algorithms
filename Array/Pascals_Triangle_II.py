"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow(self, k: int) -> List[int]:
        ind = k-1
        rind = k+1
        if k==0:
            return [1]
        if k==1:
            return [1,1]
        
        st = [1,1]
        i = 3
        while i<=rind:
            temp = [1]
            for j in range(1,len(st)):
                temp.append(st[j-1]+st[j])
            temp+=[1]
            st = temp.copy()
            i+=1
            
        return st
                
                
            
            
        
