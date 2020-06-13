"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

#SOLUTION 1
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        
#SOLUTION 2 - TLE (311/313)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        n = len(nums)
        res = []
        nums.sort()
        # print(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s,e = i+1, n-1
            while s<e:
                # print(nums[i],nums[s], nums[e], (nums[s]+nums[e]+nums[i])==0)
                # print("SUM", (nums[s]+nums[e]+nums[i]))
                if (nums[s]+nums[e]+nums[i])==0:
                    if [nums[i], nums[s], nums[e]] not in res:
                        res.append([nums[i], nums[s], nums[e]])
                    s+=1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                elif (nums[s]+nums[e]+nums[i]>0):
                    e-=1
                else:
                    s+=1
        return res
                            
