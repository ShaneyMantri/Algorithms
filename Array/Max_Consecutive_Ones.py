"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i= 0
        if len(nums)==0:
            return 0
        n = len(nums)
        m = 0
        l=0
        while i<n:    
            if nums[i]==1:
                l+=1
            else:
                m = max(m, l)
                l = 0
            i+=1
        return max(m,l)
        
