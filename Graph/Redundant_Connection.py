"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
    
"""

class Solution:
    def makeGraph(self, edge):
        d = {}
        for i,j in edge:
            if i in d:
                d[i].append(j)
            else:
                d[i] = [j]
                
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
                
        return d
    
    def dfs(self, g, v, i,path, cycle):
        if i in g:
            for j in g[i]:
                if v[j]==0:
                    v[j]=1
                    self.dfs(g,v,j,path+[i], cycle)
                else:
                    if path[-1]!=j:
                        cycle.append([i,j])
                        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = self.makeGraph(edges)
        cycle = []
        # print(g)
        n = len(g.keys())
        for i in g.keys():
            v = [0]*(n+1)
            v[i]=1
            self.dfs(g,v,i,[i], cycle)
            
        for i in cycle:
            i.sort()
        
        for i in range(len(edges)-1, -1, -1):
            if edges[i] in cycle:
                return edges[i]
            
        return cycle[0]
        
        
