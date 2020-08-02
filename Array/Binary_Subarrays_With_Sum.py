"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

    A.length <= 30000
    0 <= S <= A.length
    A[i] is either 0 or 1.
"""

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        subarray = 0
        dp = [0]*(n+1)
        d = {0:1}
        for i in range(n):
            dp[i+1]=dp[i]+A[i]
            if dp[i+1] in d:
                d[dp[i+1]]+=1
            else:
                d[dp[i+1]]=1
        ans = 0
        for k in d.keys():
            if (k-S) in d:
                if (k-S)!=k:
                    ans+=(d[k]*d[k-S])
                else:
                    ans+=((d[k]*(d[k]-1))//2)
        return ans
