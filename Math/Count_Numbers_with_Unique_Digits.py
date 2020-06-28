"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99

"""
class Solution:
    def count(self, n):
        i = 1
        c = 9
        prod = 9
        n-=1
        while n>0 and prod>0:
            c*=prod
            prod-=1
            n-=1
        return c
    
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        lim = (10**n)-1
        if n==0:
            return 1
        s = 10
        n = len(str(lim))
        i = 2
        while i<=n:
            s+=self.count(i)
            i+=1
        return s
        
        
        
"""
ALSO SEE DP AND BACKTRACK SOLUTIONS
"""
