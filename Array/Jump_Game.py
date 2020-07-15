"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        bonus = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>=1:
                bonus-=1
                bonus = max(bonus, nums[i])
                
            elif nums[i-1]==0 and bonus>0:
                bonus-=1
                bonus = max(bonus, nums[i])
                
                
            else:
                return False
        return True
                
            
                
                
