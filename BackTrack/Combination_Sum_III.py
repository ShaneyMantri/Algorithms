"""


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]



"""

class Solution:
    res = []
    def dfs(self, temp, s, k,n, ind):
        if len(temp)>k:
            return
        # print(temp,s)
        
        if s>n:
            return
        
        if s==n and len(temp)==k:
            if sorted(temp) not in self.res:
                self.res.append(temp)
                
        for i in range(ind+1,10):
            self.dfs(temp+[i], s+i, k,n, i)
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n<=0 or k<=0:
            return 0 
        self.res= []
        self.dfs([], 0,k,n,0)
        
        return self.res
