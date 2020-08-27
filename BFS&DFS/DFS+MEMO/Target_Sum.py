"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def dfs(self, i, s, nums, n, target, memo):
        if (i,target - s) in memo:
            return memo[(i, target-s)]
        
        
        if i==n and s==target:
            return 1
        elif i==n:
            return 0
        memo[(i, target - s)] = 0
        memo[(i, target - s)]+= self.dfs(i+1, s + nums[i], nums, n, target, memo)
        memo[(i, target - s)]+=self.dfs(i+1, s - nums[i], nums, n, target, memo)
        return memo[(i, target-s)]
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        self.dfs(0, 0, nums, len(nums), S, memo)
        return memo[(0, S)]
        
