"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
"""

import heapq
class Solution:
    def find(self, heap, n):
        while n>0:
            t = heapq.heappop(heap)
            n-=1
            if n==0:
                return t
            while len(heap)>0 and heap[0]==t:
                heapq.heappop(heap)
                
            heapq.heappush(heap, t*2)
            heapq.heappush(heap, t*3)
            heapq.heappush(heap, t*5)
                
            
            
            
        
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        return self.find(heap, n)
        
        
        
