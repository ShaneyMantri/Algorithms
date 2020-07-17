"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        heap = []
        for i in d:
            heapq.heappush(heap, (d[i], i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        
