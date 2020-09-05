"""
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

# METHOD 1 slower

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        if S[0]==S[len(S)-1]:
            return [len(S)]
        
        while len(S)>0:
            n = len(S)
            start = 0
            rev = S[::-1]
            sl = list(S)
            revl = list(rev)
            ind = revl.index(sl[0])
            setc = list(set(sl[0:(n-ind-1)]))
            setc.sort()
            maxend = n-ind-1

            k = 0
            checked = []
            while k < len(setc):
                if setc[k] not in checked:
                    checked.append(setc[k])
                                            
                    ind1 = revl.index(setc[k])
                    ind1 = n-ind1-1
                    if ind1==(n-1):
                        maxend = ind1
                        res.append(n)
                        return res
                    elif ind1>maxend:
                        maxend = ind1
                        setc = list(set(sl[0:maxend+1]))
                        setc.sort()
                        k=0
                        
                        
                else:
                    k+=1
            res.append(maxend-start+1)
            S = S[maxend+1:]
            
            
        return res
                    
                    
# METHOD 2 faster

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        res = []
        for i in range(len(s)):
            if  s[i] not in d:
                d[s[i]] = [i, i]
            else:
                d[s[i]] = [d[s[i]][0], i]
        
        vals = list(d.values())
        i = 0
        while i<len(vals)-1:
            if vals[i][1]>vals[i+1][0]:
                vals[i][1] = max(vals[i+1][1], vals[i][1])
                vals[i][0] = min(vals[i+1][0], vals[i][0])
                vals.pop(i+1)
                continue
            i+=1
            
        for val in vals:
            res.append(val[1] - val[0] + 1)
        return res
                
