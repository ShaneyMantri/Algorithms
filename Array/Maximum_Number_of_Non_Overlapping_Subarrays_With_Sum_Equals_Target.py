"""
Given an array nums and an integer target.

Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
Example 3:

Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3
Example 4:

Input: nums = [0,0,0], target = 0
Output: 3
"""
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = {0:-1}
        s = 0
        sub = 0
        for i in range(len(nums)):
            s+=nums[i]
            if s==target:
                sub+=1
                d.clear()
                d = {0:i}
                s=0
            elif s-target in d:
                sub+=1
                d.clear()
                d = {0:i}
                s = 0
            else:
                d[s] = i
        return sub
