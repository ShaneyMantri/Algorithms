"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""

class Solution:
    res = []
    def dfs(self, temp, nums, i, n):
                
        if temp not in self.res:
            self.res.append(temp)
            
        if i>=n:
            return

        
        self.dfs(temp+[nums[i]], nums,i+1, n)
        self.dfs(temp, nums,i+1, n)
        
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.dfs([], nums, 0, len(nums))
        return self.res
        
