"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
"""

class Solution:
    res = []
    def dfs(self, path, v,g,i, dest):
        # print(path)
        if i==dest:
            self.res.append(path)
            return
            
        if i in g:
            for j in g[i]:
                if v[j]==0:
                    v[j]=1
                    self.dfs(path+[j], v,g,j, dest)
                    v[j]=0
        
        
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g = {}
        n = len(graph)
        for i in range(n):
            g[i]=[]
            for j in graph[i]:
                g[i]+=[j]
        
        self.res= []
        v = [0]*n
        self.dfs([0],v,g,0,n-1)
        return self.res
