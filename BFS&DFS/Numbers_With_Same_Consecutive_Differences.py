"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""

## ALSO AVAILABLE IN BACKTRACK FOLDER
from collections import deque
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N==1:
            return [i for i in range(10)]
        d = deque(['1','2','3','4','5','6','7','8','9'])
        res = []
        while d:
            n = d.popleft()
            if len(n)==N:
                if int(n) not in res:
                    res.append(int(n))
                continue
            if int(n[-1])+K<=9:
                d.append(n+str(K+int(n[-1])))
            if int(n[-1])-K>=0:
                d.append(n+str(int(n[-1])-K))
        res.sort()
        return res
                
