"""
You need to find the largest value in each row of a binary tree.

Example:

Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = {}
        
        if not root:
            return []
        
        d = deque([(root,0)])
        res[0]=root.val
        while d:
            n,l = d.popleft()
            if l in res:
                if n.val>res[l]:
                    res[l]=n.val
            else:
                res[l]=n.val
            if n.left:
                d.append((n.left, l+1))
            if n.right:
                d.append((n.right, l+1))
        return res.values()
