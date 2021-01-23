"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes 
for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""

class Solution:
    def makeGraph(self, times):
        d = {}
        for u,v,w in times:
            d[u] = d.setdefault(u, []) + [(v, w)]
        return d
    
    def dfs(self, g, i, d, v):
        if i in g:
            for j in g[i]:
                if v[j[0]] != 1:
                    d[j[0]] = d[i] + j[1]
                    v[j[0]] = 1
                    self.dfs(g, j[0], d, v)
                else:
                    if d[j[0]] > d[i] + j[1]:
                        d[j[0]] = d[i] + j[1]
                        v[j[0]] = 1
                        self.dfs(g, j[0], d, v)

                    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = self.makeGraph(times)
        v = [0]*(n+1)
        v[k] = 1
        d = {k:0}
        self.dfs(g, k, d, v)
        v = v[1:]
        return -1 if min(v) == 0 else max(d.values())
        
