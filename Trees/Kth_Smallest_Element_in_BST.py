"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0
    var = None;
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        def traverse(root,k):
            if self.count==k:
                return
            if not root:
                return
            
            traverse(root.left,k)
            self.count+=1
            if self.count==k:
                self.var=root
                return
            traverse(root.right,k)
        
        traverse(root, k)
        return self.var.val
