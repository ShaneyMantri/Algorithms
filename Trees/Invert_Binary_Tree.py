"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# METHOD 1

class Solution:
    def create(self, root):
        if not root:
            return 
        r = self.create(root.left)
        l = self.create(root.right)
        root1 = TreeNode(root.val)
        root1.left = l
        root1.right = r
        return root1
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        # root1 = TreeNode(root.val)
        if not root:
            return
        root1 = self.create(root)
        return root1
        
        
# METHOD 2 (in place)


class Solution:
    def dfs(self, root):
        if not root:
            return
        root.left, root.right=root.right, root.left
        self.dfs(root.left)
        self.dfs(root.right)
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.dfs(root)
        return root
        

