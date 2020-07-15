"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

## TLE DP 91/92

import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize]*n
        dp[0]=0
        for i in range(n):
            jump = nums[i]
            j = i+1
            while jump>0 and j<n:
                dp[j] = min(dp[j], dp[i]+1)
                jump-=1
                j+=1
        return dp[-1]
