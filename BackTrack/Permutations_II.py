"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

class Solution:
    def dfs(self, nums, temp):
        if len(nums)==0 and temp not in self.res:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], temp+[nums[i]])
            
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        
        
        return self.res
