"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    status = True
    def dfs(self, p, q, root):
        if self.status==False:
            return
        if not p and q:
            self.status = False
            return
        if not q and p:
            self.status = False
            return
        if not p and not q:
            return
            
        if p.val!=q.val:
            self.status=False
            
        self.dfs(p.left, q.right, root)
        self.dfs(p.right, q.left, root)
    
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.status = True
        self.dfs(root,root, root)
        return self.status
        
