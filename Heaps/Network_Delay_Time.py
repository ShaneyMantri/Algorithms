"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
"""

import sys
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        d = {}
        for i,j,k in times: 
            if i in d:
                d[i].append((j,k))
            else:
                d[i]=[(j,k)]
        time = [sys.maxsize]*(N+1)
        heap = [(0,K)]
        while heap:
            t,n = heapq.heappop(heap)
            if t<time[n]:
                time[n]=t
                if n in d:
                    for j,k in d[n]:
                        heapq.heappush(heap, (t+k, j))
            
                    
        if max(time[1:N+1])==sys.maxsize:
            return -1
        return max(time[1:N+1])
            
