""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
""

## TOPOLOGICAL SORT WITH CYCLE DETECTION
from collections import deque
class Solution:
    
    ans = []
    flag=False
    
    def makeGraph(self, arr):
        d = {}
        for i in arr:
            if i[1] not in d:
                d[i[1]] = [i[0]]
            else:
                d[i[1]].append(i[0])
        return d
    
    
    def dfs(self, g,v, i, n, path):
        if not self.flag:
            if i in g:
                for j in g[i]:
                    if j in path:
                        self.flag=True
                        return
                    if v[j]==0 and not self.flag:
                        v[j]=1
                        self.dfs(g,v,j, n, path+[j])

            self.ans.append(i)
        
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = self.makeGraph(prerequisites)    
        n = numCourses
        v = [0]*numCourses
        
        if len(prerequisites)==0:
            return [i for i in range(n)]
            
        self.ans = []
        
        for i in range(n):
            if v[i]==0:
                v[i]=1
                self.dfs(g,v, i,n, [i])
            
        return self.ans[::-1] if not self.flag else []
            
            
            
                
            
            
            
