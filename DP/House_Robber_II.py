"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n<=3:
            return max(nums)
            
        dp1 = [0]*(n-1)
        dp2 = [0]*(n-1)
        
        dp1[0]=nums[0]
        dp1[1]=nums[1]
        dp2[0]=nums[-1]
        dp2[1]=nums[-2]
                
        for i in range(2, n-1):
            t = max(dp1[:i-1])
            dp1[i]=max(dp1[i-1], t+nums[i])
            
        nums = nums[::-1]
        
        for i in range(2, n-1):
            t = max(dp2[:i-1])
            dp2[i]=max(dp2[i-1], t+nums[i])
            
        return max(dp1[-1], dp2[-1])
                    
        
