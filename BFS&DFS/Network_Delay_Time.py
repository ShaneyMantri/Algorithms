"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
"""

class Solution:
    res = []
    def dfs(self,i, g, v, cost):
        if i in g:
            for j,k in g[i]:
                if v[j]==0:
                    v[j]=1
                    self.res[j]=cost+k
                    self.dfs(j,g,v,cost+k)
                else:
                    if (cost+k)<self.res[j]:
                        self.res[j]=cost+k
                        self.dfs(j,g,v,cost+k)
                
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        d = {}
        for i,j,k in times: 
            if i in d:
                d[i].append((j,k))
            else:
                d[i]=[(j,k)]
        self.res = [0]*(N+1)
        v = [0]*(N+1)
        v[K]=1
        self.dfs(K,d,v,0)
        if min(v[1:N+1])==0:
            return -1
        return max(self.res)
            
