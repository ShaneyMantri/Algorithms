"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating)<3:
            return 0
        ind = {}
        for i in range(len(rating)):
            ind[rating[i]]= i
        i=0
        inc=[]
        dec=[]
        n=len(rating)
        count=0
        while i<n-1:
            j=i+1
            while j<n:
                if rating[i]<rating[j]:
                    inc.append([rating[i], rating[j]])
                else:
                    dec.append([rating[i], rating[j]])
                j+=1
            i+=1
        for x in inc:
            last = ind[x[1]]
            if last<n-1:
                last+=1
                while last<n:
                    if rating[last]>x[1]:
                        count+=1
                    last+=1
        for y in dec:
            last=ind[y[1]]
            if last<n-1:
                last+=1
                while last<n:
                    if rating[last]<y[1]:
                        count+=1
                    last+=1
        return count                
        
        
