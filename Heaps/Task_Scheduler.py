"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""

from heapq import heappop, heappush, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            if i in d:
                d[i]-=1
            else:
                d[i]=-1
        
        res = [[v,k] for k,v in d.items()]
        heapify(res)
        count=0
        st = ''
        while res:
            i = 0
            temp = []
            while i<=n and (len(res)>0):
                v,k = heappop(res)
                v+=1
                count+=1
                st+=k
                if v<0:
                    temp.append([v,k])
                i+=1
            if i==(n+1):
                for v,k in temp:
                    heappush(res, [v,k])
            elif i<=n:
                for j in range(n-i+1):
                    st+=' '
                    count+=1
                if temp:
                    for v,k in temp:
                        heappush(res,[v,k])
        return count-(n-i+1)
            
            
