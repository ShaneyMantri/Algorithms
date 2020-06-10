""""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1


Return:

[
   [5,4,11,2],
   [5,8,4,5]
]



"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = []
    def dfs(self, temp, root, s,t):
        if root is None:
            return

        if t==s+root.val and (root.left is None and root.right is None):
            self.res.append(temp+[root.val])
            
        self.dfs(temp+[root.val], root.left, s+root.val,t)
        self.dfs(temp+[root.val], root.right, s+root.val,t)
            
        
        
        
        
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.dfs([], root, 0,s)
        return self.res
        
