"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""

class Solution:
    res =0
    v = []
    def dfs(self, i, arr, n):
        if len(set(self.v))==1:
            return
        if self.res==1:
            return
        if i<0 or i>n:
            return
        if arr[i]==0:
            self.res = 1
        self.v[i]=True
        if i+arr[i]<n and not self.v[i+arr[i]]:
            self.dfs(i+arr[i], arr,n)
        if i-arr[i]>=0 and not self.v[i-arr[i]]:
            self.dfs(i-arr[i], arr, n)
        
            
    def canReach(self, arr: List[int], start: int) -> bool:
        self.res=0
        self.v = [False]*len(arr)
        if min(arr)>0:
            return False
        if len(arr)==1:
            return True if arr[0]==0 else False
        self.v[start]=True
        self.dfs(start, arr, len(arr))
        return True if self.res==1 else False
        
