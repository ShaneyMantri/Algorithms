"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            d[i] = d.setdefault(i, 0)+1
        ds = sorted(d.items(), key=lambda x:(-x[1], x[0]))
        res = []
        i = 0
        while k>0 and i<len(ds):
            res.append(ds[i][0])
            i+=1
            k-=1
        return res
