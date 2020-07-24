"""
A chess knight can move as indicated in the chess diagram below:
This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.
How many distinct numbers can you dial in this manner?
Since the answer may be large, output the answer modulo 10^9 + 7.
Example 1:

Input: 1
Output: 10

Example 2:

Input: 2
Output: 20

Example 3:

Input: 3
Output: 46
"""

class Solution:
    def dfs(self, g, memo, n, i):
        if n==0:
            return 1
        
        if (i,n) in memo:
            return memo[(i,n)]
        ret = 0
        for j in g[i]:
            ret+= self.dfs(g,memo,n-1,j)
            
        memo[(i,n)]=ret
        return ret
            
    def knightDialer(self, N: int) -> int:
        ret = 0
        g = {
            0:[4,6],
            1:[6,8],gith
            2:[7,9],
            3:[4,8],
            4:[0,9,3],
            5:[],
            6:[0,7,1],
            7:[2,6],
            8:[1,3],
            9:[4,2]
        }
        memo = {}
        for i in range(10):
            ret+=self.dfs(g,memo, N-1,i)
            
        return ret%((10**9)+7)
