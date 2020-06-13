"""

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        n = len(nums)
        dp = [[nums[_]] for _ in range(n)]
        i = n-2
        while i>=0:
            j = i+1
            t = dp[i]
            ml = 1
            while j<n:
                if nums[j]%nums[i]==0:
                    if len([nums[i]]+dp[j])>ml:
                        ml = len([nums[i]]+dp[j])
                        t = ([nums[i]]+dp[j]).copy()
                j+=1
            dp[i] = t.copy()
            i-=1
        return (sorted(dp, key=len, reverse=True)[0])
            
                    
        
