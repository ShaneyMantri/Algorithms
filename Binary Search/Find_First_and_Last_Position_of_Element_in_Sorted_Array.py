"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
# Method 1 slower
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n==0:
            return [-1,-1]
            
        low = 0
        high = n-1
        t = target
        
        while low<high:
            mid = (low+high)//2
            if nums[mid]<t:
                low = mid+1
            else:
                high=mid
                
        first = low
        low = 0
        high = n-1
        
        while (low)<high:
            mid = (low+high)//2
            if nums[mid]<=t:
                low = mid+1
            else:
                high = mid
                
        last = high
        
        if nums[first]==t:
            if nums[last]==t:
                return [first,last]
            else:
                return [first, last-1]
        else:
            return [-1,-1]
        
# Method 2 faster
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
            
        res = [0, 0]
        low = 0
        high = len(nums)
        possibleLeft = -1
        possibleRight = -1
        while low < high:
            mid = (low+high)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    possibleLeft = mid
                high = mid
            else:
                low = mid + 1
        
        res[0] = possibleLeft
            
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    possibleRight = mid
                low = mid + 1
            else:
                high = mid
                
        res[1] = possibleRight
        return res
