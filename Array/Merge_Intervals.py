"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval = sorted(intervals, key = lambda x:x[0])
        while True:
            flag=0
            for i in range(len(interval)-1):
                if interval[i][1]>=interval[i+1][0]:
                    flag=1
                    interval[i][1] = max(interval[i][1], interval[i+1][1])
                    interval.pop(i+1)
                    break
            if flag==0:
                return interval
        
