"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

class Solution:  
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a = {}
        b = {}
        same = {}
        if len(A)<=1:
            return 0
        for  i in range(len(A)):
            a[A[i]] = a.setdefault(A[i], 0)+1
            b[B[i]] = b.setdefault(B[i], 0)+1
            if A[i]==B[i]:
                same[A[i]] = same.setdefault(A[i], 0)+1
        m = 10**14
        cannota = []
        for i in range(1,7):
            if i in a:
                if i not in cannota:
                    if i in b:
                        if i in same:
                            if (a[i]+b[i]-same[i])>=len(A):
                                m = min(m, len(A)-a[i])
                            else:
                                cannota.append(i)
                        else:
                            if (a[i]+b[i])>=len(A):
                                m = min(m, len(A)-a[i])
                            else:
                                cannota.append(i)

                    else:
                        cannota.append(i)
                    
        cannotb = []
        for i in range(1,7):
            if i in b:
                if i not in cannotb:
                    if i in a:
                        if i in same:
                            if (a[i]+b[i]-same[i])>=len(B):
                                m = min(m, len(B)-b[i])
                            else:
                                cannotb.append(i)
                        else:
                            if (a[i]+b[i])>=len(B):
                                m = min(m, len(B)-b[i])
                            else:
                                cannotb.append(i)
                    else:
                        cannotb.append(i)
        return m if m<10**14 else -1
            
        
        
