"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

## TLE BFS 91/92

from collections import deque
class Solution:
    def makeGraph(self, nums, n):
        d = {}
        for i in range(n-1):
            j = i+1
            k = nums[i]
            d[i]=[]
            while j<n and k>0:
                d[i].append(j)
                j+=1
                k-=1
                
            j = i-1
            k = nums[i]
            while j>=0 and k>0:
                d[i].append(j)
                j+=1
                k=-1
        return d
    
    
    def jump(self, nums: List[int]) -> int:
        g = self.makeGraph(nums, len(nums))
        d = deque([(0,0)])
        n = len(nums)
        v = [0]*n
        while d:
            ind, val = d.popleft()
            if ind==(n-1):
                return val
            for i in g[ind]:
                if v[i]==0:
                    v[i]=1
                    d.append((i, val+1))
        
                
