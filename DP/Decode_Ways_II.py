"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
"""

# Method 1 WA - 128/173

class Solution:
    def dfs(self, memo, i, n):
        # print(n)
        if n[i:] in memo:
            return memo[n[i:]]
        
        if len(n) == 0:
            # print(n, 1)
            return 1
        
        if len(n) == 1:
            if n.count('*') == 0:
                # print(n, 1)
                return 1
            # print(n, 9)
            return 9
        
        # if len(n) == 2 and n.count('*') == 0:
        #     if int(n) <= 26:
        #         print(n, 1)
        #         return 1
            
        memo[n[i:]] = 0    
        if n[0] == "*":
            for j in range(1, 10):
                memo[n[i:]] += self.dfs(memo, i, str(j) + n[1:])
        else:
            if n[0] == '1':
                if n[1] == "0":
                    memo[n[i:]] += self.dfs(memo, i, n[2:])
                    # memo[n[i:]] += self.dfs(memo, i, n[1:])
                else:
                    memo[n[i:]] += self.dfs(memo, i, n[1:])
                    memo[n[i:]] += self.dfs(memo, i, n[2:])
                if n[1] == "*":
                    for j in range(1, 10):
                        memo[n[i:]] += self.dfs(memo, i, n[0] + str(j) + n[2:])
                    
            elif n[0] == '2':
                if n[1] == '0':
                    # memo[n[i:]] += self.dfs(memo, i, n[1:])
                    memo[n[i:]] += self.dfs(memo, i, n[2:])
                elif n[1] < '7':
                    memo[n[i:]] += self.dfs(memo, i, n[1:])
                    memo[n[i:]] += self.dfs(memo, i, n[2:])
                if n[1] == "*":
                    for j in range(1, 7):
                        memo[n[i:]] += self.dfs(memo, i, n[0] + str(j) + n[2:])
            elif n[0] > '2':
                memo[n[i:]] += self.dfs(memo, i, n[1:])
        # print(n[i:], memo[n[i:]])
        return memo[n[i:]]
                
        
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.dfs(memo, 0, s)%((10**9)+7)
        
