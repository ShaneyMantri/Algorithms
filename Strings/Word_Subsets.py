"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
"""

from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for b in B:
            t = list(set(b))
            for i in t:
                if  i not in d:
                    d[i] = b.count(i)
                else:
                    if b.count(i)>d[i]:
                        d[i]=b.count(i)
        res = []
        for a in A:
            flag = 0
            da = Counter(a)
            left = 0
            for i in da:
                if i in d:
                    if d[i]>da[i]:
                        flag=1
                        break
                else:
                    left+=1
            if flag!=1 and left==(len(da)-len(d)):
                res.append(a)
        return res
                    
            
                
        
