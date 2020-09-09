"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""

class Solution:
    res = 0
    def dfs(self, root, c):
        if not root.left and not root.right:
            self.res+=c*2+root.val
            return
        
        if root.left:
            self.dfs(root.left, c*2+root.val)
        if root.right:
            self.dfs(root.right, c*2+root.val)
        
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return
        self.res = 0
        self.dfs(root, 0)
        
        return self.res
