"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
"""
## METHOD 1
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dp = [[0]*3 for i in range(n)]
        dp[0][nums[0]%3]=nums[0]
        for i in range(1,n):
            t1 = nums[i]%3
            dp[i][0] = max(dp[i-1][(3-t1)%3]+nums[i], dp[i-1][0]) if dp[i-1][(3-t1)%3]!=0 else dp[i-1][0]
            dp[i][1] = max(dp[i-1][(3-t1+1)%3]+nums[i],dp[i-1][1]) if dp[i-1][(3-t1+1)%3]!=0 else dp[i-1][1]
            dp[i][2] = max(dp[i-1][(3-t1+2)%3]+nums[i], dp[i-1][2]) if dp[i-1][(3-t1+2)%3]!=0 else dp[i-1][2]
            dp[i][t1] = max(nums[i], dp[i][t1])
        
        return dp[-1][0]
    
## METHOD 2
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dp = [0,0,0]
        for num in nums:
            for i in dp[:]:
                dp[(i+num)%3] = max(dp[(i+num)%3], i+num)
        return dp[0]
                
        
