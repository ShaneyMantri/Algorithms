"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import deque
class Solution:
    def createGraph(self, wordList):
        d = {}
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                c = 0
                for k in range(len(wordList[i])):
                    if wordList[i][k]!=wordList[j][k]:
                        c+=1
                if c==1:
                    if wordList[i] not in d:
                        d[wordList[i]]=[wordList[j]]
                    else:
                        d[wordList[i]].append(wordList[j])
                    if wordList[j] not in d:
                        d[wordList[j]]=[wordList[i]]
                    else:
                        d[wordList[j]].append(wordList[i])
        return d
    
    
    
    def bfs(self, d, beginWord, endWord, wordList):
        qs = deque([(beginWord, 1)])
        qe = deque([(endWord, 1)])
        vs = {beginWord:1}
        ve = {endWord:1}
        while qs and qe:
            sw, sl = qs.popleft()
            ew,el = qe.popleft()
            if sw in d:
                for i in d[sw]:
                    if i==endWord:
                        return sl+1
                    if i in ve:
                        return ve[i]+sl
                    if i not in vs:                    
                        vs[i]=sl+1
                        qs.append((i, sl+1))
                        
            if ew in d:
                for i in d[ew]:
                    if i==beginWord:
                        return el+1
                    if i in vs:
                        return vs[i]+el
                    if i not in ve:
                        ve[i]=el+1
                        qe.append((i, el+1))
        return 0
        
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        d = self.createGraph(wordList)
        return self.bfs(d, beginWord, endWord,wordList)
        
