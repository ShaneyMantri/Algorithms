"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way. 
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cont = False
        start = False
        if word[0].isupper() and word.isupper():
            return True
        for i in range(len(word)):
            if i==0 and word[i].isupper():
                start=True
            elif i>0:
                if word[i].isupper():
                    return False
        return True
                    
