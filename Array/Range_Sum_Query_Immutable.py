"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

"""

class NumArray:
    arr = []
    def __init__(self, nums: List[int]):
        self.arr = [0]*len(nums)
        if len(nums)==0:
            return
        self.arr[0] = nums[0]
        for i in range(1, len(self.arr)):
            self.arr[i] = self.arr[i-1] + nums[i]
        self.arr = [0] + self.arr

    def sumRange(self, i: int, j: int) -> int:
        return self.arr[j+1] - self.arr[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
