"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target==0:
            return 0
        dp = [0]*(target+1)
        
        dp[0]=1
        for i in range(1,target+1):
            for j in nums:
                if (i-j)>=0:
                    dp[i]+=dp[i-j]
        print(dp)
        return dp[-1]
        
