"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
class Solution:
    def dfs(self, nums, temp):
        if len(nums)==0:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], temp+[nums[i]])
            
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        
        
        return self.res
