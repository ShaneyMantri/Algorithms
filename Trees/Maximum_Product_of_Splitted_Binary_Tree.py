"""
Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.
Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:



Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    ms = 0
    def dfs(self, root, memo):
        if not root:
            return 0
        l = self.dfs(root.left, memo)
        self.ms += root.val
        r = self.dfs(root.right, memo)
        memo[root.val] = [l, r]
        return root.val + l + r
        
    def maxProd(self, memo):
        for k, v in memo.items():
            self.s = max(self.s, (v[1])*(self.ms - v[1]), (v[0])*(self.ms - v[0]))
        
    def maxProduct(self, root: TreeNode) -> int:
        memo = {}
        self.s = 0
        self.ms = 0
        self.dfs(root, memo)
        self.maxProd(memo)
        return self.s%((10**9) + 7)
