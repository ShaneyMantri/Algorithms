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

from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        d = deque([(0,0)])
        n = len(nums)
        v = [0]*n
        v[0]=1
        while d:
            ind, val = d.popleft()
            if ind+nums[ind]>=(n-1):
                return val+1
            for i in range(min(n-1, ind+nums[ind]),max(0, ind-nums[ind]-1), -1):
                if v[i]==0:
                    v[i]=1
                    d.append((i, val+1))
        return 
        
                
