"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

"""

# DFS SOLUTION
class Solution:
    flag=0
    def dfs(self, stat, v, i, d):
        if self.flag==1:
            return

        for j in d[i]:
            if self.flag==0:
                if v[j]==0:
                    stat[j] = not stat[i]
                    v[j]=1
                    self.dfs(stat, v, j, d)                        
                else:
                    if stat[i]==stat[j]:
                        self.flag=1
                
        
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        for i in range(len(graph)):
            d[i]=graph[i].copy()
            
        stat = [-1]*len(graph)
        self.flag=0
        v= [0]*len(graph)
        for i in d.keys():
            if v[i]==0:
                stat[i]=0
                v[i]=1
                self.dfs(stat, v, i, d)
        return True if self.flag==0 else False
