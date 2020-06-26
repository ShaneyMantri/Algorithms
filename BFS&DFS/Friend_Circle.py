"""
 There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""

# BFS IMPLEMENTATION
from collections import deque
class Solution:
    def bfs(self, d):
        ret = 0
        v = [0]*len(d.keys())
        q = deque([])
        while min(v)!=1:
            ret+=1
            ind = v.index(0)
            q.append(ind)
            v[ind]=1
            while q:
                t = q.popleft()
                for item in d[t]:
                    if v[item]==0:
                        q.append(item)
                        v[item]=1
        return ret
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        d = {}
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]==1:
                    if i in d:
                        d[i].append(j)
                    else:
                        d[i]=[j]
        return self.bfs(d)
                
# DFS IMPLEMENTATION
class Solution:
    v= []
    ret = 0
    def dfs(self,i, d):
        for j in d[i]:
            if self.v[j]==0:
                self.v[j]=1
                self.dfs(j, d)
                                    
    def findCircleNum(self, M: List[List[int]]) -> int:
        d = {}
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]==1:
                    if i in d:
                        d[i].append(j)
                    else:
                        d[i]=[j]
        self.ret = 0
        self.v=[0]*len(d.keys())
        for i in range(len(self.v)):
            if self.v[i]==0:
                self.v[i]=1
                self.dfs(i, d)
                self.ret+=1
        return self.ret
                
