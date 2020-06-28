"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99


"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        lim = (10**n)-1
        if n==0:
            return 1
        s = 10
        
        d = [9]
        dp = [10-i for i in range(1, 10)]
        dp = d+dp
        
        for i in range(1,10):
            dp[i]*=dp[i-1]
            
            
        i = 2
        n = len(str(lim))
        while i<=n:
            s+=dp[i-1]
            i+=1
            
        return s
            
        
