"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = {0:1}
        s = 0
        count = 0
        rem = 0
        for i in range(len(A)):
            s+=A[i]
            rem = s%K
            if rem in d:
                count+=d[rem]
            d[rem] = d.setdefault(rem, 0)+1
        return count
                
                
        
