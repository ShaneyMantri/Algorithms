"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
"""
### ALSO AVAILABLE IN BFS DFS FOLDER

class Solution:
    def dfs(self, c, st, k, i):
        if c<0:
            return
        if c==0:
            self.res.append(st)
            return
        if i+k<10 and c>0:
            self.dfs(c-1, st+str(i+k), k, i+k)
            
        if i-k>=0 and c>0:
            self.dfs(c-1, st+str(i-k), k, i-k)
            
        
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.res = []

        if N>1:
            
            for i in range(1, 10):
                self.dfs(N-1, str(i),K,i)
        else:
            for i in range(10):
                self.dfs(N-1, str(i),K,i)
                

        return list(set(self.res))
