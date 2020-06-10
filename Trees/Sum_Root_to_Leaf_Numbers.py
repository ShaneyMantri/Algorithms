"""

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def dfs(self, root, s):
        if not root:
            return
        
        if root.left is None and root.right is None:
            self.res.append(s+str(root.val))
            return
        self.dfs(root.left, s+str(root.val))
        self.dfs(root.right, s+str(root.val))
        
        
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = []
        self.dfs(root, '')
        temp = 0
        for i in self.res:
            temp+=int(i)
            
        return temp
            
        
        
