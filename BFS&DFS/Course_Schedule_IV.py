"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

 

Example 1:

Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.

Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.

Example 3:

Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]

Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]
"""

from collections import deque
class Solution:
    def buildGraph(self, prerequisites):
        d = {}
        for i in prerequisites:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]]= [i[1]]
                
        return d
    
    def bfs(self, d, src, dst, n):
        q = deque([src])
        visited = [0]*n
        visited[src]=1
        while q:
            # print(q, visited)
            t = q.popleft()
            if t==dst:
                return True
            if t in d:
                for i in d[t]:
                    if visited[i]==0:
                        q.append(i)
                        visited[i]=1
                    
        return False   
    
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        d = self.buildGraph(prerequisites)
        res = []
        for i in queries:
            src = i[0]
            dst = i[1]
            # print(src, dst)
            # print(d)
            res.append(self.bfs(d, src, dst, n))
        return res
