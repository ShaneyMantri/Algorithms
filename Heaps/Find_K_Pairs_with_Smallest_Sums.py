"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

import heapq 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        n1 = len(nums1)
        n2 = len(nums2)
        currmax = 0
        
        for i in range(n1):
            for j in range(n2):
                if len(heap)<k:
                    heapq.heappush(heap, ((nums1[i]+nums2[j])*-1, [nums1[i],nums2[j]]))
                else:
                    if nums1[i]+nums2[j]<heap[0][0]*-1:
                        heapq.heappop(heap)
                        heapq.heappush(heap, ((nums1[i]+nums2[j])*-1, [nums1[i],nums2[j]]))
                        
        res = []        
        
        for i in heap:
            res.append(i[1])
            
        return res
