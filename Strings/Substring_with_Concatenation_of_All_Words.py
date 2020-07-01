"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        print(n)
        if n==0 or len(words)==0 or n<len(words[0]):
            return []

        nw = len(words[0])
        d ={}
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        i = 0
        res= [ ]
        while i<n:
            t = d.copy()
            if s[i:i+nw] in t and t[s[i:i+nw]]>0:
                t[s[i:i+nw]]-=1
                st = i
                st+=nw
                while st<=(n-nw):
                    if s[st:st+nw] not in t:
                        break
                    elif t[s[st:st+nw]]==0:
                            break
                    else:
                        t[s[st:st+nw]]-=1
                        st+=nw
                        
                if (sorted(t.items(), key= lambda x: x[1], reverse=True)[0][1])==0:
                    res.append(i)
            i+=1
        return res
                
                

                    
                    
                    
        
