"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

"""


#SOLUTION 1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins)==0 and amount==0:
            return 1
        if len(coins)==0:
            return 0
        if amount==0:
            return 1
        dp = [0]*(amount+1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j>=i:
                    dp[j]+=dp[j-i]
                    
        return dp[-1]
                    
                    
#SOLUTION 2 - TLE (17/27)
class Solution:
    res = 0
    def dfs(self, i, amt,n, coins):
        # print(amt)
        if amt<0:
            return
        if amt==0:
            self.res+=1
        for j in range(i, n):
            if amt-coins[j]>=0:
                self.dfs(j, amt-coins[j], n, coins)
                
                
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins)==0 and amount==0:
            return 1
        if len(coins)==0:
            return 0
        if amount==0:
            return 1
        self.res = 0
        coins.sort(reverse=True)
        self.dfs(0,amount, len(coins), coins)
        return self.res
        
