"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n<0:
            x = 1/x
            n = -1*n
        t = x
        res=1
        step = 0
        while n>0:
            print(x, n,res)
            if n==1:
                return x*res
            
            if n%2==0:
                x*=x
                n=n//2
            else:
                res*=x
                n-=1
            step+=1
