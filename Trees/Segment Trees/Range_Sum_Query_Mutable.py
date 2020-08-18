"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

class NumArray:

    tree = []
    n = 0
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0]*self.n+nums
        t = self.n-1
        while t>0:
            self.tree[t] = self.tree[t<<1]+self.tree[t<<1|1]
            t-=1
    
    def update(self, i: int, val: int) -> None:
        n = self.n+i
        self.tree[n] = val
        while n>1:
            self.tree[n>>1] = self.tree[n] + self.tree[n^1]
            n>>=1
            
    def sumRange(self, i: int, j: int) -> int:
        left = self.n + i
        right = self.n + j
        add = 0
        while left<=right:
            if left%2==1:
                add+=self.tree[left]
                left+=1
            left>>=1
            if right%2==0:
                add+=self.tree[right]
                right-=1
            right>>=1
        return add
                


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
