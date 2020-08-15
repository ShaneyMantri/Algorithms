"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0 or len(intervals)==1:
            return 0
        inc = sorted(intervals , key = lambda x:(x[1]-x[0]))
        m = 0
        
        stat = {}
        remove = 0
        for i in inc:
            for j in range(i[0], i[1]+1):
                if j in stat:
                    if stat[j]==True and j!=i[1]:
                        if (j+1) in stat and stat[j+1]==True:
                            remove+=1
                            break
                stat[j]=True
        return remove
                    
                        
        
