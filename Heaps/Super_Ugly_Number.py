"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
"""

import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        d = {1:0}
        while n > 0:
            a = heapq.heappop(heap)
            for i in primes:
                if a*i in d:
                    continue
                heapq.heappush(heap, a*i)
                d[a*i] = 1
            n -= 1
        return a
