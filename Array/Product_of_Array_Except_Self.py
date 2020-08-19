"""
Given an array nums of n integers where n > 1,  return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [0]
        if len(nums)==0:
            return []
        if max(nums)==0:
            return [0]*len(nums)
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = left[i]*right[i]
        return res
        
        
        
