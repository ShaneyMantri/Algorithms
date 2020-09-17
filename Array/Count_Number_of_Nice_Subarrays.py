"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

## 22/35 WA

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [0]*len(nums)
        n = len(nums)
        d = {}
        if nums[0]%2 == 1:
            odds[0] = 1
        else:
            odds[0] = 0
            
        odds = [0] + odds
        d[0] = d.setdefault(0, []) + [0]
        d[odds[0]] = d.setdefault(0, []) + [1]
        
        for i in range(1, n):
            if nums[i]%2 == 1:
                odds[i] = odds[i-1] + 1
            else:
                odds[i] = odds[i-1]
            
            d[odds[i]] = d.setdefault(odds[i], []) + [i+1] 
            
            
            
                
        count = 0
        key = list(d.keys())
        for i in key:
            if i - k in key:
                count += len(d[i])*len(d[i-k])
                
        
        return (count)
        
## AC single pass
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [0]*len(nums)
        n = len(nums)
        d = {}
        if nums[0]%2 == 1:
            odds[0] = 1
        else:
            odds[0] = 0
            
        # d[odds[0]] = d.setdefault(0, []) + [1]
        odds = [0] + odds
        d[0] = d.setdefault(0, []) + [0]
        
        count = 0
        for i in range(1, n+1):
            if nums[i-1]%2 == 1:
                odds[i] = odds[i-1] + 1
            else:
                odds[i] = odds[i-1]
            
            if odds[i] - k in d:
                count += len(d[odds[i] - k])
            d[odds[i]] = d.setdefault(odds[i], []) + [i] 
        
        return (count)
                        
        


