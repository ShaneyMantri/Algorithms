"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
"""

class NumArray:

    tree = []
    n = 0
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0]*self.n + nums
        t = self.n - 1
        while t>0:
            self.tree[t] = self.tree[t<<1] + self.tree[t<<1|1]
            t-=1
        

    def sumRange(self, i: int, j: int) -> int:
        left = self.n + i
        right = self.n + j
        ret = 0
        while left<=right:
            if left%2==1:
                ret+=self.tree[left]
                left+=1
            left>>=1
            if right%2==0:
                ret+=self.tree[right]
                right-=1
            right>>=1
        return ret
                
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
