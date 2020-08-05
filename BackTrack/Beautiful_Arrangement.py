"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

    The number at the ith position is divisible by i.
    i is divisible by the number at the ith position.

 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
"""

class Solution:
    count = 0
    def dfs(self, temp, n, nums, i):
        if len(temp)==n:
            self.count+=1
            return
        
        for j in range(len(nums)):
            if (i+1)%nums[j]==0 or nums[j]%(i+1)==0:
                self.dfs(temp+[nums[j]], n,nums[0:j]+nums[j+1:n], i+1)
            
    
    
    def countArrangement(self, N: int) -> int:
        self.count=0
        n = N
        nums = [i+1 for i in range(N)]
        for j in range(len(nums)):
            if (1)%nums[j]==0 or nums[j]%(1)==0:
                self.dfs([nums[j]], n,nums[0:j]+nums[j+1:n], 1)
        return self.count
