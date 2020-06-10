"""
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

"""
from collections import Counter
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        a = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in a:
                a[groupSizes[i]].append(i)
            else:
                a[groupSizes[i]] = [i]
        b = groupSizes.copy()
        l = 0
        for k,v in a.items():
            l+=len(v)//k
        res = []
        for k,v in a.items():
            i = 0
            while i<len(v):
                res.append(v[i:i+k])
                i+=k
        return res