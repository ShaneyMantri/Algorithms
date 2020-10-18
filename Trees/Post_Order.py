""" 
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, root, res):
        if not root:
            return
        
        self.postOrder(root.left, res)
        self.postOrder(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postOrder(root, res)
        return res
