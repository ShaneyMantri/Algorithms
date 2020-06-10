"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

 
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = 0
    val = None
    def dfs(self, p,  q, root):
        
        if self.flag==1:
            return
        if not root:
            return None
        if (root.val<=p.val and root.val>=q.val) or (root.val>=p.val and root.val<=q.val):
            self.val = root
            self.flag=1
            return
        self.dfs(p, q, root.left)
        self.dfs(p, q, root.right)
        
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(p, q, root)
        return self.val
