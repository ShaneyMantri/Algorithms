"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

class Solution:
    def dfs(self, curr, i, arr, low, high):
        if low<=curr<=high and curr not in self.res:
            self.res.append(curr)
            
        if i>=8:
            return
        
        if curr>high:
            return
        
        self.dfs(curr*10+arr[i+1], i+1, arr, low, high)
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = [i for i in range(1,10)]
        self.res= []
        for i in range(len(arr)):
            self.dfs(arr[i], i, arr, low, high)
            
        return sorted(self.res)
        
        
        
