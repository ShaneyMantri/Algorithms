"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
"""
class Solution:
    res = []
    def dfs(self,i, temp, n, nums):
        if temp not in self.res and len(temp)>=2:
            self.res.append(temp)
        
        used = {}
        for j in range(i+1,n):
            if nums[j] not in used:
                used[nums[j]]=1
                if nums[j] >=temp[-1]:
                    self.dfs(j, temp+[nums[j]], n, nums)
                    
                    
                    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        if len(nums)==0:
            return self.res
        a = set()
        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
                self.dfs(i, [nums[i]], len(nums), nums)
        return self.res
