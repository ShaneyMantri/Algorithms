"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""
class Solution:
    flag=True
    def makeGraph(self,arr):
        d = {}
        for i in arr:
            if i[1] not in d:
                d[i[1]]=[i[0]]
            else:
                d[i[1]].append(i[0])
        return d
    
    def dfs(self, g, path, i, v):
        if self.flag:
            if i in g:
                for j in g[i]:
                    
                    if j in path:
                        self.flag=False
                        return
                    
                    if v[j]==0 and self.flag:
                        v[j]=1
                        self.dfs(g,path+[j],j,v)
            
            
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        
        n = numCourses
        g = self.makeGraph(prerequisites)
        v = [0]*n
        
        for i in range(n):
            if v[i]==0:
                v[i]=1
                self.dfs(g,[i],i,v)
                
        return self.flag
